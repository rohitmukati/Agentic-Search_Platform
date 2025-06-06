import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

def run_google_agent(keywords: str, industry: str, countries: str, services: str):
    query = f"{keywords} {industry} {services}"
    api_key = os.getenv("SERPAPI_KEY")

    if not api_key:
        raise Exception("SERPAPI_KEY not found in .env")
    # Default country if not provided
    country_str = countries.strip() if countries else "India"
    
    search = GoogleSearch({
        "q": query,
        "location": country_str,
        "hl": "en",
        "gl": "us",
        "api_key": api_key
    })

    results = search.get_dict()
    raw_results = results.get("organic_results", [])

    leads = []
    for i, result in enumerate(raw_results[:5]):
        domain = result.get("link", "").split("/")[2] if result.get("link") else "example.com"
        email = f"info{i}@{domain}"

        lead = {
            "company": domain,
            "email": email,
            "title": result.get("title", "Web Result"),
            "country": country_str,
            "source": "Google",
            "contact": result.get("link", "")
        }
        leads.append(lead)

    return leads
