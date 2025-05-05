import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

def run_linkedin_agent(keywords: str, industry: str, countries: str, services: str):
    query = f"{keywords} {industry} {services} site:linkedin.com/in/"
    api_key = os.getenv("SERPAPI_KEY")

    if not api_key:
        raise Exception("SERPAPI_KEY not found in .env")
    country_str = countries.strip() if countries else "India"

    search = GoogleSearch({
        "q": query,
        "location": country_str,
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
            "country": country_str,
            "source": "LinkedIn",
            "contact": link
        })

    return leads
