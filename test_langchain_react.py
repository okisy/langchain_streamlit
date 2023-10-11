# from langchain.chat_models import ChatOpenAI
# from langchain import hub

import langchain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

def main():
    # chat_model = ChatOpenAI(temperature=0)

    # prompt = hub.pull("hwchase17/react-json")
    # prompt = prompt.partial(
    #     tools=render_text_description(tools),
    #     tool_names=", ".join([t.name for t in tools]),
    # )

    # chat_model_with_stop = chat_model.bind(stop=["\nObservation"])

    # from langchain.agents.output_parsers import ReActJsonSingleInputOutputParser

    # agent = {
    #     "input": lambda x: x["input"],
    #     "agent_scratchpad": lambda x: format_log_to_str(x['intermediate_steps'])
    # } | prompt | chat_model_with_stop | ReActJsonSingleInputOutputParser()

    # agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # agent_executor.invoke({"input": "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"})




    langchain.verbose = True

    llm = OpenAI(temperature=0, verbose=True)
    tools = load_tools(["serpapi", "llm-math"], llm=llm)
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")

if __name__ == '__main__':
    main()
