
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from .hackathon import get_local_file_and_content, get_github_file_and_content
import os
from dotenv import load_dotenv
from on_device_requests import get_response_on_device
from aggregate import aggregate,delete_results
from url.helper import determine_severity
import json  # Add this at the top with other imports
from agregate_all_reports import get_final_report








template = """Analyze this code for vulnerabilities:
{code}

Respond in following format only:
a. Executive Summary
•	Overall risk assessment (High/Medium/Low)
•	Key findings summary
b. Vulnerability Details (for each vulnerability)
•	Title: Clear, descriptive title of the vulnerabilities
•	Summary: Brief description of the issue
•	Severity: Using a standard scoring system like CVSS (necessary field)
•	Impact: Potential consequences of the vulnerability
•	Recommendations: Suggested fixes or mitigations (not the code)
•	References: Links to relevant CWEs/CVEs (mention web links), or best practices

Do not give the updated code, just the report 
"""
# Function to create the reports folder structure
def create_reports_folder(file_path, base_folder):
    report_path = os.path.join(base_folder, file_path)
    report_dir = os.path.dirname(report_path)

    # Ensure the directory exists
    os.makedirs(report_dir, exist_ok=True)

    return report_path

def analyze_code_with_claude(file_path, content, reports_base):
    try:
        if not os.path.exists(reports_base):
            os.makedirs(reports_base)
        
        report_file = create_reports_folder(file_path + ".md", reports_base)
        
        # Write initial structure
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(f"# Vulnerability Report for `{file_path}`\n\n")
            # f.write("## Code Snippet\n")
            # f.write(f"```{os.path.splitext(file_path)[1][1:]}\n{content}\n```\n\n")
            f.write("## Vulnerability Analysis\n")

        prompt = template.format(code=content)
        response = get_response_on_device(prompt)
        
        if response:
            # Write the response to file
            with open(report_file, "a", encoding="utf-8") as f:
                f.write(response)
            
            # Format response for frontend
            return {
                'file': file_path,
                'content': response.strip(),  # Remove extra whitespace
                'severity': determine_severity(response)  # You'll need to implement this
            }
            
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return None










def main(input_path):
    delete_results()
    try:
        if input_path.startswith('http'):
            folder_structure, file_content_dict = get_github_file_and_content(input_path)
        else:
            folder_structure, file_content_dict = get_local_file_and_content(input_path)
        
        for file_path, content in file_content_dict.items():
            report = analyze_code_with_claude(file_path, content, "reports")


            # print("PRINTED REPORT ____"+ str(report))
            if report:
                yield f"data: {json.dumps({'report': report})}\n\n"
        
        document = aggregate()

        final_report=get_final_report(directory_structure=folder_structure)
        print("FINAL REPORT ____"+ str(final_report))
        
        yield f"data: {json.dumps({'completed': True})}\n\n"
        
    except Exception as e:
        yield f"data: {json.dumps({'error': str(e)})}\n\n"
     