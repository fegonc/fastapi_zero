from http import HTTPStatus

from fast_zero.schemas import UerPublic


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


def test_list_users(client, user):
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


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': []
    }


def test_read_users_with_user(client, user):
    user_schema = UerPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_users(client, user):
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


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
