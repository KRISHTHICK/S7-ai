# agent.py - Simple A2A Agent
from a2a import A2ARunner

class SimpleAgent:
    def __init__(self):
        self.runner = A2ARunner()

    def run_agent(self, user_input: str) -> str:
        """
        Runs a simple A2A agent workflow that echoes back transformed input.
        """
        # Example A2A workflow (expandable later)
        response = self.runner.run(
            {
                "task": "process_input",
                "data": user_input
            }
        )
        return f"🤖 Agent Response: {response}"
