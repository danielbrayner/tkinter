

def check_cpf_func(cpf):
    import re

    while True:

        #Verificando se os "." e "-" estao no lugar certo e se o tamanho do cpf eh 14
        if (len(cpf) != 14 or cpf[3] != "." or cpf[7] != "." or cpf[11] != "-"):
            return "CPF no formato inválido.", "error"
            break

        #Verificando se existem caracteres alem de "numeros", "." e "-".
        if (re.search(r'[^(0-9\-.)]', cpf) != None):
            return 'CPF inválido.', "error"
            break

        #Deixando o cpf apenas com numeros
        cpf_so_numeros = re.sub(r"[^a-zA-Z0-9]","",cpf)

        #Verificando se os numeros do CPF são repeditos.
        if(len(set(cpf_so_numeros[:9])) == 1):
            return "Os 09 primeiros dígitos do CPF não podem ser iguais.", "error"
            break

        #Calculando primeiro digito verificador.
        somatorio = 0
        j = 10

        for i in range(0, 9):
            somatorio = somatorio + (j * int(cpf_so_numeros[i]))
            j = j - 1

        resto = somatorio % 11
        if (resto == 0 or resto == 1):
            digito_verificador_1 = 0
        else:
            digito_verificador_1 = 11 - resto

        #Calculando segundo digito verificador
        somatorio = 0
        j = 11
        for i in range(0, 10):
            somatorio = somatorio + (j * int(cpf_so_numeros[i]))
            j = j - 1

        resto = somatorio % 11
        if (resto == 0 or resto == 1):
            digito_verificador_2 = 0
        else:
            digito_verificador_2 = 11 - resto


        if (digito_verificador_1 == int(cpf[12]) and digito_verificador_2 == int(cpf[13])):
            return "CPF válido.", "confirmed"
            break
        else:
            return "CPF inválido.", "error"
            break