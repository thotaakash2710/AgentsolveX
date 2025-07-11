import streamlit as st
from team.dsa_team import get_dsa_team_and_docker
from config.docker_utils import start_docker_container,stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
import asyncio
import base64
import os

from judgeval.common.tracer import Tracer
from judgeval.integrations.langgraph import JudgevalCallbackHandler

tracer = Tracer(
    api_key=os.getenv("JUDGMENT_API_KEY"), 
    project_name="AgentsolveX",
    enable_monitoring=True
)

handler = JudgevalCallbackHandler(tracer)


def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()  
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("download (1).jpeg")

st.markdown(
    """
    <style>
    h1 {
        font-size: 3em;
        color: #222831;
        text-align: center;
        margin-top: 30px;
        font-weight: bold;
    }
    .stTextInput > label {
        font-size: 1.2em;
        color: #393E46;
        font-weight: 600;
    }
    .stButton > button {
        background-color: #00ADB5;
        color: white;
        border-radius: 8px;
        padding: 0.5em 2em;
        font-size: 1.1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.title("AgentsolveX -  DSA Problem Solver")
st.write("Welcome to AgentsolveX, your personal DSA problem solver powered by Autogen. Here you can ask solutions to various data structures and algorithms problems.")

task = st.text_input("Enter your DSA problem or question:",value='Enter your question here')


async def run(team,docker,task):
    try:
        await start_docker_container(docker)
        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print(msg:= f"{message.source} : {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:= f"Stop Reason: {message.stop_reason}")
                yield msg
        print("Task Completed")
    except Exception as e:
        print(f"Error: {e}")
        yield f"Error: {e}"
    finally:
        await stop_docker_container(docker)


if st.button("Run"):
    st.write("Running the Task..")

    team,docker = get_dsa_team_and_docker()

    async def collect_messages():
        async for msg in run(team,docker,task):
            if isinstance(msg, str):
                if msg.startswith("user"):
                    with st.chat_message('user',avatar='👤'):
                        st.markdown(msg)
                elif msg.startswith('DSA_Problem_Solver_Agent'):
                    with st.chat_message('assistant',avatar='🧑‍💻'):
                        st.markdown(msg)
                elif msg.startswith('CodeExecutorAgent'):
                    with st.chat_message('assistant',avatar='🤖'):
                        st.markdown(msg)
            elif isinstance(msg, TaskResult):
                with st.chat_message('stopper',avatar='🚫'):
                    st.markdown(f"Task Completed: {msg.result}")
    
    asyncio.run(collect_messages())
            
