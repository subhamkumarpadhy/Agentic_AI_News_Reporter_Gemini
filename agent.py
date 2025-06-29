from crewai import Agent, LLM
from tool import tool
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model = "gemini/gemini-1.5-flash",
    verbose = True,
    temperature = 0.5,
    google_api_key = os.getenv("GEMINI_API_KEY")
)

#creating the research agent
news_researcher = Agent(
    role = "Senior Researcher",
    goal = "Uncover Groundbreaking Technologies in {topic}",
    tools = [tool],
    verbose = True,
    memory = True,
    backstory = (
        "Driven by curiosity, you are at the forefront of innovation,"
        "eager to explore and share knowledge that could change the world"
    ),
    llm = llm,
    allow_delegation = True
)

#creating a news writer agent
news_writer = Agent(
    role = "Writer",
    goal = "Narrate compelling tech stories about {topic}",
    tools = [tool],
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
        
    ),
    llm = llm,
    allow_delegation = False
)