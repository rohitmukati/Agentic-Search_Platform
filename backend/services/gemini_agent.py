import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def run_gemini_agent(keywords: str, industry: str, countries: str, services: str):
    query = f"""
    Generate a list of the top 5 B2B companies based in {countries} that provide {services} services within the {industry} industry.
    For each company, include the following details:
    - Company Name
    - Official Website URL
    - Relevant Job Titles or a Brief Company Service Description
    """


    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(query)
        text = response.text

        # 🧠 Naive lead extraction (can be improved later with regex or another Gemini call)
        lines = text.strip().split("\n")
        leads = []
        for i, line in enumerate(lines[:5]):
            leads.append({
                "company": line.strip().split("-")[0].strip() if "-" in line else f"Company {i+1}",
                "email": f"contact{i}@example.com",
                "title": line.strip(),
                "country": countries,
                "source": "Gemini",
                "contact": "https://example.com"
            })

        return leads

    except Exception as e:
        print(f"[Gemini ERROR] {e}")
        return []
