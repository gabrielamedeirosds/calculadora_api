import time
import json
from loguru import logger
from service import responses
from service.constants import mensagens
import pandas as pd
import numpy as np


class CalculadoraService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_MODEL)
        self.load_model()

    def load_model(self):

        logger.debug(mensagens.FIM_LOAD_MODEL)

    def executar_calc(self, value):

        response = {}

        logger.debug(mensagens.INICIO_CALCULO)
        start_time = time.time()

        response_predicts = self.buscar_predicao(value['value1'], value['value2'], value['operacao'])
        

        logger.debug(mensagens.FIM_CALCULO)
        logger.debug(f"Fim de todas as predições em {time.time()-start_time}")
        response = {
                    "Resultado da operacao": response_predicts}

        return response

    def buscar_predicao(self, value1, value2, operacao):
        
        logger.debug('Iniciando o calculo...')

        if operacao[0] == '+':
            response = value1[0] + value2[0]
            
        elif operacao[0] == '-':
            response = value1[0] - value2[0]
        
        elif operacao[0] == '*':
            response = value1[0] * value2[0]

        elif operacao[0] == '/':
            response = value1[0] / value2[0]

        print(response)

        return response
       