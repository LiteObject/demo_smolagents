# Demo Smolagents - A Simple Library to Build Agents

## What are agents?
>Any efficient system using AI will need to provide LLMs some kind of access to the real world: for instance the possibility to call a search tool to get external information, or to act on certain programs in order to solve a task. In other words, LLMs should have agency. Agentic programs are the gateway to the outside world for LLMs.

>AI Agents are programs where LLM outputs control the workflow.

## Project

This Python code demonstrates the use of a `CodeAgent` from the `smolagents` library to solve a problem (finding the 20th Fibonacci number) using a language model and a web search tool. Here's a step-by-step explanation:

1. **Imports and Setup**:
   ```python
   from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
   import os
   from dotenv import load_dotenv
   load_dotenv()
   ```
   - The code imports necessary classes from the `smolagents` library: `CodeAgent` (an agent that can execute tasks), `DuckDuckGoSearchTool` (a tool for web searches), and `HfApiModel` (a model wrapper for Hugging Face API).
   - `os` and `dotenv` are used to load environment variables (e.g., API keys) from a `.env` file using `load_dotenv()`. This is typically for securely accessing credentials like a Hugging Face API token.

2. **Initialize the Model**:
   ```python
   model = HfApiModel(model_id="Qwen/Qwen2.5-72B-Instruct")
   ```
   - A Hugging Face API model (`Qwen/Qwen2.5-72B-Instruct`, a 72-billion-parameter instruction-tuned model) is initialized. This model will power the agent's reasoning and code generation.

3. **Initialize the Web Search Tool**:
   ```python
   search_tool = DuckDuckGoSearchTool()
   ```
   - A `DuckDuckGoSearchTool` is created, allowing the agent to perform web searches using DuckDuckGo if needed to solve the task.

4. **Create the CodeAgent**:
   ```python
   agent = CodeAgent(
       tools=[search_tool],
       model=model,
       max_steps=10,
       verbosity_level=1
   )
   ```
   - A `CodeAgent` is instantiated with:
     - `tools`: A list containing the `DuckDuckGoSearchTool` for web searches.
     - `model`: The Hugging Face model for reasoning and task execution.
     - `max_steps=10`: Limits the agent to 10 steps to prevent infinite loops or excessive processing.
     - `verbosity_level=1`: Enables step-by-step logging so you can see the agent's reasoning process.

5. **Define the Task**:
   ```python
   task = "What is the 20th Fibonacci number?"
   ```
   - The task is defined as a string: finding the 20th number in the Fibonacci sequence (where each number is the sum of the two preceding ones, starting with 0 and 1).

6. **Run the Agent**:
   ```python
   result = agent.run(task)
   ```
   - The `CodeAgent` processes the task. It may:
     - Use the model to reason about the Fibonacci sequence.
     - Generate code to compute the 20th Fibonacci number.
     - Optionally use the search tool if it needs external information (though for this task, it likely won't, as Fibonacci is a well-defined mathematical problem).
   - The agent iterates up to `max_steps` to arrive at a solution, logging its steps due to `verbosity_level=1`.

7. **Print the Result**:
   ```python
   print(f"Final Answer: {result}")
   ```
   - The final result (the 20th Fibonacci number) is printed. For reference, the Fibonacci sequence starts as 0, 1, 1, 2, 3, 5, 8, ..., and the 20th number is 6765.

### How It Works
- The `CodeAgent` uses the Qwen model to interpret the task and decide how to solve it. It might generate a Python function to compute the Fibonacci number (e.g., using recursion, iteration, or dynamic programming).
- If the agent lacks information or needs clarification, it could use the `DuckDuckGoSearchTool` to search the web, but for a straightforward mathematical task like this, it likely relies on the model's internal knowledge.
- The `max_steps` and `verbosity_level` ensure the process is controlled and transparent.

### Expected Output
Assuming the agent correctly computes the 20th Fibonacci number, the output would be:
```
Final Answer: 6765
```
You might also see intermediate logs (due to `verbosity_level=1`) showing the agent's reasoning, such as the code it generates or steps it takes.

### Notes
- The code assumes a `.env` file with a Hugging Face API key (e.g., `HF_API_TOKEN=your_token`) for the `HfApiModel`.
- The Qwen model is powerful but requires significant computational resources or API access.
- The `DuckDuckGoSearchTool` is included but likely unused for this specific task, as Fibonacci is a self-contained problem.