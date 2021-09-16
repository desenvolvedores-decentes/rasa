from . import response_model
from pymongo import MongoClient
from dotenv import dotenv_values

env = dotenv_values('.env')

client = MongoClient(env['URI'])
db = client[env['DATABASE']]

def get_services(service, mensagem, attributes=[]):

    data = ''
    buttons = []

    try:
        cursor = db.services.find({'servico':mensagem})
    except:
        data = "Ocorreu um problema na conexão do banco"

    results = [item for item in cursor]

    if(len(results) < 1):
        try:
            cursor = db.services.find(
                {'$text': {'$search': service}},
                {'servico': 1, 'horario': 1, 'descricao': 1, 'etapas': 1, 'enderecos': 1, 'link': 1, '_id': 0})
        except:
            data = 'Desculpe, tive um problema em pesquisar essa informação em meu banco de dados. Por favor tente mais tarde'

        results = [item for item in cursor]

    data, buttons = response_model.identificou_servico_atributos(results, attributes)

    if (data == ''):
        data = 'Desculpe, não consegui encontrar informações em meu banco de dados.'

    data += '\nConsegui lhe ajudar?'
    
    return data, buttons

def get_only_service(service, mensagem):
    
    data = ''
    buttons = []

    try:
        cursor = db.services.find({'servico':mensagem})
    except:
        data = "Ocorreu um problema na conexão do banco"

    results = [item for item in cursor]

    if(len(results) < 1):
        try:
            cursor = db.services.find(
                {'$text': {'$search': service}},
                {'servico': 1, 'horario': 1, 'descricao': 1, 'etapas': 1, 'enderecos': 1, 'link': 1, '_id': 0})
        except:
            data = 'Desculpe, tive um problema em pesquisar essa informação em meu banco de dados. Por favor tente mais tarde'

        results = [item for item in cursor]

    data, buttons = response_model.identificou_somente_servico(results)
    
    return data, buttons

def get_more_services(service, mensagem):
    
    data = ''
    buttons = []

    try:
        cursor = db.services.find({'servico':mensagem})
    except:
        data = "Ocorreu um problema na conexão do banco"

    results = [item for item in cursor]

    if(len(results) < 1):
        try:
            cursor = db.services.find(
                {'$text': {'$search': service}},
                {'servico': 1, 'horario': 1, 'descricao': 1, 'etapas': 1, 'enderecos': 1, 'link': 1, '_id': 0})
        except:
            data = 'Desculpe, tive um problema em pesquisar essa informação em meu banco de dados. Por favor tente mais tarde'

        results = [item for item in cursor]

    data = response_model.solicitou_mais_sevicos(results)
    
    return data

def close():
    return client.close()
