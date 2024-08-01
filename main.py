import json
import re

def parse_resume(resume_text):
    # Initialize a dictionary to store parsed data
    resume_json = {
        "name": "",
        "contact_information": "",
        "summary": "",
        "education": [],
        "experience": [],
        "skills": [],
        "certifications": [],
        "projects": [],
        "volunteer_work": []
    }

    # Example extraction (customize as needed)
    # Extract name (assuming it starts with "Name:")
    name_match = re.search(r"Name:\s*(.*)", resume_text)
    if name_match:
        resume_json["name"] = name_match.group(1).strip()

    # Extract contact information
    contact_match = re.search(r"Contact:\s*(.*)", resume_text)
    if contact_match:
        resume_json["contact_information"] = contact_match.group(1).strip()

    # Extract summary
    summary_match = re.search(r"Summary:\s*(.*)", resume_text)
    if summary_match:
        resume_json["summary"] = summary_match.group(1).strip()

    # Extract education (example for one entry)
    education_matches = re.findall(r"Education:\s*(.*)", resume_text)
    resume_json["education"] = [edu.strip() for edu in education_matches]

    # Extract experience (example for one entry)
    experience_matches = re.findall(r"Experience:\s*(.*)", resume_text)
    resume_json["experience"] = [exp.strip() for exp in experience_matches]

    # Extract skills
    skills_match = re.search(r"Skills:\s*(.*)", resume_text)
    if skills_match:
        resume_json["skills"] = [skill.strip() for skill in skills_match.group(1).split(',')]

    # Extract certifications
    certifications_match = re.search(r"Certifications:\s*(.*)", resume_text)
    if certifications_match:
        resume_json["certifications"] = [cert.strip() for cert in certifications_match.group(1).split(',')]

    # Extract projects
    projects_match = re.search(r"Projects:\s*(.*)", resume_text)
    if projects_match:
        resume_json["projects"] = [proj.strip() for proj in projects_match.group(1).split(',')]

    # Extract volunteer work
    volunteer_match = re.search(r"Volunteer Work:\s*(.*)", resume_text)
    if volunteer_match:
        resume_json["volunteer_work"] = [vol_work.strip() for vol_work in volunteer_match.group(1).split(',')]

    return resume_json

def main():
    # Sample resume text for testing
    resume_text = """Name: John Doe
Contact: johndoe@example.com
Summary: Experienced software developer.
Education: B.Sc. Computer Science, ABC University
Experience: Software Engineer at XYZ Corp
Skills: Python, Java, SQL
Certifications: Certified Python Developer
Projects: Project A, Project B
Volunteer Work: Local Charity"""

    parsed_resume = parse_resume(resume_text)
    print(json.dumps(parsed_resume, indent=4))

if __name__ == "__main__":
    main()
