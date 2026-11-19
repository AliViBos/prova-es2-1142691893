MINIMO = 9  # TROQUE pelo seu LIMITE


def senha_valida(senha):
    if not senha or senha.isspace():
        return False
    return len(senha) >= MINIMO
