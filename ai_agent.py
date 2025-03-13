import os
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import agentops


os.environ["AGENTOPS_API_KEY"] = "5e6b0dd4-8f11-4202-bbb4-5dabc7c94f4e"
os.environ["OPENAI_API_KEY"] = "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"



agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"), default_tags=["AI_Study_Assistant"])


llm = ChatOpenAI(model="gpt-4-turbo", temperature=0.2)

user_topic = input("Enter the topic you want to learn about: ")
user_level = input("Enter your current level (Beginner, Intermediate, Advanced): ")


overview_agent = Agent(
    name="overview_agent",
    role="Topic Expert",
    goal=f"Provide a structured and concise introduction to {user_topic}.",
    backstory="An AI that explains concepts in an easy-to-understand way.",
    llm=llm
)

study_plan_agent = Agent(
    name="study_plan_agent",
    role="Learning Guide",
    goal=f"Create a study plan for {user_topic} tailored to a {user_level} learner.",
    backstory="An AI that helps learners by providing structured study approaches.",
    llm=llm
)

code_agent = Agent(
    name="code_agent",
    role="Practice Mentor",
    goal=f"Provide {user_level}-level code examples for {user_topic} so users can practice.",
    backstory="An AI that helps users learn through hands-on coding practice.",
    llm=llm
)


task1 = Task(
    description=f"Explain {user_topic} briefly.",
    agent=overview_agent,
    expected_output=f"A beginner-friendly explanation of {user_topic}."
)

task2 = Task(
    description=f"Suggest a study plan for {user_topic} based on {user_level} level.",
    agent=study_plan_agent,
    expected_output=f"A step-by-step study plan to learn {user_topic} at a {user_level} level."
)

task3 = Task(
    description=f"Provide {user_level}-level coding exercises for {user_topic}.",
    agent=code_agent,
    expected_output=f"Practical coding exercises related to {user_topic} for a {user_level} learner."
)


crew = Crew(agents=[overview_agent, study_plan_agent, code_agent],
            tasks=[task1, task2, task3])


output = crew.kickoff()

print("\n💡 **Results:**")
print(output)