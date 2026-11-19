from senha import MINIMO, senha_valida


def test_senha_com_exatamente_limite_caracteres_e_aceita():
    # Preparar
    senha = "a" * MINIMO  # 9 caracteres
    # Agir
    resultado = senha_valida(senha)
    # Verificar
    assert resultado is True


def test_senha_com_limite_menos_1_caracteres_e_rejeitada():
    # Preparar
    senha = "a" * (MINIMO - 1)  # 8 caracteres
    # Agir
    resultado = senha_valida(senha)
    # Verificar
    assert resultado is False


def test_senha_vazia_e_rejeitada():
    # Preparar
    senha = ""
    # Agir
    resultado = senha_valida(senha)
    # Verificar
    assert resultado is False


def test_senha_so_com_espacos_e_rejeitada():
    # Preparar
    senha = " " * (MINIMO + 2)  # 11 espaços, nada além de espaços
    # Agir
    resultado = senha_valida(senha)
    # Verificar
    assert resultado is False
