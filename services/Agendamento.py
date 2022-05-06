from connection.Conexao import Conexao
import json

class Agendamento(Conexao):

    def inserirAgendamento(self, dados):
        cursor = self.conexao.cursor()
        try:
            query_sql = "INSERT INTO Agendamento VALUES(null, %s, %s, %s, %s, %s)"
            cursor.execute(query_sql, dados)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0
            return cursor.rowcount
        except Exception as e:
            return e
    
    def listarAgendamento(self):
        cursor = self.conexao.cursor()
        try:
            query_sql = "SELECT * FROM db_agendamento.Agendamento as a JOIN\
                         db_agendamento.Cliente as c ON c.idCliente = a.cliente_fk JOIN\
                         db_agendamento.Servico as s ON s.idServico = a.servico_fk"
            cursor.execute(query_sql)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                return 0
            
            dados_json = {}
            for data in resultado:
                dados_json.update({
                    data [0]:{
                        "data": str(data [1]),
                        "hora_inicio": str(data [2]),
                        "hora_fim": str(data [3]),
                        "id_cliente": data [6],
                        "nome_cliente": data [7],
                        "rg": data [8],
                        "cpf": data [9],
                        "telefone": data [10],
                        "id_servico": data [11],
                        "descricao": data [12],
                        "valor": data [13],
                        "categoria_fk": data [14]
                    } 
                })
            return json.dumps(dados_json)
        except Exception as e:
            return e

    def listarAgendamentoPorId(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"SELECT * FROM db_agendamento.Agendamento as a JOIN\
                         db_agendamento.Cliente as c ON c.idCliente = a.cliente_fk JOIN\
                         db_agendamento.Servico as s ON s.idServico = a.servico_fk\
                         WHERE idAgendamento = {id}"

            cursor.execute(query_sql)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                return 0
            
            dados_json = {}
            for data in resultado:
                dados_json.update({
                    data [0]:{
                        "data": str(data [1]),
                        "hora_inicio": str(data [2]),
                        "hora_fim": str(data [3]),
                        "id_cliente": data [6],
                        "nome_cliente": data [7],
                        "rg": data [8],
                        "cpf": data [9],
                        "telefone": data [10],
                        "id_servico": data [11],
                        "descricao": data [12],
                        "valor": data [13],
                        "categoria_fk": data [14]
                    }
                })
            return json.dumps(dados_json)
        except Exception as e:
            return e

    def atualizarAgendamento(self, dados, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"UPDATE Agendamento SET {dados} WHERE idAgendamento = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0

            return cursor.rowcount            
        except Exception as e :
            return e

    def deleteAgendamento(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"DELETE FROM Agendamento WHERE idAgendamento = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount == 0:
                return 0
            return cursor.rowcount
        except Exception as e:
            return e