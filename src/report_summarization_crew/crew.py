from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

# define the crew base class --> class name should be the similar as the project name
@CrewBase
class ReportSummarizationCrew:

    # define the agents and tasks for the crew
    agents : list[BaseAgent]
    tasks : list[Task]

    # added path to the config files for agents and tasks
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # agent method name must be the same as the agent name defined in the config file
    @agent
    def report_generator(self) -> Agent:
        return Agent(name="report_generator", 
                    config=self.agents_config["report_generator"],
                    verbose=True
                    ) 

    @agent
    def report_summarizer(self) -> Agent:
        return Agent(name="report_summarizer", 
                    config=self.agents_config["report_summarizer"],
                    verbose=True
                    )
    
    # define the tasks for the crew, the task method name must be the same as the task name defined in the config file also task should be in order of execution
    
    @task
    def report_generation_task(self) -> Task:
        return Task(config=self.tasks_config["report_generation_task"],
        output_file="reports/report.md",
                    verbose=True
                    )

    @task
    def report_summarization_task(self) -> Task:
        return Task(config=self.tasks_config["report_summarization_task"],
                    output_file="reports/report_summary.md"
                    )

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents,
                    tasks=self.tasks, 
                    process=Process.sequential,
                    verbose=True
                    )
    

    


