from __future__ import annotations

import asyncio

from agents import Agent, Runner, set_tracing_disabled

"""Simple hello world agent example using LiteLLM with Claude 3.5 Sonnet.
To use this, ensure you have the ANTHROPIC_API_KEY environment variable set.
"""

set_tracing_disabled(disabled=True)


async def main():
    agent = Agent(
        name="HelloWorldAgent",
        instructions="You are a friendly hello world agent. Always greet users warmly and be helpful.",
        model="litellm/anthropic/claude-3-5-sonnet-20240620",
    )

    result = await Runner.run(agent, "Hello, please introduce yourself!")
    print(result.final_output)


if __name__ == "__main__":
    import os
    
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    if os.getenv("ANTHROPIC_API_KEY") is None:
        raise ValueError(
            "ANTHROPIC_API_KEY is not set. Please set it in a .env file or environment variable."
        )

    asyncio.run(main())