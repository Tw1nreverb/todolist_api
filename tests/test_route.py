def test_task(client):
    response = client.get('/task')
    print(response.json())
    assert response.status_code == 200
