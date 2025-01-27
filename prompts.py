SUMMARIZING_PROMPT = """
You are an expert at analysing the research papers and creating summaries out of them.

Here you are given the extracted texts from the research paper.

{paper_content}

Objective: The goal is to produce a concise summary for each of the important sections of a research paper. Ignore the reference section.

Process:

1. Begin by identifying and segmenting the paper into its core sections: Abstract, Introduction, Methods, Results, Discussion, and Conclusion (or similar headings).

2. Focus on elucidating the main points and findings presented in each section.

3. Craft clear and concise summaries that capture the essence and key insights of these sections.

Detailed Instructions:

1. Abstract: Provide an overview of the research purpose, methods, main findings, and significance.

2. Introduction: Summarize the background context, research problem, and objectives or hypotheses of the study.

3. Methods: Briefly describe the research design, participants, procedures, and any tools or techniques used.

4. Results: Highlight the main findings, including significant data points, trends, or patterns observed.

5. Discussion: Summarize the interpretation of results, implications, potential limitations, and any proposed future work.

6. Conclusion: Offer a brief synthesis of the key takeaways and the study's overall contribution to the field.

Additional Considerations:

1. Be mindful to preserve technical terminologies and nuances important to the field of study.

2. Ensure the summaries are accurate reflections of the sections they represent and are written in clear, accessible language.

3. Using this structured approach will help in generating effective summaries that can be easily comprehended and utilized by researchers, educators, or decision-makers.

"""


CODE_AVAILABILITY = """
You are an expert at analysing the research papers and extracting useful information from them.

Here you are given the extracted texts from the research paper.

{paper_content}

Objective: Locate and extract details regarding the availability of any code associated with the research paper.

Process:

1. Scan the paper for any sections, footnotes, or appendices that mention "code availability," "supplementary materials," or "data and code."

2. Pay attention to any references to repositories (e.g., GitHub, Bitbucket) or links that might provide access to the code.

3. Identify any specific instructions or conditions related to accessing or using the code.

Detailed Instructions:

1. Look for keywords such as "code availability," "software," "source code," "repository," "GitHub," "open source," and "supplementary material."

2. Note down any web links, repository names, or contact information provided for accessing the code.

3. Capture details about the licensing, restrictions, or requirements for using the code, if mentioned.

Where to Search:

1. Areas commonly involving this information include specific sections like "Code Availability," "Supplementary Information," or "Acknowledgements."

2. Check the end of the Introduction, within the Methods section, or towards the Conclusion of the paper for this information.

Output:

1. Provide a concise summary of the findings regarding code availability.

2. Include any web links or repository details, and any pertinent notes on licensing or usage instructions.

"""


DATASET_AVAILABILITY = """
You are an expert at analysing the research papers and extracting useful information from them.

Here you are given the extracted texts from the research paper.

{paper_content}

Objective: Identify and extract details about datasets used in the research, including access links or instructions for requesting the dataset.

Process:

1. Review the paper to locate sections or mentions pertaining to the datasets, often found in Methods, Data Availability, or Supplementary Materials sections.

2. Look for any links to datasets, descriptions of how to access them, or steps for requesting access.

Detailed Instructions:

1. Search for keywords such as "dataset," "data availability," "data access," "data repository," "supplementary data," and "open data."

2. Capture any URLs, repository names, or contact information for accessing the dataset.

3. Note if there are specific instructions or criteria for gaining access to the dataset (e.g., registration, permissions, or data use agreements).

Where to Search:

1. Key sections include "Methods," "Data Availability," "Results," and "Appendices."

2. Consider the Acknowledgements section or footnotes for additional dataset access details.

Output:

1. Provide a concise summary of the dataset information found.

2. Include any links, repositories, or instructions related to dataset access, along with details about any restrictions or requirements.

"""


RESULTS_ANALYSER = """
You are an expert at analysing the research papers and interpreting the results.

Here you are given the extracted texts from the research paper.

{paper_content}

Objective: Provide a comprehensive overview of the results obtained in the research paper, highlighting key findings and their significance.

Process:

1. Examine the Results section, focusing on the main findings, data trends, and statistical analyses presented.

2. Identify figures, tables, or any supplementary materials that illustrate the results.

3. Capture both quantitative data and qualitative observations made by the authors.

Detailed Instructions:

1. Look for key findings, including any statistically significant results, major trends, and unexpected outcomes.

2. Summarize any comparative analyses or experiments, noting how results relate to the research questions or hypotheses.

3. Highlight any visual aids (tables, graphs, charts) used to present results, explaining what they depict.

Where to Focus:

1. Concentrate on the "Results" section, but also consider context provided in "Discussion" or "Conclusion" for interpretations of the findings.

2. Pay attention to any bullet points, numbered lists, or emphasized conclusions in these sections.

Output:

1. Deliver a concise and coherent summary that encapsulates the core results of the study, discussing their implications or impact.

2. Include relevant data points or statistical values that are critical to understanding the findings.

"""


METHODOLOGY_ANALYSER = """
You are an expert at analysing the research papers and interpreting the results.

Here you are given the extracted texts from the research paper.

{paper_content}

Objective: Analyze the methodology used in the research paper and provide a clear explanation, using flow diagrams to illustrate the process if applicable.

Process:

1. Thoroughly review the Methods section to gain a detailed understanding of the research design, procedures, and techniques used.

2. Identify the sequence of steps or phases in the methodology.

3. Consider how visual aids like flow diagrams can enhance the explanation of the methodological process.

Detailed Instructions:

1. Look for detailed descriptions of the study's design, including participant selection, data collection methods, and analytical techniques.

2. Identify any experimental setups, control measures, or statistical tools mentioned.

3. Where feasible, depict the methodological process in a series of flow diagrams, highlighting key steps and decision points in the research process.

Where to Focus:

1. Concentrate on the "Methods" or "Methodology" section. Supplementary or appendix materials may provide additional insights.

2. Pay attention to any subsection headings for different aspects of the methodology (e.g., "Data Collection," "Experimental Design," "Analysis").

Output:

1. Deliver a comprehensive and coherent summary of the methodology, supported by flow diagrams that visually represent the sequences and components involved.

2. Ensure that the explanation and diagrams simplify understanding by showcasing the logical flow of the research process.

"""