# research_agent_gemini.py
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.tools.reasoning import ReasoningTools
import markdown

# Load .env
load_dotenv()

# Create Gemini model instance
model = Gemini(
    id="gemini-2.0-flash",  # or "gemini-1.5-pro" if you want the latest
    api_key=os.getenv("GEMINI_API_KEY")
)

# Setup agent
agent = Agent(
    model=model,
    tools=[
        DuckDuckGoTools(),
        Newspaper4kTools(),
        ReasoningTools(),
    ],
    instructions=[
        "You're a chess news curator. Your job is to find recent news articles or announcements about the world of chess (tournaments, GMs, openings, drama, etc.).",
        "Use search and summarization tools to find the most relevant and interesting stories.",
        "Summarize your findings in clean markdown with sections like **Headline**, **Summary**, and **Source Link**.",
        "Only include content published in the past 7–10 days.",
    ],
    markdown=True
)

response = agent.run("Get the most recent and important chess news.")
print(response)