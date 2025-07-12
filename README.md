# 🧠 AgentsolveX – DSA Problem Solver with AutoGen & JudgeVal

> A modular, multi-agent system that autonomously solves DSA problems using [AutoGen](https://github.com/microsoft/autogen) and monitors traceability & performance with [JudgeVal](https://github.com/JudgmentLabs/judgeval).

---

## 📁 Production-Ready Project Structure

**🧩 A dedicated notebook — `project_structure.ipynb` — is included to explain the modular architecture followed in this project.**

This notebook outlines the **best practices and folder-level organization** adopted from real-world agentic AI applications, ensuring the codebase is:
- ✅ **Scalable**
- 🔁 **Modular**
- 🧪 **Easily testable**
- 🔧 **Flexible for future extensions (like tracing, evaluation, RAG, tool orchestration)**


## 🚀 Why This Project Is Special

While many tools and even ChatGPT can solve DSA problems, **AgentsolveX** elevates this by:

✅ Using **industry-grade agent orchestration** with `AutoGen`  
✅ Structuring the entire codebase in **modular format for scalability**  
✅ Integrating **JudgeVal SDK** for **tracing, evaluation, and online performance monitoring**  
✅ Supporting **Dockerized code execution** to ensure safe and isolated runtime  
✅ Offering a clean **Streamlit UI** for real-time interaction  
✅ Designed to **plug and play custom scorers** and **evaluation pipelines**

---



## 📁 Project Architecture


```
AgentsolveX/
├── agents/
│   ├── code_executor_agent.py    # Executes code via Docker
│   └── problem_solver.py         # Plans and solves DSA problems
│
├── config/
│   ├── constant.py               # Project-wide constants
│   ├── docker_executor.py        # Docker executor configuration
│   ├── docker_utils.py           # Start/stop Docker helpers
│   └── settings.py               # Loads OpenAI model settings
│
├── judgeval_utils/
│   ├── __init__.py               # Marks the folder as a Python package
│   ├── callback_handler.py       # JudgeVal callback handler integration
│   ├── evaluation.py             # Evaluation runner and scorers
│   ├── tracing.py                # Tracer setup using JudgeVal SDK
│   └── utils.py                  # Utility methods for formatting/logging
│
├── team/
│   └── dsa_team.py               # Creates RoundRobinGroupChat with agents
│
├── app.py                        # Streamlit frontend entrypoint
├── requirements.txt              # Required packages
└── .env                          # API keys and secrets (not committed)
```




---

## 🧠 Agent Workflow

1. **User submits a DSA problem**
2. `DSA_Problem_Solver_Agent`:
   - Plans the solution
   - Writes Python code step-by-step
   - Adds relevant test cases
3. `CodeExecutorAgent`:
   - Executes the code inside a Docker container
   - Returns the output or error
4. **JudgeVal SDK**:
   - Automatically traces the entire agent interaction
   - Captures latency, usage, and performance metrics
5. The final result is shown through a beautiful Streamlit UI with avatars

---

## ⚙️ Prerequisites

- Python 3.10+
- [Docker](https://docs.docker.com/get-docker/)
- [OpenAI API Key](https://platform.openai.com/)
- [JudgeVal API Key](https://judgmentlabs.ai/)

Create a `.env` file in the root directory with:

```env
OPENAI_API_KEY=your_openai_key
JUDGMENT_API_KEY=your_judgeval_key

```

📦 Installation


```bash
git clone https://github.com/your-username/AgentsolveX.git
cd AgentsolveX
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```



▶️ Run the App

```bash
streamlit run app.py
```
