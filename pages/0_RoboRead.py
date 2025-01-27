from openai import OpenAI
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

from graph import helper_graph


PDF_NAME = "uploaded.pdf"


if "login" not in st.session_state:
    st.session_state.login = False


if not st.session_state.login:
    st.error("Please LogIn First to Use the RoboRead", icon = "🚨")
    st.stop()


st.title("RoboRead 🤖")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    # save the file
    with open(PDF_NAME, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.sidebar:
        st.subheader("PDF 📖")
        pdf_viewer(PDF_NAME)

    # execute the graph
    with st.spinner("Analysing............"):
        get_content = helper_graph.invoke({"pdf_path": PDF_NAME})

    if get_content:
        with st.expander("Paper Summary"):
            st.subheader("Summary")
            st.markdown(get_content["summary"])

        with st.expander("Code Availability"):
            st.subheader("Code Availability")
            st.markdown(get_content["code_availability"])
       
        with st.expander("Data Availability"):
            st.subheader("Data Availability")
            st.markdown(get_content["data_availability"])

       
        with st.expander("Results Overview"):
            st.subheader("Results Overview")
            st.markdown(get_content["results"])


        with st.expander("Methodology Overview"):
            st.subheader("Methodology Overview")
            st.markdown(get_content["methodology"])
            

