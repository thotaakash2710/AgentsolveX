# 🧠 AgentsolveX – DSA Problem Solver with AutoGen & JudgeVal

> A modular, multi-agent system that autonomously solves DSA problems using [AutoGen](https://github.com/microsoft/autogen) and monitors traceability & performance with [JudgeVal](https://github.com/JudgmentLabs/judgeval).

---

## 🚀 Why This Project Is Special

While many tools and even ChatGPT can solve DSA problems, **AgentsolveX** elevates this by:

✅ Using **industry-grade agent orchestration** with `AutoGen`  
✅ Structuring the entire codebase in **modular format for scalability**  
✅ Integrating **JudgeVal SDK** for **tracing, evaluation, and online performance monitoring**  
✅ Supporting **Dockerized code execution** to ensure safe and isolated runtime  
✅ Offering a clean **Streamlit UI** for real-time interaction  
✅ Designed to **plug and play custom scorers** and **evaluation pipelines**

---

## 🧩 Project Architecture

## 📁 Project Architecture

AgentsolveX/  
├── agents/  
│   ├── code_executor_agent.py        # Executes code via Docker  
│   └── problem_solver.py             # Plans and solves DSA problems  
│  
├── config/  
│   ├── constant.py  
│   ├── docker_executor.py  
│   ├── docker_utils.py  
│   └── settings.py  
│  
├── evaluation/  
│   ├── scorer_config.py              # Custom scorer setup  
│   └── online_eval.py                # Online eval logic (optional extension)  
│  
├── monitoring/  
│   └── trace_manager.py              # Centralized Tracer instance setup  
│  
├── team/  
│   └── dsa_team.py                   # Creates RoundRobinGroupChat  
│  
├── app.py                            # Streamlit frontend  
├── requirements.txt  
└── .env                              # Environment variables (not committed)
