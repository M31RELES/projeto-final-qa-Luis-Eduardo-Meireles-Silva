!pip install pytest

!pytest -v --maxfail=1 --disable-warnings
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

import pytest

@pytest.mark.parametrize("numero, esperado", [
    (2, True),
    (3, True),
    (4, False),
    (13, True),
    (20, False),
    (1, False),
    (0, False),
    (-5, False)
])
def test_eh_primo(numero, esperado):
    assert eh_primo(numero) == esperado
