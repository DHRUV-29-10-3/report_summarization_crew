from report_summarization_crew.crew import ReportSummarizationCrew 

def run(): 
    # define the inputs 
    inputs = {"field": "Education"} 

    # create the crew 
    my_crew = ReportSummarizationCrew().crew()

    # pass the inputs to the crew and run the tasks
    result = my_crew.kickoff(inputs=inputs) 


if __name__ == "__main__":
    run()