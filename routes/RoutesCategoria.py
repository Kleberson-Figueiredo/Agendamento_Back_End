from flask import jsonify
from flask_restful import Resource, reqparse
from services.Categoria import Categoria
from ast import literal_eval


class CategoriaInsertRoute(Resource):

    def post(self):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('descricao_categoria', type=str, required=True)

            argumentos = parametros.parse_args()
            dados = (argumentos["descricao_categoria"])

            categoria = Categoria()
            resultado_insert = categoria.inserirCategoria(dados)

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


class CategoriaListRoute(Resource):

    def get(self):
        try:
            categoria = Categoria()
            resultset = categoria.listarCategoria()

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


class CategoriaListByIdRoute(Resource):

    def get(self, id):
        try:
            categoria = Categoria()
            resultset = categoria.listarCategoriaPorId(id)

            if resultset == 0:
                return {
                    "sucesso": False,
                    "mensagem": "Categoria nao encontrada"
                }, 404
            return jsonify(literal_eval(resultset))

        except Exception as e:
            return {
                "sucesso": False,
                "mensagem": "Erro de servidor interno, Contate o admin para mais detalhes"
            }, 500


class CategoriaUpdateRoute(Resource):
    def put(self, id):
        try:
            parametros = reqparse.RequestParser()
            parametros.add_argument('descricao_categoria', type=str, required=True)

            argumentos = parametros.parse_args()
            valores = f"descricao_categoria = '{argumentos ['descricao_categoria']}'"

            categoria = Categoria()
            categoria.atualizarCategoria(valores,id)

            return {
                "sucesso": True,
                "mensagem": "Atualizado com sucesso!"
            }, 200

        except Exception as e:
            return {
                "sucesso": False,
                "mensagem": "Erro de servidor interno, Contate o admin para mais detalhes"
            }, 500



class CategoriaDeleteRoute(Resource):
    def delete(self, id):
        try:
            categoria = Categoria()
            resultado_delete = categoria.deleteCategoria(id)

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