from flask import jsonify
from flask_restful import Resource, reqparse
from mysql.connector.utils import read_bytes
from services.Servico import Servico
from ast import literal_eval

parametros = reqparse.RequestParser()
parametros.add_argument('descricao_servico', type=str, required=True)
parametros.add_argument('valor', type=str, required=True)
parametros.add_argument('categoria_fk', type=str, required=False)


class ServicoInsertRoute(Resource):

    def post(self):
        try:
            

            argumentos = parametros.parse_args()
            dados = (argumentos['descricao_servico'], argumentos['valor'], argumentos['categoria_fk'])

            servico = Servico()
            resultado_insert = servico.inserirServico(dados)
           
            if resultado_insert == 0:
                return {
                    "sucesso": False,
                    "mensagem": "Erro ao inserir dados"
                }, 400
            return {
                "sucesso": True,
                "mensagem": "Dados inseridos com sucesso!"
            }, 201

        except Exception as e:
            return {
                "sucesso": False,
                "mensagem": "Erro servidor interno, Contate o admin para mais detalhes"
            },500


class ServicoListRoute(Resource):

    def get(self):
        try:
            servico = Servico()
            resultset = servico.listarServico()

            if resultset == 0:
                return {
                    "sucesso": True,
                    "mensagem": "Nenhum dado a ser exibido"
                }, 200
            return jsonify(literal_eval(resultset))

        except Exception as e:
            return {
                "sucesso": False,
                "mensagem": "Erro de servidor interno, Contate o admin para mais detalhes"
            }, 500


class ServicoListByIdRoute(Resource):

    def get(self, id):
        try:
            servico = Servico()
            resultset = servico.listarServicoPorId(id)

            if resultset == 0:
                return {
                    "sucesso": False,
                    "mensagem": "Serviço nao encontrado"
                }, 404
            return jsonify(literal_eval(resultset))

        except Exception as e:
            return {
                "sucesso": False,
                "mensagem": "Erro de servidor interno, Contate o admin para mais detalhes"
            }, 500


class ServicoUpdateRoute(Resource):
    def put(self, id):
        try:

            argumentos = parametros.parse_args()
            valores = f"descricao_servico = '{argumentos['descricao_servico']}', valor = '{argumentos['valor']}', categoria_fk = '{argumentos['categoria_fk']}'"

            servico = Servico()
            servico.atualizarServico(valores, id)

            return {
                "sucesso": True,
                "mensagem": "Atualizado com sucesso!"
            }, 200

        except Exception as e:
            return {
                "sucesso": False,
                "mensagem": "Erro de servidor interno, Contate o admin para mais detalhes"
            }, 500


class ServicoUpdatePatchRoute(Resource):

    def patch(self, id):
        try:

            args = parametros.parse_args()
            dicion_args = dict(args)

            values = {chave: valor for chave, valor in dicion_args.items() if valor is not None}

            string_dados = ''
            for chave, valor in values.items():
                string_dados += f"{chave} = '{valor}', "

            servico = Servico()
            resultado_update = servico.atualizarServico(string_dados, id)

            if resultado_update == 0:
                return {
                           "sucesso": False,
                           "mensagem": "Erro ao atualizar os dados. Contate o administrador para mais detalhes"
                       }, 400

            return {
                       "sucesso": True,
                       "mensagem": "Atualizado com sucesso!"
                   }, 200
        except Exception as e:
            return {
                       "sucesso": False,
                       "mensagem": "Erro de servidor interno. Contate o admin para mais detalhes"
                   }, 500


class ServicoDeleteRoute(Resource):
    def delete(self, id):
        try:
            servico = Servico()
            resultado_delete = servico.deleteServico(id)

            if resultado_delete == 0:
                return {
                    "sucesso": False,
                    "mensagem": "Erro ao excluir os dados. Contate o administrador para mais detalhes"
                }, 400

            return {}, 204
            
        except Exception as e:
            return {
                "sucesso": False,
                "mensagem": "Erro de servidor interno. Contate o admin para mais detalhes"
            }, 500