from connection.Conexao import Conexao
import json

class Servico(Conexao):

    def inserirServico(self, dados):
        cursor = self.conexao.cursor()
        try:
            query_sql = "INSERT INTO Servico VALUES(null, %s, %s, %s)"
            cursor.execute(query_sql, dados)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0
            return cursor.rowcount
        except Exception as e:
            return e 

    def listarServico(self):
        cursor = self.conexao.cursor()
        try:
            query_sql = "SELECT * FROM Servico as  s JOIN\
                         Categoria as c ON c.idCategoria = s.categoria_fk"
            cursor.execute(query_sql)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                return 0

            dados_json = {}
            for data in resultado:
                dados_json.update({
                    data [0]:{
                        "descricao": data [1],
                        "valor": data [2],
                        "categotia_fk": data [3],
                        "descricao_categoria": data [5]
                    }
                })
            return json.dumps(dados_json)
        except Exception as e:
            return e 

    def listarServicoPorId(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"SELECT * FROM Servico as  s JOIN Categoria as c ON\
                         c.idCategoria = s.categoria_fk WHERE idServico = {id}"
            cursor.execute(query_sql)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                return 0

            dados_json = {}
            for data in resultado:
                dados_json.update({
                    data [0]:{
                        "descricao": data [1],
                        "valor": data [2],
                        "categotia_fk": data [3],
                        "descricao_categoria": data [5]
                    }
                })
            return json.dumps(dados_json)
        except Exception as e:
            return e 

    def atualizarServico(self, dados, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"UPDATE Servico SET {dados} WHERE idServico = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0
            return cursor.rowcount
        except Exception as e:
            return e 

    def deleteServico(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"DELETE FROM Servico WHERE idServico = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0
            return cursor.rowcount
        except Exception as e:
            return e 
