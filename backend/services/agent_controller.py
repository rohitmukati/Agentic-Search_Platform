from backend.schemas import SearchInput
from backend.services.google_agent import run_google_agent
from backend.services.linkedin_agent import run_linkedin_agent
# future me: from backend.services.linkedin_agent import run_linkedin_agent

def run_agents(search_input: SearchInput):
    all_leads = []

    # Call Google agent
    google_leads = run_google_agent(
        keywords=search_input.keywords,
        industry=search_input.industry,
        countries=search_input.countries,
        services=search_input.services
    )
    all_leads.extend(google_leads)

    # future: LinkedIn, blog, etc. agents bhi add kar sakte ho
    linkedin_leads = run_linkedin_agent(
        keywords=search_input.keywords,
        industry=search_input.industry,
        countries=search_input.countries,
        services=search_input.services
    )
    all_leads.extend(linkedin_leads)

    return all_leads
