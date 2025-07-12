from judgeval.common.tracer import Tracer

def export_trace_json(tracer: Tracer, file_path: str):
    with open(file_path, "w") as f:
        f.write(tracer.to_json())
