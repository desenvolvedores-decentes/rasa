def identificou_somente_servico(results):
    data = ''
    buttons = []

    if (len(results) == 0):
        data = 'Desculpa, não consegui entender. Você pode refazer a pergunta?'
    else:
        data = 'O servico que você deseja é '+ results[0]['servico'] + '?\n' + 'se sim, posso lhe ajudar com: \n' 
        if results[0]['descricao'] != None:
            buttons.append({"payload": "descricao", "title": "O que é"})
        if results[0]['etapas'] != None:
            buttons.append({"payload": "etapas", "title": "Informar o passo a passo"})
        if results[0]['horario'] != None:
            buttons.append({"payload":"horario", "title":"Qual o horario"})
        if results[0]['link'] != None:
            buttons.append({"payload":"link", "title":"link"})
        if results[0]['enderecos'] != None:
            buttons.append({"payload":"enderecos", "title":"Qual o endereço"})
    
    return data, buttons

def identificou_servico_atributos(results, attributes):
    data = ''
    buttons = []

    if (len(results) == 0):
        data = 'Desculpa, não consegui entender. Você pode refazer a pergunta?'
    elif all(att is None for att in attributes):
        data = 'O servico que você deseja é '+ results[0]['servico'] + '?\n' + 'se sim, posso lhe ajudar com: \n' 
        if results[0]['descricao'] != None:
            buttons.append({"payload": "descricao", "title": "O que é"})
        if results[0]['etapas'] != None:
            buttons.append({"payload": "etapas", "title": "Informar o passo a passo"})
        if results[0]['horario'] != None:
            buttons.append({"payload":"horario", "title":"Qual o horario"})
        if results[0]['link'] != None:
            buttons.append({"payload":"link", "title":"link"})
        if results[0]['enderecos'] != None:
            buttons.append({"payload":"enderecos", "title":"Qual o endereço"})
    else:
        for attribute in attributes:
            if (attribute != None):
                if(results[0][attribute] != None):
                    data = data + results[0][attribute] + '\n'
    return data, buttons

def solicitou_mais_sevicos(results):
    data = ''
    limite = 0

    if(len(results)<4):
        limite = len(results)
    else:
        limite = 4

    data += 'Então um desses serviço pode lhe ajudar: \n'
    for result in range(1, limite):
        data += results[result]['servico'] + '\n'

    return data
