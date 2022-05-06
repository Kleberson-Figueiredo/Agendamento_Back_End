import mysql.connector
from config import *

class Conexao:

    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="HOST",
            port="PORT",
            user="USER",
            password="PASSWORD",
            database="DATABASE"
        )