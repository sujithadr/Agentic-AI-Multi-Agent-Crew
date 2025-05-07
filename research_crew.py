import os
import yaml
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

load_dotenv()
search_tool = SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))

def load_agents(config_path: str):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)['agents']
    agents = {}
    for key, a in config.items():
        agents[key] = Agent(
            role=a['role'],
            goal=a['goal'],
            backstory=a['backstory'],
            tools=[search_tool] if key == 'research_agent' else []
        )
    return agents

def load_tasks(config_path: str, agents: dict):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)['tasks']
    tasks = {}
    for t in config:
        task = Task(
            description=t['description'],
            expected_output=t['expected_output'],
            agent=agents[t['assigned_agent']],
            depends_on=[tasks[t['depends_on']]] if 'depends_on' in t else []
        )
        tasks[t['name']] = task
    return list(tasks.values())

def run_research(topic: str):
    agents = load_agents('config/agents.yaml')
    tasks = load_tasks('config/tasks.yaml', agents)
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True
    )
    return crew.kickoff(inputs={"topic": topic})

if __name__ == "__main__":
    result = run_research("How AI is transforming education")
    print("\n✅ Final Fact-Checked Report:\n")
    print(result)
