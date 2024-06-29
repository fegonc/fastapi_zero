from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Name Test',
            'password': 'test123',
            'email': 'test@example.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'Name Test',
        'email': 'test@example.com',
        'id': 1,
    }


def test_list_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'Name Test',
                'email': 'test@example.com',
                'id': 1,
            }
        ]
    }


def test_update_users(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Teste 2',
            'password': 'test123',
            'email': 'test@example.com',
        },
    )
    assert response.json() == {
        'username': 'Teste 2',
        'email': 'test@example.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'Teste 2',
            'password': 'test123',
            'email': 'test@example.com',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
