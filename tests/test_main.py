from main import add, greet


def test_greet_uses_the_name():
    assert greet("CI") == "Hello from CI!"


def test_greet_uses_default_name():
    assert greet() == "Hello from cicd-docker-practice!"


def test_adds_two_numbers():
    assert add(2, 3) == 5


def test_adds_negative_numbers():
    assert add(-2, -3) == -5
