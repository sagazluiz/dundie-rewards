import pytest

from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


@pytest.mark.unit
@pytest.mark.parametrize("address", ["fabio@araujo.com", "joe@doe.com", "a@b.pt"])
def test_positive_check_valid_email(address):
    """Ensure e-mail is valid."""
    assert check_valid_email(address) is True


@pytest.mark.unit
@pytest.mark.parametrize("address", ["fabio@com", "@doe.com", "a@b."])
def test_negative_check_valid_email(address):
    """Ensure e-mail is invalid."""
    assert check_valid_email(address) is False


@pytest.mark.unit
def test_generate_simple_password():
    """Test generation simples password
    TODO: Generate hashed comples password, encrypted
    """
    passwords = []
    for _ in range(100):
        passwords.append(generate_simple_password(8))

    assert len(set(passwords)) == 100
