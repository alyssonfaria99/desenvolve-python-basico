def validador_senha(senha):
    arrRequisitos = [
        len(senha) >= 8,
        any(letra.isupper() for letra in senha) and any(letra.islower() for letra in senha),
        any(caracter.isdigit() for caracter in senha),
        any(not caracter.isalnum() for caracter in senha)
    ]

    if all(arrRequisitos):
        print(True)
        return True
    else:
        print(False)
        return False

validador_senha("Senha123@")
validador_senha("senhafraca")
validador_senha("Senha_fraca")