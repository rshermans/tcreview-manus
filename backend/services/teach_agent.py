import logging

logger = logging.getLogger(__name__)

def generate_pedagogical_insights(content: str) -> dict:
    """
    Simula o comportamento do Agente Teach focado em Scaffolding e no modelo AHOC.
    Em produção, chamaria a LLM com um system prompt pedagógico.
    """
    logger.info("Agente Teach analisando vieses e heurísticas...")
    
    # Mock de resposta pedagógica
    return {
        "socratic_question": "Notei que o texto afirma opiniões como fatos absolutos. Quais palavras você acha que o autor usou para tentar convencer você rapidamente?",
        "highlights": [
            {"text": "nunca visto antes", "type": "bias-sensationalist"},
            {"text": "comprovado por especialistas", "type": "bias-authority-unverified"}
        ],
        "suggested_path": "viés_de_autoriadade",
        "tokens_reward": 15
    }
