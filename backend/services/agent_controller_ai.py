from backend.schemas import SearchInput
from backend.services.google_agent import run_google_agent
from backend.services.linkedin_agent import run_linkedin_agent
from backend.services.gemini_agent import run_gemini_agent

def run_agentic_pipeline(search_input: SearchInput):
    all_leads = []

    # ✅ Google Agent
    google_leads = run_google_agent(
        keywords=search_input.keywords,
        industry=search_input.industry,
        countries=search_input.countries,
        services=search_input.services
    )
    all_leads.extend(google_leads)

    # ✅ LinkedIn Agent
    linkedin_leads = run_linkedin_agent(
        keywords=search_input.keywords,
        industry=search_input.industry,
        countries=search_input.countries,
        services=search_input.services
    )
    all_leads.extend(linkedin_leads)

    # ✅ Gemini Agent
    gemini_leads = run_gemini_agent(
        keywords=search_input.keywords,
        industry=search_input.industry,
        countries=search_input.countries,
        services=search_input.services
    )
    all_leads.extend(gemini_leads)

    return all_leads
