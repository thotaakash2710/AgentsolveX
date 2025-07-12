import os
from judgeval.common.tracer import Tracer

def get_tracer():
    return Tracer(
        api_key=os.getenv("JUDGMENT_API_KEY"),
        project_name="AgentsolveX",
        enable_monitoring=True
    )
