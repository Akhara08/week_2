import autogen

# Configuration (disable Docker)
config = {
    "code_execution_config": {
        "use_docker": False
    }
}

# Pass config using **config to unpack it into keyword arguments
assistant = autogen.AssistantAgent("assistant", **config)
user_proxy = autogen.UserProxyAgent("user_proxy", **config)

# Start the chat
user_proxy.initiate_chat(
    assistant,
    message="Show me the YTD gain of 10 largest technology companies as of today."
)
