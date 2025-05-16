import autogen

config_list = [
    {
        'model': 'gpt-4o-mini',
        'api_key': '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'  # Replace with your actual API key
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
        code_execution_config={"work_dir": "web", "use_docker": False},  # Docker disabled here
        llm_config=llm_config,
        system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
    )

    task1 = "Write python code to output numbers 1 to 100, and then store the code in a file"
    print("Sending Task 1...")
    user_proxy.initiate_chat(assistant, message=task1)

    task2 = "Change the code in the file you just created to instead output numbers 1 to 200"
    print("Sending Task 2...")
    user_proxy.initiate_chat(assistant, message=task2)

if __name__ == "__main__":
    main()
