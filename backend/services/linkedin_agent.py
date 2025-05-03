import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

def run_linkedin_agent(keywords: str, industry: str, countries: list, services: str):
    query = f"{keywords} {industry} {services} site:linkedin.com/in/"
    api_key = os.getenv("SERPAPI_KEY")

    if not api_key:
        raise Exception("SERPAPI_KEY not found in .env")

    search = GoogleSearch({
        "q": query,
        "location": countries[0] if countries else "India",
        "hl": "en",
        "gl": "us",
        "api_key": api_key
    })

    results = search.get_dict()
    profiles = results.get("organic_results", [])

    leads = []
    for i, profile in enumerate(profiles[:5]):
        link = profile.get("link", "")
        title = profile.get("title", "LinkedIn Profile")
        domain = "linkedin.com"
        email = f"profile{i}@{domain}"

        leads.append({
            "company": "LinkedIn Profile",
            "email": email,
            "title": title,
            "country": countries[0],
            "source": "LinkedIn",
            "contact": link
        })

    return leads
