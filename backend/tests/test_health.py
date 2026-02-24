def test_health_check(client):
    """Testa o endpoint de saúde da API."""
    response = client.get('/api/health')

    # Verifica o código de status
    assert response.status_code == 200

    # Verifica o conteúdo do JSON
    data = response.get_json()
    assert data['status'] == 'ok'
    assert data['message'] == 'TrueCheck API está funcionando'
