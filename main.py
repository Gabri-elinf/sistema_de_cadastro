#Importa de módulo (db.py) as funções conectar e criar_banco_e_tabela.
#conectar -> Conexão com o Mysql.
#criar_banco_e_tabela -> Garantir que o banco e as tabelas necessárias existam.
from db import conectar, criar_banco_e_tabela

#Importa do módulo (app.py).
#Representa a interface gráfica de botões, campos de texto, tabelas e lógica de interação com o usuário.
from app import AppCadastro

#A condição verifica se o arquivo atual está sendo executado diretamente e não importado.
#Quando o arquivo é executado pelo __name__ = __main__.
#Quando é importado por outro arquivo, __name__ contém o nome do módulo.
if __name__ == '__main__':

    try:
        c = conectar(usar_banco=False)
        criar_banco_e_tabela(c)
        c.close()

    except Exception:
        pass

    #Cria uma instância da classe "AppCadastro", a janela principal do programa.
    #Ao ser criada, monta toda a interface gráfica e conecta automaticamente ao db.
    app = AppCadastro()

    #Executa o loop principal da interface Tkinter.
    #Mantém a janela aberta e escuta as ações do usuário, permanecendo ativo, até que seja fechado o programa.
    app.mainloop()