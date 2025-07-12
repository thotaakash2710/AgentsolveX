from judgeval.integrations.langgraph import JudgevalCallbackHandler
from judgeval_utils.tracing import get_tracer

def get_callback_handler():
    tracer = get_tracer()
    return JudgevalCallbackHandler(tracer)
