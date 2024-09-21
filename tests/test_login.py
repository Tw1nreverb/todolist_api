def test_login_route(client):
    response = client.post('/user/login')
    assert response.status_code == 200

def test_register_route(client):
    response = client.post('/user/register')
    assert response.status_code == 200

