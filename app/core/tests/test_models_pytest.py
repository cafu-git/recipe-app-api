from django.contrib.auth import get_user_model
import pytest


@pytest.mark.django_db
def test_create_user_with_email_successful():
    """Test creating a new user with an email is successful"""
    email = "test@gmail.com"
    password = "Testpass123"
    user_model = get_user_model()
    user = user_model.objects.create_user(email=email, password=password)
    # user = user_model.objects.get(email=email)
    assert user.email == email
    assert user.check_password(password) is True
