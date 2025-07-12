from judgeval.evaluation import Evaluation
from judgeval.scorers.abilities import Faithfulness, Relevance, InstructionAdherence

def get_evaluation():
    return Evaluation(
        scorers=[
            Faithfulness(),
            Relevance(),
            InstructionAdherence(),
        ]
    )
