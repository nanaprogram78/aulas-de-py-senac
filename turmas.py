from platform import node
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askyesno
import mysql.connector
from mysql.connector import Error

# Variáveis globais
global hostX
global userX
global passwordX
global databaseX
global cursorX
global comando_sql_criar_database
global comando_sql_criar_table 
global comando_sql_inserir
global comando_sql_select
global comando_sql_seguranca
global comando_sql_deletar
global caixa_combo_diasX
global caixa_combo_mesesX
global caixa_combo_anosX
global caixa_combo_turnox

# Dados para conexão com o banco de dados
hostX = 'localhost'
userX = 'root'
passwordX = 'acesso123'
databaseX = 'senacpy'

# Instruções SQL
comando_sql_criar_database = "CREATE DATABASE IF NOT EXISTS senacpy"
comando_sql_criar_table = "CREATE TABLE IF NOT EXISTS `alunospy` (`ra_aluno` int NOT NULL AUTO_INCREMENT,`nome_aluno` varchar(80) NOT NULL,`celular` varchar(11) NOT NULL,`data_nasc` date NOT NULL,`curso` varchar(60) NOT NULL, PRIMARY KEY (`ra_aluno`)) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"
comando_sql_inserir = "INSERT INTO alunospy (nome_aluno, celular, data_nasc, curso) VALUES(%s, %s, %s, %s)"
comando_sql_select = "SELECT * FROM alunospy;"
comando_sql_seguranca = "SET SQL_SAFE_UPDATES = 0;"
comando_sql_deletar = "DELETE FROM alunospy WHERE ra_aluno=%s;"

caixa_combo_diasX = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
caixa_combo_mesesX = ['01','02','03','04','05','06','07','08','09','10','11','12']
caixa_combo_anosX = ["1900","1901","1902","1903","1904","1905","1906","1907","1908","1909","1910","1911","1912","1913","1914","1915","1916","1917","1918","1919","1920","1921","1922","1923","1924","1925","1926","1927","1928","1929","1930","1931","1932","1933","1934","1935","1936","1937","1938","1939","1940","1941","1942","1943","1944","1945","1946","1947","1948","1949","1950","1951","1952","1953","1954","1955","1956","1957","1958","1959","1960","1961","1962","1963","1964","1965","1966","1967","1968","1969","1970","1971","1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006"]
caixa_combo_turnox = ["Manhã","Tarde","Noite"]

# Lista de mensagens
mensagem_bd = ['Erro de Conexão ao banco de dados.',
               'Erro ao criar banco de dados.',
               'Erro ao criar tabela no banco de dados.',
               'Registro cadastrado com sucesso',
               'Erro ao cadastrar o registro',
               'Erro ao deletar o cadastro',
               'Deseja deletar o registro selecionado?']

# Função para conectar o banco de dados.
def conectar():
    global banco
    try:
        banco = mysql.connector.connect(
        host = hostX, 
        user = userX,
        password = passwordX)
        #print('Conexão 0: ', banco)
    except Error as erro:
        print(mensagem_bd[0])
    
# Função para criar o banco de dados
def criar_database():
    global banco
    try:
        conectar()
        cursorX = banco.cursor()
        cursorX.execute(comando_sql_criar_database)        
    except Error as erro:
        print(mensagem_bd[1])
        
    if banco.is_connected():
        cursorX.close()

# Função para criar tabela
def criar_tabela():
    global banco
    try:
        banco = mysql.connector.connect(
            host = hostX,
            user = userX,
            password = passwordX,
            database = databaseX
        )

        cursorX = banco.cursor()
        cursorX.execute(comando_sql_criar_table)
    except Error as erro:
        print(mensagem_bd[2])
        
    if banco.is_connected():
            banco.close()
    
# Inserir novo registro
def inserir_novo_aluno():
    global banco
    entry_ra['state'] = 'normal'
    entry_ra.delete(0,'end')
    entry_ra['state'] = 'disabled'
    
    banco = mysql.connector.connect(
        host=hostX,
        user=userX,
        password=passwordX,
        database=databaseX
    )
    
    cursorX = banco.cursor()
    cursorX.execute(comando_sql_criar_table)
    try:
        if banco.is_connected():
            agrupa_data = str(caixa_combo_anos.get() + '-' + caixa_combo_meses.get() + '-'+ caixa_combo_dias.get())
            dados = (str(entry_nome.get()), str(entry_numero.get()), str(agrupa_data), str(entry_cursoaluno.get()))
            cursorX.execute(comando_sql_inserir, dados)
            banco.commit()
            messagebox.showinfo('AVISO', mensagem_bd[3])
    except:
        messagebox.showerror('ERRO', mensagem_bd[4])
        
    desconecta_banco()
    
# Exibe os registros do banco de dados
def mostrar_todos_registros():
    banco = mysql.connector.connect(
        host=hostX,
        user=userX,
        password=passwordX,
        database=databaseX
    )
 
    if banco.is_connected():
        tree_ferramentas.delete(*tree_ferramentas.get_children(None))
        cursorX = banco.cursor()
        cursorX.execute(comando_sql_select)
        dados_tabela = cursorX.fetchall()
        #print(dados_tabela)
        for i in range(0, len(dados_tabela)):
            tree_ferramentas.insert(parent='', index=i, values=dados_tabela[i])

# Deletar o registro selecionado no banco de dados            
def deletar_registro():
    deletar_reg = messagebox.askyesno('ATENÇÃO', mensagem_bd[5])

    curItem = tree_ferramentas.focus()
    valor = tree_ferramentas.item(curItem)
    lista_valores = valor['values']
    
    try:
        if deletar_reg:
            banco = mysql.connector.connect(
                host=hostX,
                user=userX,
                password=passwordX,
                database=databaseX
            )
            if banco.is_connected():
                tree_ferramentas.delete(curItem)
                cursorX = banco.cursor()
                dados = [(lista_valores[0])]
                cursorX.execute(comando_sql_seguranca)
                cursorX.execute(comando_sql_deletar, dados)
                banco.commit()
    except:
        messagebox.showerror('ERRO', mensagem_bd[5])

# Desconecta banco
def desconecta_banco():
    if banco.is_connected():
        banco.close()
    
# Janela principal 
janela = Tk()
janela.title('Sistema acadêmico')
janela.geometry('850x400')

janela.configure(bg='white')
janela.resizable(width=FALSE, height=FALSE)


# JANELA 
label_cadastro = Label(janela, text='Cadastro de Turmas', fg='orange', bg='white', font=('Arial','16'), justify='center')
label_cadastro.pack(side=TOP)

# FRAME 1 
label_ra = Label(text='ID da Turma', fg='black', bg='white', font=('Arial','12'))
label_ra.place(x=80,y=80)

entry_ra = Entry(font=('Arial','12'), relief='solid')
entry_ra.place(x=175, y=82, height=28,width=250)

entry_ra['state'] = 'disabled'

label_IDprofessor = Label(text='ID professor', fg='black', bg='white', font=('Arial','12'))
label_IDprofessor.place(x=80, y=120)

entry_IDprofessor = Entry(font=('Arial','12'), relief='solid')
entry_IDprofessor.place(x=175,y=122,height=28,width=500)

label_IDCursos = Label(text='ID Curso', fg='black', bg='white', font=('Arial','12'))
label_IDCursos.place(x=100,y=160)

entry_IDCursos = Entry(font=('Arial','12'), relief='solid')
entry_IDCursos.place(x=175,y=162,height=28,width=500)

label_turno = Label(text='Turno', fg='black', bg='white', font=('Arial','12'))
label_turno.place(x=120,y=200)

escolher_dia = StringVar()
caixa_combo_dias = ttk.Combobox( textvariable=escolher_dia)
caixa_combo_dias['values']=caixa_combo_turnox
caixa_combo_dias.place(x=175, y=200, width=180, height=28)


label_datainicio = Label(text='Data de início', fg='black', bg='white', font=('Arial','12'))
label_datainicio.place(x=70,y=240)

escolher_dia = StringVar()
caixa_combo_dias = ttk.Combobox( textvariable=escolher_dia)
caixa_combo_dias['values']=caixa_combo_diasX
caixa_combo_dias.place(x=175, y=240, width=45, height=28)

escolher_meses = StringVar()
caixa_combo_meses = ttk.Combobox( textvariable=escolher_meses)
caixa_combo_meses['values']=caixa_combo_mesesX
caixa_combo_meses.place(x=242, y=240, width=45, height=28)

escolher_anos = StringVar()
caixa_combo_anos = ttk.Combobox(textvariable=escolher_anos)
caixa_combo_anos['values']=caixa_combo_anosX
caixa_combo_anos.place(x=309, y=240, width=50, height=28)

label_datafinal = Label(text='Data Final', fg='black', bg='white', font=('Arial','12'))
label_datafinal.place(x=95,y=280)

escolher_dia = StringVar()
caixa_combo_dias = ttk.Combobox( textvariable=escolher_dia)
caixa_combo_dias['values']=caixa_combo_diasX
caixa_combo_dias.place(x=175, y=280, width=45, height=28)

escolher_meses = StringVar()
caixa_combo_meses = ttk.Combobox( textvariable=escolher_meses)
caixa_combo_meses['values']=caixa_combo_mesesX
caixa_combo_meses.place(x=242, y=280, width=45, height=28)

escolher_anos = StringVar()
caixa_combo_anos = ttk.Combobox(textvariable=escolher_anos)
caixa_combo_anos['values']=caixa_combo_anosX
caixa_combo_anos.place(x=309, y=280, width=50, height=28)

label_cargahoraria = Label(text='Carga Horária', fg='black', bg='white', font=('Arial','12'))
label_cargahoraria .place(x=70,y=320)

entry_cargahoraria  = Entry(font=('Arial','12'), relief='solid')
entry_cargahoraria .place(x=175,y=322,height=28,width=250)

style_ferramentas = ttk.Style()
style_ferramentas.theme_use("vista")



# Botões
botao_inserir = Button(text='Inserir',relief='groove',command=inserir_novo_aluno,font=('Arial','12'), fg='black', activeforeground='orange')
botao_inserir.place(x=500,y=322,width=80,height=30)

botao_excluir = Button(text='Excluir',command=deletar_registro,font=('Arial','12'),relief='groove', fg='black', activeforeground='orange')
botao_excluir.place(x=600,y=322,width=80,height=30)

#conectar()
#criar_database()
#criar_tabela()
janela.mainloop()