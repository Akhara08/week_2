import autogen
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

config_list = [
    {
        'model': 'gpt-4o-mini',
        'api_key': os.getenv('OPENAI_API_KEY')  # Load API key from .env
    }
]

llm_config = {
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

def main():
    assistant = autogen.AssistantAgent(
        name="CTO",
        llm_config=llm_config,
        system_message="Chief technical officer of a tech company"
    )

    user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        code_execution_config={"work_dir": "web", "use_docker": False},
        llm_config=llm_config,
        system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
    )

    # Task 1: Write code for 1 to 100
    task1 = (
        "Write a Python script named 'numbers.py' that outputs numbers from 1 to 100 "
        "to a file 'output.txt', with 10 numbers per line separated by spaces."
    )
    print("Sending Task 1...")
    user_proxy.initiate_chat(assistant, message=task1)

    # Wait for termination on Task 1
    while True:
        response = user_proxy.step(assistant)
        print("Assistant:", response["content"])
        if user_proxy.is_termination_msg(response):
            break

    # Task 2: Modify code to output 1 to 200 instead
    task2 = (
        "Modify the 'numbers.py' script you created so it outputs numbers from 1 to 200 "
        "to the same 'output.txt', keeping the same formatting (10 numbers per line)."
    )
    print("Sending Task 2...")
    user_proxy.initiate_chat(assistant, message=task2)

    # Wait for termination on Task 2
    while True:
        response = user_proxy.step(assistant)
        print("Assistant:", response["content"])
        if user_proxy.is_termination_msg(response):
            break


if __name__ == "__main__":
    main()
