# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from flask import request
#from flask import json
import datetime
import uuid
import os.path
import json

## inicializar a aplicaÃ§Ã£o
application = Flask(__name__)

## endpoint para testar se api esta rodando
@application.route('/')
def test():
    return 'API running!'

@application.route('/endpoint/',methods=['POST'])
def endpoint():
    ## pega os parametros que vem na request via POST
    post_params = request.get_json(cache=False)
   
    if post_params:
        ## valida existencia de algum campo obrigatÃ³rio, post_param Ã© um dicionÃ¡rio
        if ('campo' in post_params):
            try:
                
                ## AQUI FAZ A CHAMADA PRO SEU CÃDIGO QUE DE PREFERENCIA ESTA EM OUTRO ARQUIVO
                resposta = {"resposta": "valor do retorno"}

                response = application.response_class(
                        response=json.dumps(resposta),
                        status=200,
                        mimetype='application/json')

                return response

            ## retorna exeÃ§Ã£o caso de algum erro de execuÃ§Ã£o, impedindo que derrube a aplicaÃ§Ã£o
            except AssertionError as error:
                response = application.response_class(
                        response=json.dumps(error),
                        status=200,
                        mimetype='application/json')

                return response

        else: ## se falha na validaÃ§Ã£o de algum campo

            resposta =  {
                    "error": {
                        "Resposta": "ALGUM CAMPO ESTA FALTANDO",
                        "exception": ""
                    }
                    }

            response = application.response_class(
                response=json.dumps(resposta),
                status=200,
                mimetype='application/json')
            return response

    else: ## caso aconteca algum problema ao carregar a request e post_params estaja vazio 
        resposta =  {
                    "error": {
                        "Resposta": "Json nÃ£o compativel!", 
                        "exception": ""
                    }
                    }
        response = application.response_class(
                response=json.dumps(resposta),
                status=200,
                mimetype='application/json')
        return response

        

if __name__ == '__main__':
    ## mudar debug=False quando colocar em produÃ§Ã£o
    application.run(debug=True, host='0.0.0.0', port=80)
