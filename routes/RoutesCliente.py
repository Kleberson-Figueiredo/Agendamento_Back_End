from flask_restful import Resource, reqparse
from models.Cliente import Cliente
from connection.Conexao import Conexao
from ast import literal_eval




parametros = reqparse.RequestParser()
parametros.add_argument('nome', type=str, required=True,help='Nome é obrigatório')
parametros.add_argument('rg', type=str, required=True, help='RG é obrigatório')
parametros.add_argument('cpf', type=str, required=True,help='CPF é obrigatório')
parametros.add_argument('telefone', type=str, required=True, help='Telefone é obrigatório')

class Clientes(Resource):
    def get(self):
        cliente = Cliente.listarClientes(self)
        if cliente:
            return literal_eval(cliente)
        return {
            "sucesso": False,
            "mensagem": "Nenhum dado a ser exibido" }
class CadastroCliente(Resource):
    def post(self):
        dados = parametros.parse_args()

        if Cliente.ListarPorCpf(dados['cpf']):
            return {'message': 'Cliente já cadastrado'}, 400
        cliente = Cliente(**dados)
        cliente.SaveCliente()
        return {'message': 'Cliente cadastrado com sucesso'}, 201
    
class ClienteRoutes(Resource):
    def get(self, id):
        try:
            cliente = Cliente.ListarClientes(id)
            if cliente:
                return cliente
            return {'message': 'Cliente não encontrado'}, 404
        except:
            return {'message': 'Erro de servidor interno, Contate o admin para mais detalhes'}, 500

    def put(self, id):

        dados = parametros.parse_args()
        valores = f"nome = '{dados['nome']}', rg = '{dados['rg']}',\
         cpf = '{dados['cpf']}', telefone = '{dados['telefone']}'"

        try:
            enc_cliente = Cliente.ListarClientes(id)
            if enc_cliente:
                Cliente.AtualizarCliente(self, valores, id)
                return {'message': 'Cliente atualizado'}, 200
            cliente = Cliente(**dados)
            cliente.SaveCliente()
            return {'message': 'Cliente cadastrado com sucesso'}, 201
        except:
            return {'message': 'Erro de servidor interno, Contate o admin para mais detalhes'}, 500
    
    def delete(self, id):
        try:
            cliente = Cliente.ListarClientes(id)
            if cliente:
                 Cliente.DeleteCliente(self, id)
                 return {'message': 'Cliente deletado'}, 200
            return {'message': 'Cliente não encontrado'}, 404
        except: 
            return {'message': 'Erro de servidor interno, Contate o admin para mais detalhes'}, 500

