from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langgraph.graph import MessagesState
from typing import  Annotated
import operator
from openai import OpenAI
from langgraph.graph import START, END, StateGraph
from langchain_core.runnables import RunnableConfig
import PyPDF2
import streamlit as st
import os

import prompts as pt



os.environ["LANGCHAIN_TRACING_V2"] = st.secrets["LANGCHAIN_TRACING_V2"]
os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]
os.environ["LANGCHAIN_ENDPOINT"] = st.secrets["LANGCHAIN_ENDPOINT"]
os.environ["LANGCHAIN_PROJECT"] = st.secrets["LANGCHAIN_PROJECT"]
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


# set the openai model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
# create client
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


# states
class BotState(MessagesState):
    pdf_path: str
    content: str
    summary: str
    code_availability: str
    data_availability: str
    results: str
    methodology: str


# state functions
def extract_text_from_pdf(pdf_path: str) -> str:
    pdf_text = ""
    # read the pdf
    with open(pdf_path, 'rb') as file_:
        reader = PyPDF2.PdfReader(file_)
        # extract the text
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            pdf_text += page.extract_text()

    final_text = pdf_text.strip().replace("\n", "")

    return final_text


def pdf_data_extractor(state: BotState):
    pdf_path = state["pdf_path"]
    extracted_text = extract_text_from_pdf(pdf_path)

    return {"content": extracted_text}


def paper_summary_extractor(state: BotState):
    pdf_text = state["content"]

    # create the system message
    summarise_message = [SystemMessage(pt.SUMMARIZING_PROMPT.format(paper_content = pdf_text))]
    # invoke the llm
    summary_result = llm.invoke(summarise_message)

    return {"summary": summary_result.content}


def code_availability_checker(state: BotState):
    pdf_text = state["content"]

    # crete the code extractor prompt
    code_message = [SystemMessage(pt.CODE_AVAILABILITY.format(paper_content = pdf_text))]

    # invoke the llm
    code_result = llm.invoke(code_message)

    return {"code_availability": code_result.content}


def dataset_details_extractor(state: BotState):
    pdf_text = state["content"]

    # crete the code extractor prompt
    data_message = [SystemMessage(pt.DATASET_AVAILABILITY.format(paper_content = pdf_text))]

    # invoke the llm
    data_result = llm.invoke(data_message)

    return {"data_availability": data_result.content}


def results_analyser(state: BotState):
    pdf_text = state["content"]

    # crete the code extractor prompt
    results_message = [SystemMessage(pt.RESULTS_ANALYSER.format(paper_content = pdf_text))]

    # invoke the llm
    result_info = llm.invoke(results_message)

    return {"results": result_info.content}


def methodology_extractor(state: BotState):
    pdf_text = state["content"]

    # crete the code extractor prompt
    method_message = [SystemMessage(pt.METHODOLOGY_ANALYSER.format(paper_content = pdf_text))]

    # invoke the llm
    method_info = llm.invoke(method_message)

    return {"methodology": method_info.content}


# add nodes and edges
helper_builder = StateGraph(BotState)
helper_builder.add_node("pdf_text_extractor", pdf_data_extractor)
helper_builder.add_node("summary_extractor", paper_summary_extractor)
helper_builder.add_node("code_extractor", code_availability_checker)
helper_builder.add_node("dataset_extractor", dataset_details_extractor)
helper_builder.add_node("results_analyzer", results_analyser)
helper_builder.add_node("methodology_analyzer", methodology_extractor)

# build graph
helper_builder.add_edge(START, "pdf_text_extractor")
helper_builder.add_edge("pdf_text_extractor", "summary_extractor")
helper_builder.add_edge("pdf_text_extractor", "code_extractor")
helper_builder.add_edge("pdf_text_extractor", "dataset_extractor")
helper_builder.add_edge("pdf_text_extractor", "results_analyzer")
helper_builder.add_edge("pdf_text_extractor", "methodology_analyzer")
helper_builder.add_edge(["summary_extractor", "code_extractor", "dataset_extractor", "results_analyzer", "methodology_analyzer"], END)

# compile the graph
helper_graph = helper_builder.compile()


