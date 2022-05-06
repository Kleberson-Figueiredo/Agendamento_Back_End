from connection.Conexao import Conexao
import json

class Categoria(Conexao):

    def inserirCategoria(self,dados):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"INSERT INTO Categoria VALUES(null, '{dados}')"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0
            return cursor.rowcount
        except Exception as e:
            return e 

    def  listarCategoria(self):
        cursor = self.conexao.cursor()
        try:
            query_sql = "SELECT * FROM Categoria"
            cursor.execute(query_sql)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                return 0

            dados_json = {}
            for data in resultado:
                dados_json.update({
                    data [0]:{
                        "descricao_categoria": data[1]
                    }
                })
            return json.dumps(dados_json)
        except Exception as e:
            return e 

    def listarCategoriaPorId(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"SELECT * FROM Categoria WHERE idCategoria = {id}"
            cursor.execute(query_sql)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                return 0
            
            dados_json = {}
            for data in resultado:
                dados_json.update({
                    data [0]:{
                        "descricao_categoria": data[1]
                    }
                })
            return json.dumps(dados_json)
        except Exception as e:
            return e

    def atualizarCategoria(self, dados, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"UPDATE Categoria SET {dados} WHERE idCategoria = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0
            return cursor.rowcount
        except Exception as e:
            return e 

    def deleteCategoria(self, id):
        cursor = self.conexao.cursor()
        try:
            query_sql = f"DELETE FROM Categoria WHERE idCategoria = {id}"
            cursor.execute(query_sql)
            self.conexao.commit()

            if cursor.rowcount < 1:
                return 0
            return cursor.rowcount
        except Exception as e:
            return e