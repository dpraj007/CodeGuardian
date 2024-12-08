from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from typing import List
from dotenv import load_dotenv
import os

load_dotenv("url/.env")
api_claude = os.getenv('LLM_TOKEN')
# print(api_claude)

def init_claude():
    return ChatAnthropic(
        model_name="claude-3-haiku-20240307",
        temperature=0,
        api_key=str(api_claude)
    )

def get_final_report(directory_structure: str = "") -> str:
    """
    Generate a comprehensive security report from individual vulnerability reports.
    
    Args:
        directory_structure (str): String representation of the repository structure
    
    Returns:
        str: The generated security report in markdown format
    """
    Claude_haiku_model = init_claude()
    
    # Read the individual reports
    try:
        with open('document.md', 'r', encoding='utf-8') as file:
            small_reports = file.read()
    except FileNotFoundError:
        raise FileNotFoundError("document.md not found. Please ensure the file exists.")

    final_report_template = """You are a cybersecurity expert tasked with synthesizing multiple code vulnerability reports into a single, comprehensive summary. You are provided with individual reports for each file from a GitHub repository: {small_reports}. This is the repo's directory structure: {directory_structure}. Your goal is to create a concise yet thorough aggregated report that highlights the most critical issues and provides an overall security assessment.
    Please follow these guidelines:
    1. Executive Summary:
       - Provide an overall risk assessment for the entire codebase (High/medium/low)
       - Summarize the most critical vulnerabilities across all files.
       - Highlight any patterns or recurring issues.

    2. Key Findings:
       - List the top 5 most severe vulnerabilities, regardless of which file they appear in.
       - For each, include:
       - Vulnerability title
       - Affected file(s) and their location in {directory_structure}
       - Severity score
       - Brief impact statement

    3. Vulnerability Statistics:
       - Total number of vulnerabilities found
       - Breakdown of vulnerabilities by severity (High, Medium, Low)

    4. Detailed Vulnerability Analysis:
       - For each unique vulnerability type found:
       - Provide a general description
       - List affected files
       - Explain the potential impact on the overall system
       
    5. Recommendations:
       - Prioritized list of actions to address the most critical issues
       - Any overarching security improvements for the entire codebase

    Format the report using markdown for readability. Use tables for statistical data and bullet points for lists. Highlight critical information using bold text.

    Your task is to analyze the individual reports, identify patterns, and create a cohesive narrative about the overall security state of the codebase. Focus on providing actionable insights and clear priorities for the development team."""

    prompt = final_report_template.format(
        directory_structure=directory_structure,
        small_reports=small_reports
    )
    
    try:
        response = Claude_haiku_model.invoke(prompt)
        report_content = response.content

        # Save the report to a file
        with open('final_report.md', 'w', encoding='utf-8') as file:
            file.write(report_content)

        # Convert Markdown to HTML
        html = markdown.markdown(report_content, extensions=['tables', 'fenced_code'])

        # Save HTML to a file (optional, for debugging)
        with open('final_report.html', 'w', encoding='utf-8') as file:
            file.write(html)

        # Convert HTML to PDF
        pdfkit.from_string(html, 'final_report.pdf')
        static_dir = os.path.join(os.getcwd(), 'static')
        if not os.path.exists(static_dir):
            os.makedirs(static_dir)
        shutil.copy('final_report.pdf', os.path.join(static_dir, 'final_report.pdf'))

        return report_content
    except Exception as e:
        raise Exception(f"Error generating report: {str(e)}")

def test_report_generation():
    """
    Test function to demonstrate the usage of the report generator
    """
    # Sample directory structure
    sample_directory = """
    /project
    ├── src/
    │   ├── main.py
    │   └── utils.py
    ├── tests/
    │   └── test_main.py
    └── README.md
    """
    
    # Create a sample document.md file
    sample_report = """
    # Security Analysis for main.py
    - **Severity**: High
    - **Issue**: Hardcoded credentials found
    - **Location**: Line 45
    - **Description**: API keys stored in plaintext
    
    # Security Analysis for utils.py
    - **Severity**: Medium
    - **Issue**: Insufficient input validation
    - **Location**: Line 23
    - **Description**: Potential SQL injection vulnerability
    """
    
    with open('document.md', 'w', encoding='utf-8') as file:
        file.write(sample_report)
    
    try:
        # Generate the report
        final_report = get_final_report(sample_directory)
        print("Report generated successfully!")
        print("\nReport preview:")
        print(final_report[:500] + "...")  # Print first 500 characters
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Clean up test file
        if os.path.exists('document.md'):
            os.remove('document.md')

# if __name__ == "__main__":
#     test_report_generation()