import pytest
from services.llm_service import final_evaluation

def test_final_evaluation_calculation():
    """Testa a lógica de cálculo da avaliação final no serviço"""
    user_perception = {'reliability': 10, 'factual': 20} # média 15
    ai_analysis = {'reliability': 30, 'factual': 40} # média 35

    # final_score = (15 * 0.3) + (35 * 0.7) = 4.5 + 24.5 = 29
    result = final_evaluation(user_perception, ai_analysis)

    assert result['final_score'] == 29
    assert result['user_vs_ai_discrepancy'] == 20

def test_final_evaluation_empty_input():
    """Testa o comportamento com dicionários vazios (deve retornar 0.0 em vez de erro)"""
    result = final_evaluation({}, {})
    assert result['final_score'] == 0
    assert result['user_vs_ai_discrepancy'] == 0

def test_final_evaluation_non_numeric_input():
    """Testa o comportamento com valores não numéricos (deve ignorar e não falhar)"""
    # Deve ignorar 'invalid' e tirar média apenas de 10 -> média 10
    user_perception = {'a': 'invalid', 'b': 10}
    ai_analysis = {'c': 20} # média 20

    # final_score = (10 * 0.3) + (20 * 0.7) = 3 + 14 = 17
    result = final_evaluation(user_perception, ai_analysis)
    assert result['final_score'] == 17
    assert result['user_vs_ai_discrepancy'] == 10
