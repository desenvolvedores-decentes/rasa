# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from . import database
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, UserUtteranceReverted, AllSlotsReset

import sys
sys.path.append('.')

# Action responsável por consultar dados no banco de dados
# de serviços da Prefeitura de Fortaleza.
class ActionPesquisaInfoBanco(Action):

    def name(self) -> Text:
        return 'action_pesquisa_info_banco'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # ao ser chamado, a action inicialmente captura o conteúdo
        # do slot servico e salva em uma variável para ser enviada
        # ao scritp do banco. 
        service = tracker.get_slot('servico')
        mensagem = tracker.latest_message['text']


        # alem do serviço a ser consultado no banco, é também repassado
        # um array de attributos relacionados a este serviço, como 
        # por exemplo, o horário de funcionamento, o endereço, etc.
        # aqui é instanciado um array vazio.
        attributes = []
        
        # é capturado o valor do slot 'descricao' e armazenado em uma
        # variável chamada descricao. Caso o valor seja diferente de 
        # None, isto é, existe algum valor capturado no diálogo, este
        # conteúdo é ignorado e substituído pela string 'descricao'.
        # Isto é necessário porque ao consultar no banco pela descricao
        # de um serviço, a chave enviada deve ser exatamente 'descricao'
        # e não o conteúdo do slot.
        descricao = tracker.get_slot('descricao')
        if(descricao != None):
            descricao = 'descricao'
            attributes.append(descricao)

        # o mesmo procedimento que é feito para o slot descricao é
        # feito para os outros slots
        horario = tracker.get_slot('horario')
        if(horario != None):
            horario = 'horario'
            attributes.append(horario)

        # o mesmo procedimento que é feito para o slot descricao é
        # feito para os outros slots
        etapas = tracker.get_slot('etapas')
        if(etapas != None):
            etapas = 'etapas'
            attributes.append(etapas)
        
        # o mesmo procedimento que é feito para o slot descricao é
        # feito para os outros slots
        endereco = tracker.get_slot('endereco')
        if(endereco != None):
            endereco = 'enderecos'
            attributes.append(endereco)

        # o mesmo procedimento que é feito para o slot descricao é
        # feito para os outros slots
        link = tracker.get_slot('link')
        if(link != None):
            link = 'link'
            attributes.append(link)

        # após todas a verificações de slots, são adicionados todos
        # a o array de attributos para ser enviado a função
        # de consulta ao banco
        # os dados são enviados ao serviço de consulta ao banco
        # passado os parâmetros de serviço e attributos do servico
        # e a resposta é armazenada na variável 'data'
        if(len(attributes) > 0):
            data, buttons = database.get_services(service, mensagem, attributes)
        else:
            data, buttons = database.get_only_service(service, mensagem)

        # a mensagem construida na variável 'data' é então enviada
        # ao diálogo.
        dispatcher.utter_message(text=data, buttons=buttons)
        database.close()

        return []
        # Reverter o estado do diálogo ao estado anterior da chamada à action.
        # return [UserUtteranceReverted()]

        # Resetar todos os slots após a chamada da action
        # return [AllSlotsReset()]


class ActionPesquisaMaisServicosBanco(Action):

    def name(self) -> Text:
        return 'action_pesquisa_mais_servico_banco'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # ao ser chamado, a action inicialmente captura o conteúdo
        # do slot servico e salva em uma variável para ser enviada
        # ao scritp do banco. 
        service = tracker.get_slot('servico')
        mensagem = tracker.latest_message['text']

        data = database.get_more_services(service, mensagem)

        # a mensagem construida na variável 'data' é então enviada
        # ao diálogo.
        dispatcher.utter_message(text=data)
        database.close()

        return []
        # Reverter o estado do diálogo ao estado anterior da chamada à action.
        # return [UserUtteranceReverted()]

        # Resetar todos os slots após a chamada da action
        # return [AllSlotsReset()]
