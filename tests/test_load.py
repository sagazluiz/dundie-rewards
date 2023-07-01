import os
import uuid
import pytest
from dundie.core import load
from .constants import PEOPLE_FILE

def setup_module():
    print()
    print("roda antes dos testes do modulo\n")

def teardown_module():
    print()
    print("roda depois dos testes desse modulo\n")


@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    file_ = tmpdir.join("newfile.txt")
    file_.write("isso é sujeira...")
    yield
    file_.remove()



@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test function load functions"""

    file_path = f"arquivo_indesejado-{uuid.uuid4()}.txt"
    request.addfinalizer(lambda: os.unlink(file_path))

    request.addfinalizer(lambda: print("Terminou"))

    with open(file_path, "w") as file_:
        file_.write("dados uteis somente para o teste")

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'

def test_load2():
    """Test function load functions"""

    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as file_:
        file_.write("dados uteis somente para o teste")

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'
