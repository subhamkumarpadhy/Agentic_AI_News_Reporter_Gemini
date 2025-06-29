from crewai import Crew, Process
from task import research_task, write_task
from agent import news_researcher, news_writer

crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process = Process.sequential
)

result = crew.kickoff(inputs={'topic': 'World War -2'})
print(result)