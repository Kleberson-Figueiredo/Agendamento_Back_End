from flask import jsonify
from flask_restful import Resource, reqparse
from services.Cliente import Cliente
from ast import literal_eval


class ClienteInsertRoute(Resource):

    def post(self):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('nome', type=str, required=True)
            parametros.add_argument('rg', type=str, required=True)
            parametros.add_argument('cpf', type=str, required=True)
            parametros.add_argument('telefone', type=str, required=True)

            argumentos = parametros.parse_args()
            dados = (argumentos["nome"], argumentos["rg"], argumentos["cpf"],\
                     argumentos["telefone"])

            cliente = Cliente()
            resultado_insert = cliente.inserirCliente(dados)

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


class ClienteListRoute(Resource):

    def get(self):
        try:
            cliente = Cliente()
            resultset = cliente.listarCliente()

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


class ClienteListByIdRoute(Resource):

    def get(self, id):
        try:
            cliente = Cliente()
            resultset = cliente.listarClientePorId(id)

            if resultset == 0:
                return {
                    "sucesso": False,
                    "mensagem": "Cliente nao encontrado"
                }, 404
            return jsonify(literal_eval(resultset))

        except Exception as e:
            return {
                "sucesso": False,
                "mensagem": "Erro de servidor interno, Contate o admin para mais detalhes"
            }, 500


class ClienteUpdateRoute(Resource):
    def put(self, id):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('nome', type=str, required=True)
            parametros.add_argument('rg', type=str, required=True)
            parametros.add_argument('cpf', type=str, required=False)
            parametros.add_argument('telefone', type=str, required=True)

            argumentos = parametros.parse_args()

            valores = f"nome = '{argumentos ['nome']}', rg = '{argumentos ['rg']}',\
                        cpf = '{argumentos ['cpf']}', telefone = '{argumentos ['telefone']}'"

            cliente = Cliente()
            cliente.atualizarCliente(valores, id)

            return {
                "sucesso": True,
                "mensagem": "Atualizado com sucesso!"
            }, 200

        except Exception as e:
            return {
                "sucesso": False,
                "mensagem": "Erro de servidor interno, Contate o admin para mais detalhes"
            }, 500


class ClienteUpdatePatchRoute(Resource):

    def patch(self, id):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('nome', type=str, required=False)
            parametros.add_argument('rg', type=str, required=False)
            parametros.add_argument('cpf', type=str, required=False)
            parametros.add_argument('telefone', type=str, required=False)

            args = parametros.parse_args()
            dicion_args = dict(args)

            values = {chave: valor for chave, valor in dicion_args.items() if valor is not None}

            string_dados = ''
            for chave, valor in values.items():
                string_dados += f"{chave} = '{valor}', "

            cliente = Cliente()
            resultado_update = cliente.atualizarCliente(string_dados, id)

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


class ClienteDeleteRoute(Resource):
    def delete(self, id):
        try:
            cliente = Cliente()
            resultado_delete = cliente.deleteCliente(id)

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