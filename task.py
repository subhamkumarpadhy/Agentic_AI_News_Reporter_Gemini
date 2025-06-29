from crewai import Task
from tool import tool
from agent import news_researcher, news_writer

#Research Task
research_task = Task(
    description= (
        "Identify the next big trend in {topic}"
        "Focus on identifying pros and corns and the overall narrative."
        "Your final report should clearly articulate the key points, "
        "it's market opportunities and potential risks."
    ),
    expected_output='A comprehensive 3 paragraph long report on the latest AI trnends.',
    tools=[tool],
    agent= news_researcher
)


#Writing Task
write_task = Task(
    description= (
        "Compose an insightful articel on {topic}"
        "Focus on the latest trends and how it's impacting the industry."
        "zthis articel should be easy to understand, engaging and positive."
    ),
    expected_output='A 4 paragraph artical on {topic} advancements formatted as markdown.',
    tools=[tool],
    agent= news_writer,
    async_execution= False
)