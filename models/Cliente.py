from connection.Conexao import Conexao
import json


class Cliente(Conexao):
    
    __tablename__ = "Cliente"
    
    def __init__(self, nome, rg, cpf, telefone):

        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone

    def listarClientes(self):
        Conexao.__init__(self)
        cusor = self.conexao.cursor()
        cusor.execute("SELECT * FROM Cliente")
        resultado = cusor.fetchall()
        if resultado:
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
        return None

    
    def json(self):
        return {
            "nome": self.nome,
            "rg": self.rg,
            "cpf": self.cpf,
            "telefone": self.telefone
        } 

    @classmethod
    def ListarPorCpf(cls, cpf):
        Conexao.__init__(cls)
        cursor = cls.conexao.cursor()
        cursor.execute(f"SELECT * FROM Cliente WHERE cpf = {cpf}")
        resultado = cursor.fetchall()
        if resultado:
            return resultado
        return None


    @classmethod
    def ListarClientes(cls, idCliente):
        Conexao.__init__(cls)
        cursor = cls.conexao.cursor()
        cursor.execute(f"SELECT * FROM Cliente WHERE idCliente = {idCliente}")
        resultado = cursor.fetchall()
        if resultado:
            return resultado
        return None

    def AtualizarCliente(self, dados, idCliente):
        Conexao.__init__(self)
        cursor = self.conexao.cursor()
        cursor.execute(f"UPDATE Cliente SET {dados} WHERE idCliente = {idCliente}")
        self.conexao.commit()
    
    

    def SaveCliente(self):
        cursor = self.conexao.cursor()
        query_sql = "INSERT INTO Cliente VALUES(null, %s,%s,%s,%s)"
        cursor.execute(query_sql, (self.nome, self.rg, self.cpf, self.telefone))
        self.conexao.commit()
    

    def DeleteCliente(self, idCliente):
        Conexao.__init__(self)
        cursor = self.conexao.cursor()
        query_sql = f"DELETE FROM Cliente WHERE idCliente = {idCliente}"
        cursor.execute(query_sql)
        self.conexao.commit()