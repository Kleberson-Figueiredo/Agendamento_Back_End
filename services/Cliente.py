from connection.Conexao import Conexao
import json

class Cliente(Conexao):

    def inserirCliente(self, dados):
        cursor = self.conexao.cursor()
        try:
            query_sql = "INSERT INTO Cliente VALUES(null, %s,%s,%s,%s)"
            cursor.execute(query_sql, dados)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0
            return cursor.rowcount
        except Exception as e:
            return e

    def listarCliente(self):
        cursor = self.conexao.cursor()
        try:
            query_sql = "SELECT * FROM Cliente"
            cursor.execute(query_sql)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                return 0
            
            dados_json = {}
            for data in resultado:
                dados_json.update({
                    data[0]:{
                        "nome": data[1],
                        "rg": data[2],
                        "cpf": data[3],
                        "telefone": data[4]
                    }
                })
            return json.dumps(dados_json)
        except Exception as e:
            return e  

    def listarClientePorId(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"SELECT * FROM Cliente WHERE idCliente = {id}"
            cursor.execute(query_sql)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                return 0

            dados_json = {}
            for data in resultado:
                dados_json.update({
                    data [0]:{
                        "nome": data[1],
                        "rg": data[2],
                        "cpf": data[3],
                        "telefone": data[4]
                    }
                })
            return json.dumps(dados_json)
        except Exception as e:
            return e    

    def atualizarCliente(self, dados, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"UPDATE Cliente SET {dados} WHERE idCliente = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0
            return cursor.rowcount
        except Exception as e:
            return e 

    def deleteCliente(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"DELETE FROM Cliente WHERE idCliente = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0
            return cursor.rowcount
        except Exception as e:
            return e 