from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='test name', email='test@example.com', password='test123')
    session.add(user)
    session.commit()
    session.refresh(user)
    result = session.scalar(select(User).where(User.email == 'test@example.com'))

    assert result.username == 'test name'
