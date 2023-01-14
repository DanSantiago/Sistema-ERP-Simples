import sqlite3

# cria a database
dbase1 = sqlite3.connect('dados.db')
c1 = dbase1.cursor()
dbase1.execute(''' CREATE TABLE IF NOT EXISTS produtos( 
                   PRODUTO TEXT NOT NULL,
                   COD INT NOT NULL,
                   CATEGORIA TEXT NOT NULL,
                   MARCA TEXT NOT NULL,
                   ESTOMIN INT NOT NULL,
                   ESTOMAX INT NOT NULL,
                   PRODOBS TEXT NOT NULL,
                   PRECO REAL NOT NULL,
                   VENDATAC REAL NOT NULL,
                   VENDVAR REAL NOT NULL,
                   QUANT INT NOT NULL,
                   INSUMO TEXT NOT NULL)''')

c1 = dbase1.cursor()
dbase1.execute('''CREATE TABLE IF NOT EXISTS clientes(
                  NOME TEXT NOT NULL,
                  COD INT NOT NULL,
                  RG TEXT NOT NULL,
                  CPF TEXT NOT NULL,
                  CELULAR TEXT NOT NULL,
                  TELEFONE TEXT NOT NULL,
                  EMAIL TEXT NOT NULL,
                  OBSERVACAO TEXT NOT NULL,
                  CEP TEXT NOT NULL,
                  ENDERECO TEXT NOT NULL,
                  NUMERO TEXT NOT NULL,
                  BAIRRO TEXT NOT NULL,
                  CIDADE TEXT NOT NULL,
                  ESTADO TEXT NOT NULL)''')


c1 = dbase1.cursor()
dbase1.execute('''CREATE TABLE IF NOT EXISTS regvendas(
                  VALOR REAL NOT NULL,
                  DIA TEXT NOT NULL)''')


c1 = dbase1.cursor()
dbase1.execute('''CREATE TABLE IF NOT EXISTS regcompras(
                  VALOR REAL NOT NULL,
                  DIA TEXT NOT NULL)''')


c1 = dbase1.cursor()
dbase1.execute('''CREATE TABLE IF NOT EXISTS login(
                  NOMELOJA TEXT NOT NULL,
                  NOMEUSUARIO TEXT NOT NULL,
                  SENHA TEXT NOT NULL,
                  CARGO TEXT NOT NULL)''')


c1 = dbase1.cursor()
dbase1.execute('''CREATE TABLE IF NOT EXISTS registro(
                  ATIVIDADE TEXT NOT NULL)''')


c1 = dbase1.cursor()
dbase1.execute(''' CREATE TABLE IF NOT EXISTS vendas( 
                   CLIENTE TEXT NOT NULL,
                   PRODUTO TEXT NOT NULL,
                   QUANT INT NOT NULL,
                   VALOR REAL NOT NULL,
                   DESCONTO REAL NOT NULL,
                   FRETE REAL NOT NULL,
                   TOTAL REAL NOT NULL,
                   PAGAMENTO TEXT NOT NULL,
                   NPARCELAS INT NOT NULL,
                   VALPAR REAL NOT NULL,
                   VENCIMENTO TEXT NOT NULL)''')


# aplica as mudanças no database
dbase1.commit()


#########################################################################TABELA DOS CLIENTES##########################################################################################################
def add_clientes(NOME, COD, RG, CPF, CELULAR, TELEFONE, EMAIL, OBSERVACAO, CEP, ENDERECO, NUMERO, BAIRRO, CIDADE, ESTADO):
    c1.execute('''INSERT into clientes (NOME, COD, RG, CPF, CELULAR, TELEFONE, EMAIL, OBSERVACAO, CEP, ENDERECO, NUMERO, BAIRRO, CIDADE, ESTADO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (NOME, COD, RG, CPF, CELULAR, TELEFONE, EMAIL, OBSERVACAO, CEP, ENDERECO, NUMERO, BAIRRO, CIDADE, ESTADO))
    dbase1.commit()


def rmv_clientes(x):
    c1.execute('''delete from clientes where (COD, NOME) = (?, ?)''', x)
    dbase1.commit()


def read_clientes():
    c1 = dbase1.cursor()
    c1.execute('''SELECT COD, NOME from clientes''')
    data = c1.fetchall()
    dbase1.commit()
    return data


def show_clientes_info(x):
    c1 = dbase1.cursor()
    c1.execute('''SELECT NOME, COD, RG, CPF, CELULAR, TELEFONE, EMAIL, OBSERVACAO, CEP, ENDERECO, NUMERO, BAIRRO, CIDADE, ESTADO from clientes where (COD, NOME) = (?, ?)''', x)
    data = c1.fetchone()
    return data


def pick_clientes_info(x):
    c1 = dbase1.cursor()
    c1.execute('''SELECT NOME, COD, RG, CPF, CELULAR, TELEFONE, EMAIL, OBSERVACAO, CEP, ENDERECO, NUMERO, BAIRRO, CIDADE, ESTADO from clientes where (COD, NOME) = (?, ?)''', x)
    data = c1.fetchone()
    return data


def att_clientes(NOME, COD, RG, CPF, CELULAR, TELEFONE, EMAIL, OBSERVACAO, CEP, ENDERECO, NUMERO, BAIRRO, CIDADE, ESTADO, x):
    c1 = dbase1.cursor()
    d1 = (NOME, COD, RG, CPF, CELULAR, TELEFONE, EMAIL, OBSERVACAO, CEP, ENDERECO, NUMERO, BAIRRO, CIDADE, ESTADO, )
    d2 = d1 + x
    c1.execute('''UPDATE clientes set NOME = ?, COD = ?, RG = ?, CPF = ?, CELULAR = ?, TELEFONE = ?, EMAIL = ?, OBSERVACAO = ?, CEP = ?, ENDERECO = ?, NUMERO = ?, BAIRRO = ?, CIDADE = ?, ESTADO = ? where (COD, NOME) = (?, ?)''', d2)
    dbase1.commit()


def clie_geracode():
    c1 = dbase1.cursor()
    c1.execute('''SELECT MAX(COD) FROM clientes''')
    teste = c1.fetchone()

    if teste[0] == None:
        return 0
    else:
        return teste[0] + 1


def checa_clicode():
    c1 = dbase1.cursor()
    c1.execute('''SELECT COD from clientes''')
    data = c1.fetchall()
    dbase1.commit()
    return data


def checa_cli():
    c1 = dbase1.cursor()
    c1.execute('''SELECT NOME from clientes''')
    data = c1.fetchall()
    dbase1.commit()
    return data


#########################################################################TABELA DOS PRODUTOS###########################################################################################################
def add_produtos(PRODUTO, COD, CATEGORIA, MARCA, ESTOMIN, ESTOMAX, PRODOBS, PRECO, VENDATAC, VENDAVAR, QUANT, INSUMO):
    c1.execute('''INSERT into produtos (PRODUTO, COD, CATEGORIA, MARCA, ESTOMIN, ESTOMAX, PRODOBS, PRECO, VENDATAC, VENDVAR, QUANT, INSUMO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (PRODUTO, COD, CATEGORIA, MARCA, ESTOMIN, ESTOMAX, PRODOBS, PRECO, VENDATAC, VENDAVAR, QUANT, INSUMO))
    dbase1.commit()


def rmv_produtos(x):
    c1.execute('''delete from produtos where (COD, PRODUTO) = (?, ?)''', x)
    dbase1.commit()


def read_produtos():
    c1 = dbase1.cursor()
    c1.execute('''SELECT COD, PRODUTO from produtos''')
    data = c1.fetchall()
    dbase1.commit()
    return data


def show_produtos_info(x):
    c1 = dbase1.cursor()
    c1.execute('''SELECT PRODUTO, COD, CATEGORIA, MARCA, ESTOMIN, ESTOMAX, PRODOBS, PRECO, VENDATAC, VENDVAR, QUANT, INSUMO from produtos where (COD, PRODUTO) = (?, ?)''', x)
    data = c1.fetchone()
    return data


def pick_produtos_info(x):
    c1 = dbase1.cursor()
    c1.execute('''SELECT PRODUTO, COD, CATEGORIA, MARCA, ESTOMIN, ESTOMAX, PRODOBS, PRECO, VENDATAC, VENDVAR, QUANT, INSUMO from produtos where (COD, PRODUTO) = (?, ?)''', x)
    data = c1.fetchone()
    return data


def att_produtos(PRODUTO, COD, CATEGORIA, MARCA, ESTOMIN, ESTOMAX, PRODOBS, PRECO, VENDATAC, VENDAVAR, INSUMO, x):
    c1 = dbase1.cursor()
    d1 = (PRODUTO, COD, CATEGORIA, MARCA, ESTOMIN, ESTOMAX, PRODOBS, PRECO, VENDATAC, VENDAVAR, INSUMO, )
    d2 = d1 + x
    c1.execute('''UPDATE produtos set PRODUTO = ?, COD = ?, CATEGORIA = ?, MARCA = ?, ESTOMIN = ?, ESTOMAX = ?, PRODOBS = ?, PRECO = ?, VENDATAC = ?, VENDVAR = ?, INSUMO = ? where (COD, PRODUTO) = (?, ?)''', d2)
    dbase1.commit()


def prod_geracode():
    c1 = dbase1.cursor()
    c1.execute('''SELECT MAX(COD) FROM produtos''')
    teste = c1.fetchone()

    if teste[0] == None:
        return 0
    else:
        return teste[0] + 1


def checa_prodcode():
    c1 = dbase1.cursor()
    c1.execute('''SELECT COD from produtos''')
    data = c1.fetchall()
    dbase1.commit()
    return data


def checa_prod():
    c1 = dbase1.cursor()
    c1.execute('''SELECT PRODUTO, INSUMO from produtos''')
    data = c1.fetchall()
    dbase1.commit()
    return data


#########################################################################TABELA DOS PRODUTOS/COMPRAS###########################################################################################################
def read_compras():
    c1 = dbase1.cursor()
    c1.execute('''SELECT PRODUTO, QUANT from produtos''')
    data = c1.fetchall()
    dbase1.commit()
    return data


def altera_quant(QUANT, x):
    c1 = dbase1.cursor()
    d1 = (QUANT, x)
    c1.execute('''UPDATE produtos set QUANT = ? where PRODUTO = ?''', d1)
    dbase1.commit()


def antiga_quant(x):
    c1 = dbase1.cursor()
    c1.execute('''SELECT QUANT from produtos where PRODUTO = ?''', (x,))
    data = c1.fetchone()
    return data    


def antigos_precos(x):
    c1 = dbase1.cursor()
    c1.execute('''SELECT VENDATAC, VENDVAR from produtos where PRODUTO = ?''', (x,))
    data = c1.fetchone()
    return data


def antigo_custo(x):
    c1 = dbase1.cursor()
    c1.execute('''SELECT PRECO from produtos where PRODUTO = ?''', (x,))
    data = c1.fetchone()
    return data


def altera_custo(CUSTO, x):
    c1 = dbase1.cursor()
    d1 = (CUSTO, x)
    c1.execute('''UPDATE produtos set PRECO = ? where PRODUTO = ?''', d1)
    dbase1.commit()

def altera_preco(PRECO1, PRECO2, x):
    c1 = dbase1.cursor()
    d1 = (PRECO1, PRECO2, x)
    c1.execute('''UPDATE produtos set VENDATAC = ?, VENDVAR = ? where PRODUTO = ?''', d1)
    dbase1.commit()


def show_all_quant():
    c1 = dbase1.cursor()
    c1.execute('''SELECT PRODUTO, QUANT, ESTOMIN, ESTOMAX from produtos''')
    data = c1.fetchall()
    dbase1.commit()
    return data


##################################################################################TABELA DAS VENDAS##################################################################################################
def add_venda(CLIENTE, PRODUTO, QUANT, VALOR, DESCONTO, FRETE, TOTAL, PAGAMENTO, NPARCELAS, VALPAR, VENCIMENTO):
    c1.execute('''INSERT into vendas (CLIENTE, PRODUTO, QUANT, VALOR, DESCONTO, FRETE, TOTAL, PAGAMENTO, NPARCELAS, VALPAR, VENCIMENTO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (CLIENTE, PRODUTO, QUANT, VALOR, DESCONTO, FRETE, TOTAL, PAGAMENTO, NPARCELAS, VALPAR, VENCIMENTO))
    dbase1.commit()


def read_venda():
    c1 = dbase1.cursor()
    c1.execute('''SELECT CLIENTE, PRODUTO, VENCIMENTO from vendas''')
    data = c1.fetchall()
    dbase1.commit()
    return data


def show_venda_info(x):
    c1 = dbase1.cursor()
    c1.execute('''SELECT CLIENTE, PRODUTO, QUANT, VALOR, DESCONTO, FRETE, TOTAL, PAGAMENTO, NPARCELAS, VALPAR, VENCIMENTO from vendas where (CLIENTE, PRODUTO, VENCIMENTO) = (?, ?, ?)''', x)
    data = c1.fetchone()
    return data


def rmv_venda(x):
    c1.execute('''delete from vendas where (CLIENTE, PRODUTO, VENCIMENTO) = (?, ?, ?)''', x)
    dbase1.commit()


def pick_venda_info(x):
    c1 = dbase1.cursor()
    c1.execute('''SELECT CLIENTE, PRODUTO, QUANT, VALOR, DESCONTO, FRETE, PAGAMENTO, NPARCELAS, VALPAR, VENCIMENTO from vendas where (CLIENTE, PRODUTO, VENCIMENTO) = (?, ?, ?)''', x)
    data = c1.fetchone()
    return data


def pega_valor(x):
    c1 = dbase1.cursor()
    c1.execute('''SELECT TOTAL from vendas where (CLIENTE, PRODUTO, VENCIMENTO) = (?, ?, ?)''', x)
    data = c1.fetchone()
    return data


def att_venda(CLIENTE, PRODUTO, QUANT, VALOR, DESCONTO, FRETE, TOTAL, PAGAMENTO, NPARCELAS, VALPAR, VENCIMENTO, x):
    c1 = dbase1.cursor()
    d1 = (CLIENTE, PRODUTO, QUANT, VALOR, DESCONTO, FRETE, TOTAL, PAGAMENTO, NPARCELAS, VALPAR, VENCIMENTO, )
    d2 = d1 + x
    c1.execute('''UPDATE vendas set CLIENTE = ?, PRODUTO = ?, QUANT = ?, VALOR = ?, DESCONTO = ?, FRETE = ?, TOTAL = ?, PAGAMENTO = ?, NPARCELAS = ?, VALPAR = ?, VENCIMENTO = ? where (CLIENTE, PRODUTO, VENCIMENTO) = (?, ?, ?)''', d2)
    dbase1.commit()


##################################################################################TABELA DAS ATIVIDADES##################################################################################################

def add_ativ(TEXTO):
    c1.execute('''INSERT into registro (ATIVIDADE) VALUES (?)''', (TEXTO,))
    dbase1.commit()


def show_ativ():
    c1 = dbase1.cursor()
    c1.execute('''SELECT ATIVIDADE from registro''')
    data = c1.fetchall()
    dbase1.commit()
    return data


def limpa_registro():
    c1 = dbase1.cursor()
    c1.execute('''delete from registro''')
    dbase1.commit()    


##################################################################################TABELA DO ORÇAMENTO##################################################################################################
def registra_venda(VALOR, DIA):
    c1 = dbase1.cursor()
    c1.execute('''INSERT into regvendas (VALOR, DIA) VALUES (?, ?)''', (VALOR, DIA))
    dbase1.commit()


def registra_compra(VALOR, DIA):
    c1 = dbase1.cursor()
    c1.execute('''INSERT into regcompras (VALOR, DIA) VALUES (?, ?)''', (VALOR, DIA))
    dbase1.commit()


def pick_vendas():
    c1 = dbase1.cursor()
    c1.execute('''SELECT VALOR, DIA from regvendas''')
    data = c1.fetchall()
    dbase1.commit()
    return data


def pick_compras():
    c1 = dbase1.cursor()
    c1.execute('''SELECT VALOR, DIA from regcompras''')
    data = c1.fetchall()
    dbase1.commit()
    return data


###########################################################################TABELA DO LOGIN#############################################################################################################
def add_usu(LOJA, USUARIO, SENHA, CARGO):
    c1.execute('''INSERT into login (NOMELOJA, NOMEUSUARIO, SENHA, CARGO) VALUES (?, ?, ?, ?)''', (LOJA, USUARIO, SENHA, CARGO))
    dbase1.commit()

def rmv_usu(USUARIO):
    c1.execute('''delete from login where NOMEUSUARIO = ?''', USUARIO)
    dbase1.commit()

def checa_usuario():
    c1 = dbase1.cursor()
    c1.execute('''SELECT NOMEUSUARIO from login''')
    data = c1.fetchall()
    dbase1.commit()
    return data

def pega_info(USUARIO):
    c1 = dbase1.cursor()
    c1.execute('''SELECT NOMELOJA, SENHA, CARGO from login where NOMEUSUARIO = ?''', USUARIO)
    data = c1.fetchall()
    dbase1.commit()
    return data


###########################################################################TELA HOME#############################################################################################################

def conta_produtos():
    c1 = dbase1.cursor()
    c1.execute('''SELECT count(*) from produtos''')
    data = c1.fetchone()
    dbase1.commit()
    return data[0]


def conta_repo():
    c1 = dbase1.cursor()
    c1.execute('''SELECT count(*) from produtos where QUANT < ESTOMIN''')
    data = c1.fetchone()
    dbase1.commit()
    return data[0]


def compras_dia(d):
    c1 = dbase1.cursor()
    c1.execute('''SELECT count(*) from regcompras where DIA = ?''', (d, ))
    data = c1.fetchone()
    dbase1.commit()
    return data[0]


def compras_mes(d):
    c1 = dbase1.cursor()
    c1.execute('''SELECT * from regcompras''')
    data = c1.fetchall()
    dbase1.commit()

    cont = 0
    for i in data:
        if i[1][3:5] == d[3:5]:
            cont += 1
    return cont


def vendas_dia(d):
    c1 = dbase1.cursor()
    c1.execute('''SELECT count(*) from regvendas where DIA = ?''', (d, ))
    data = c1.fetchone()
    dbase1.commit()
    return data[0]


def vendas_mes(d):
    c1 = dbase1.cursor()
    c1.execute('''SELECT * from regvendas''')
    data = c1.fetchall()
    dbase1.commit()

    cont = 0
    for i in data:
        if i[1][3:5] == d[3:5]:
            cont += 1
    return cont


def gastos_mes(d):
    c1 = dbase1.cursor()
    c1.execute('''SELECT * from regcompras''')
    data = c1.fetchall()
    dbase1.commit()

    soma = 0
    for i in data:
        if i[1][3:5] == d[3:5]:
            soma += i[0]
    return soma


def areceber():
    c1 = dbase1.cursor()
    c1.execute('''SELECT SUM(TOTAL) from vendas''')
    data = c1.fetchone()
    dbase1.commit()
    return data[0]
