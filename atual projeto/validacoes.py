#Essa função serve para validar o CPF do cliente.
def cadastrocpf(cpf):
    #validação do CPF do cliente
    cpf = [int(char) for char in cpf if char.isdigit()]
 
    if len(cpf) != 11: #faz a verificação se o CPF do cliente tem mesmo 11 dígitos
        return False
    
    if cpf == cpf [::-1]: #verifica se tem todos os números iguais, pois mesmos com os números sendo considerados inválidos, eles passam na verificação
        return False

    for i in range(9, 11): #valida os dois dígitos verificadores
        valor = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digito = ((valor * 10) % 11) % 10
        if digito != cpf[i]:
            return False
    return True


