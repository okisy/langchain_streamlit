from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
llm = OpenAI(model_name="text-davinci-002")
with get_openai_callback() as cb:
    result = llm("Tell me a joke")
    print(result)
    print("---")
    print(cb)

# Outputs:
# Tokens Used: 42
#      Prompt Tokens: 4
#      Completion Tokens: 38
# Successful Requests: 1
# Total Cost (USD): $0.00084