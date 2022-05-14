from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from routes.RoutesAgendamento import *
from routes.RoutesCategoria import *
from routes.RoutesCliente import *
from routes.RoutesServico import *


app = Flask(__name__)
api = Api(app)
cors = CORS(app)

# Rotas para Agendamento
api.add_resource(AgendamentoInsertRoute, "/agendamento")                #post
api.add_resource(AgendamentoListRoute, "/agendamento")                  #get
api.add_resource(AgendamentoListByIdRoute, "/agendamento/<id>")         #get
api.add_resource(AgendamentoUpdateRoute, "/agendamento/<id>")           #put
api.add_resource(AgendamentoUpdatePatchRoute, "/agendamento/<id>")      #patch
api.add_resource(AgendamentoDeleteRoute, "/agendamento/<id>")           #delete

# Rotas para Categoria 
api.add_resource(CategoriaInsertRoute, "/categoria")                    #post
api.add_resource(CategoriaListRoute, "/categoria")                      #get    
api.add_resource(CategoriaListByIdRoute, "/categoria/<id>")             #get
api.add_resource(CategoriaUpdateRoute, "/categoria/<id>")               #put
api.add_resource(CategoriaDeleteRoute, "/categoria/<id>")               #delete

# Rotas para Cliente  
api.add_resource(Clientes, "/cliente")                       #get
api.add_resource(CadastroCliente, "/cadastro_cliente")                 #post
api.add_resource(ClienteRoutes, "/cliente/<id>")                   #get #put #delete


# Rotas para Servico 
api.add_resource(ServicoInsertRoute, "/servico")                        #post
api.add_resource(ServicoListRoute, "/servico")                          #get
api.add_resource(ServicoListByIdRoute, "/servico/<id>")                 #get
api.add_resource(ServicoUpdateRoute, "/servico/<id>")                   #put
api.add_resource(ServicoUpdatePatchRoute, "/servico/<id>")              #patch
api.add_resource(ServicoDeleteRoute, "/servico/<id>")                   #delete


if __name__=="__main__":

    app.run(port=4000, debug=True)