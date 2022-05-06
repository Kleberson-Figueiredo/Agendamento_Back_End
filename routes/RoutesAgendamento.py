from flask import jsonify
from flask_restful import Resource, reqparse
from services.Agendamento import Agendamento
from ast import literal_eval


class AgendamentoInsertRoute(Resource):

    def post(self):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('data', type=str, required=True)
            parametros.add_argument('hora_inicio', type=str, required=True)
            parametros.add_argument('hora_fim', type=str, required=True)
            parametros.add_argument('cliente_fk', type=str, required=False)
            parametros.add_argument('servico_fk', type=str, required=False)
    
            argumentos = parametros.parse_args()
            dados = (argumentos["data"], argumentos["hora_inicio"],\
                     argumentos["hora_fim"], argumentos["cliente_fk"],\
                     argumentos["servico_fk"])

            agendamento = Agendamento()
            resultado_insert = agendamento.inserirAgendamento(dados)

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


class AgendamentoListRoute(Resource):

    def get(self):
        try:
            agendamento = Agendamento()
            resultset = agendamento.listarAgendamento()

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


class AgendamentoListByIdRoute(Resource):

    def get(self, id):
        try:
            agendamento = Agendamento()
            resultset = agendamento.listarAgendamentoPorId(id)

            if resultset == 0:
                return {
                    "sucesso": False,
                    "mensagem": "Agendamento nao encontrado"
                }, 404
            return jsonify(literal_eval(resultset))

        except Exception as e:
            return {
                "sucesso": False,
                "mensagem": "Erro de servidor interno, Contate o admin para mais detalhes"
            }, 500


class AgendamentoUpdateRoute(Resource):
    def put(self, id):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('data', type=str, required=True)
            parametros.add_argument('hora_inicio', type=str, required=True)
            parametros.add_argument('hora_fim', type=str, required=True)
            parametros.add_argument('cliente_fk', type=str, required=False)
            parametros.add_argument('servico_fk', type=str, required=False)

            argumentos = parametros.parse_args()
            valores = f"data = '{argumentos['data']}', hora_inicio = '{argumentos['hora_inicio']}', hora_fim = '{argumentos['hora_fim']}', cliente_fk = '{argumentos['cliente_fk']}', servico_fk = '{argumentos['servico_fk']}'"

            agendamento = Agendamento()
            agendamento.atualizarAgendamento(valores, id)

            return {
                "sucesso": True,
                "mensagem": "Atualizado com sucesso!"
            }, 200

        except Exception as e:
            return {
                "sucesso": False,
                "mensagem": "Erro de servidor interno, Contate o admin para mais detalhes"
            }, 500


class AgendamentoUpdatePatchRoute(Resource):

    def patch(self, id):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('data', type=str, required=True)
            parametros.add_argument('hora_inicio', type=str, required=True)
            parametros.add_argument('hora_fim', type=str, required=True)
            parametros.add_argument('cliente_kf', type=str, required=False)
            parametros.add_argument('servico_fk', type=str, required=False)

            args = parametros.parse_args()
            dicion_args = dict(args)

            values = {chave: valor for chave, valor in dicion_args.items() if valor is not None}

            string_dados = ''
            for chave, valor in values.items():
                string_dados += f"{chave} = '{valor}', "

            agendamento = Agendamento()
            resultado_update = agendamento.atualizarAgendamento(string_dados, id)

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


class AgendamentoDeleteRoute(Resource):
    def delete(self, id):
        try:
            agendamento = Agendamento()
            resultado_delete = agendamento.deleteAgendamento(id)

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