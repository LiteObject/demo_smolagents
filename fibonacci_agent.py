from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the model: This model will power the agent's reasoning and code generation.
model = HfApiModel(model_id="Qwen/Qwen2.5-72B-Instruct")

# Initialize the web search tool
search_tool = DuckDuckGoSearchTool()

# Create the CodeAgent
agent = CodeAgent(
    tools=[search_tool],
    model=model,
    max_steps=10,  # Limit the number of steps to prevent infinite loops
    verbosity_level=1  # Print step-by-step logs
)

# Define the task as a string
task = "What is the 20th Fibonacci number?"

# Run the agent
result = agent.run(task)

# Print the final result
print(f"Final Answer: {result}")