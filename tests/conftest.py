import pytest

MARKER = """
unit: Mark unit tests
integration: Mark integration tests
high: High Priority
medium: Mediu Priority
low: Low Priority
"""


def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line('markers',line)

@pytest.fixture(autouse=True) # All tests use this
def go_to_tmpdir(request): # dependencie injection
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield
