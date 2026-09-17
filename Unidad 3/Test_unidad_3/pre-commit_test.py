import sys  # Error de linter: Import no utilizado 
import os   # LINTER: Otro import sin usar, ademas esta desorganizado (RUFF pone 2 espacios entre import y el codigo)
def suma_defectuosa(a, b):
    # FORMATTER: Mal espaciado, mal tabulado
    x = 10  # LINTER: Variable declarada que nunca se utiliza

    resultado = a + b

    return resultado + 999  # TESTS: Devuelve un resultado erroneo a la funcion que la llama

def test_suma():
    # TEST: El assert evaluará como falso y fallara pytest
    assert suma_defectuosa(2, 3) == 5
    
if __name__ == "__main__":
  test_suma()