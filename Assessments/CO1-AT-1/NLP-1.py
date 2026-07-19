import re

resume = """
Name: Dharani Devi Thanappagari
Email: dharani@gmail.com
Mobile: 9876543210
Skills: Python, SQL, Machine Learning, NLP
Experience: 3 years
"""

# Extract Name
name = re.search(r"Name:\s*(.*)", resume)

# Extract Email
email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume)

# Extract Mobile Number
mobile = re.findall(r"\b[6-9]\d{9}\b", resume)

# Extract Skills
skill_list = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
skills_found = []

for skill in skill_list:
    if re.search(skill, resume, re.IGNORECASE):
        skills_found.append(skill)

# Extract Experience
experience = re.search(r"(\d+)\s+years?", resume, re.IGNORECASE)

years = 0
if experience:
    years = int(experience.group(1))

# Display Summary
print("===== Candidate Profile =====")

if name:
    print("Name :", name.group(1))

print("Email :", email)

print("Mobile :", mobile)

print("Skills :", skills_found)

print("Experience :", years, "Years")

print("\n===== Eligibility Check =====")

if years >= 2 and "Python" in skills_found:
    print("Candidate is ELIGIBLE for Shortlisting.")
else:
    print("Candidate is NOT ELIGIBLE.")
