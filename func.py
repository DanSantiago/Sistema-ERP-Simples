import PySimpleGUI as sg
from datetime import datetime
import bancodados as bd
import imagens as im


#=============== função para converter a saída da função weekday() para o nome do dia da semana ===============#
def converteDia(resultado):
    if resultado == 0:
        return "Segunda-Feira"
    elif resultado == 1:
        return "Terça-Feira"
    elif resultado == 2:
        return "Quarta-Feira"
    elif resultado == 3:
        return "Quinta-Feira"
    elif resultado == 4:
        return "Sexta-Feira"
    elif resultado == 5:
        return "Sábado"
    elif resultado == 6:
        return "Domingo"


#=============== função para limpar os campos da tela de login ===============#
def limpaLogin(t):
    t['nomeloja'].update('')
    t['nomeusu'].update('')
    t['D'].update(False)
    t['F'].update(False)
    t['senha'].update('')
    t['mastersenha'].update('')


#=============== função para desmarcar as checkboxs da tela de login ===============#
def falseBox(t):
    t['D'].update(False)
    t['F'].update(False)


#=============== função para buscar informações no registro de atividades ===============$
def attREG():
    REG = bd.show_ativ()    
    regzin = []
    for i in REG:
      if len(i[0]) > 70:
          x = i[0].split('\n')
          for j in range(0, len(x)):
              regzin.append(x[j])
          regzin.append('')
      else:
          regzin.append(i[0])
          regzin.append('')

    return regzin

#=============== função para buscar informações sobre o estoque dos produtos e avisar na tela em caso de super/sub estoque ideal ===============#
def attProd():
  prod = bd.show_all_quant()
  for i in prod:
    if i[1] < i[2]:
      print(f'O produto {i[0]} está com estoque baixo e é necessário reposição.\nEstoque mínimo: {i[2]}, estoque atual: {i[1]}.\n')
    if i[1] > i[3]:
      print(f'O produto {i[0]} está com super estoque.\nEstoque máximo: {i[3]}, estoque atual: {i[1]}.\n')   


#=============== função que calcula a hora ===============#
def calcHora():
  h = datetime.now().hour
  m = datetime.now().minute
  if m <= 9:
      hr = f'{h}:'+'0'+f'{m}'
  else:
      hr = f'{h}:{m}'

  return hr


#=============== função para exibir a aba clientes ===============#
def mostraClie(j):
    j['LayHome'].update(visible=False)
    j['LayVend'].update(visible=False)
    j['LayComp'].update(visible=False)
    j['LayFina'].update(visible=False)
    j['LayConf'].update(visible=False)
    j['LayProd'].update(visible=False)            
    j['LayClie'].update(visible=True)


#=============== função para exibir a aba produtos ===============#
def mostraProd(j):
    j['LayHome'].update(visible=False)
    j['LayVend'].update(visible=False)
    j['LayComp'].update(visible=False)
    j['LayFina'].update(visible=False)
    j['LayConf'].update(visible=False)
    j['LayProd'].update(visible=True)            
    j['LayClie'].update(visible=False)


#=============== função para exibir a aba compras ===============#
def mostraComp(j):
    j['LayHome'].update(visible=False)
    j['LayVend'].update(visible=False)
    j['LayComp'].update(visible=True)
    j['LayFina'].update(visible=False)
    j['LayConf'].update(visible=False)
    j['LayProd'].update(visible=False)            
    j['LayClie'].update(visible=False)


#=============== função para exibir a aba vendas ===============#
def mostraVend(j):
    j['LayHome'].update(visible=False)
    j['LayVend'].update(visible=True)
    j['LayComp'].update(visible=False)
    j['LayFina'].update(visible=False)
    j['LayConf'].update(visible=False)
    j['LayProd'].update(visible=False)            
    j['LayClie'].update(visible=False)


#=============== função para exibir a aba home ===============#
def mostraHome(j):
    j['LayHome'].update(visible=True)
    j['LayVend'].update(visible=False)
    j['LayComp'].update(visible=False)
    j['LayFina'].update(visible=False)
    j['LayConf'].update(visible=False)
    j['LayProd'].update(visible=False)            
    j['LayClie'].update(visible=False)


#=============== função para exibir a aba financeiro ===============#
def mostraFinan(j):
    j['LayHome'].update(visible=False)
    j['LayVend'].update(visible=False)
    j['LayComp'].update(visible=False)
    j['LayFina'].update(visible=True)
    j['LayConf'].update(visible=False)
    j['LayProd'].update(visible=False)            
    j['LayClie'].update(visible=False)


#=============== função para exibir a aba configurações ===============#
def mostraConf(j):
    j['LayHome'].update(visible=False)
    j['LayVend'].update(visible=False)
    j['LayComp'].update(visible=False)
    j['LayFina'].update(visible=False)
    j['LayConf'].update(visible=True)
    j['LayProd'].update(visible=False)            
    j['LayClie'].update(visible=False)


#=============== função para carregar as informações do board ===============#
def attBoard(j, d):
    prod_tot = str(bd.conta_produtos())
    prod_repo = str(bd.conta_repo())
    compdia = str(bd.compras_dia(d))
    compmes = str(bd.compras_mes(d))
    vendia = str(bd.vendas_dia(d))
    vendmes = str(bd.vendas_mes(d))
    gastos = str(bd.gastos_mes(d))
    receber = str(bd.areceber())

    j['qtdprod'].update(prod_tot)
    j['repoprod'].update(prod_repo)
    j['vendia'].update(vendia)
    j['vendmes'].update(vendmes)
    j['compdia'].update(compdia)
    j['compmes'].update(compmes)
    j['gastosmes'].update('R$ ' + gastos)
    j['recmes'].update('R$ ' + receber)    


#=============== função para desmarcar as checkboxs da tela de login ===============#
def resposta(a):
    if a == 1:
        sg.popup('Há 5 campos, 2 caixas de marcação e 3 botões para preenchimento/uso nessa tela.\n\nO campo "Nome da loja", "Senha mestre" e "Cargo" só precisam ser preenchidos no cadastro de usuários. Todos os campos precisam ser preenchidos nessa etapa e após isso basta clicar no botão de adicionar.\n\nPara fazer login basta preencher o nome do usuário e a senha e após isso clicar no botão de login.\n\nPara remover um usuário basta preencher o nome do usuário e inserir também a senha mestre e após isso clicar no botão de remoção.\n\nEm caso de preenchimento incorreto em alguma etapa, avisos de erros podem aparecer.\n\nPor todo o sistema, se houver dúvidas sobre determinado botão, basta passar o mouse por cima do local e dicas de uso aparecerão.\n\n', font=('Arial Black', 10), title='Instruções')
    elif a == 2:
        sg.popup('Usuário só pode ter um cargo. Marque somente uma das caixas.', font=('Arial Black', 15), title='Resposta')
    elif a == 3:
        sg.popup('Usuário precisa ter um cargo. Marque uma das caixas.', font=('Arial Black', 15), title='Resposta')
    elif a == 4:
        sg.popup('Usuário já cadastrado no banco de dados. Por favor, insira um novo usuário ou faça o login com o usuário em questão.', font=('Arial Black', 15), title='Resposta')
    elif a == 5:
        sg.popup('Cadastro efetuado com sucesso. Por favor, faça seu login ou continue cadastrando novos usuários.', font=('Arial Black', 15), title='Resposta')
    elif a == 6:
        sg.popup('A senha mestre está incorreta. Por favor, insira a senha corretamente.', font=('Arial Black', 15), title='Resposta')
    elif a == 7:
        sg.popup('Usuário removido com sucesso.', font=('Arial Black', 15), title='Resposta')
    elif a == 8:
        sg.popup('Usuário não cadastrado no banco de dados. Por favor, repita o processo', font=('Arial Black', 15), title='Resposta')
    elif a == 9:
        sg.popup('O código já foi cadastrado, por favor insira um código diferente.', font=('Arial Black', 15), title='Resposta')
    elif a == 10:
        sg.popup('Você não tem permissão para realizar esse comando. Faça login com um usuário especial.', font=('Arial Black', 15), title='Resposta')
    elif a == 11:
        sg.popup('Produto é um insumo e não pode ser vendido.', font=('Arial Black', 15), title='Resposta')
    elif a == 12:
        sg.popup('Produto não está cadastrado no sistema.', font=('Arial Black', 15), title='Resposta')
    elif a == 13:
        sg.popup('Cliente não está cadastrado no sistema.', font=('Arial Black', 15), title='Resposta')
    elif a == 14:
        sg.popup('Você não tem permissão para acessar esse módulo. Faça login com um usuário especial.', font=('Arial Black', 15), title='Resposta')
    elif a == 15:
        sg.popup('Valor inserido na receita/despesa esperada não é um numero. Insira um valor válido.', font=('Arial Black', 15), title='Resposta')
    elif a == 16:
        sg.popup('Insira um período válido no formato: dd/mm/aaaa e insira também o valor esperado das receitas e despesas.', font=('Arial Black', 15), title='Resposta')
    elif a == 17:
        sg.popup('A senha do usuário está incorreta. Por favor, repita o processo.', font=('Arial Black', 15), title='Resposta')


#=============== função para definir a senha mestre e a chave da criptografia ===============#
def chaves():
    ch = 'The witcher 3'
    sn = 'gerald'

    return ch, sn


#=============== função para limpar os campos da aba clientes ===============#
def limpaClie(j, N, C, auto):
    j['nome'].update('')
    j['cod'].update(auto)
    j['rg'].update('')
    j['cpf'].update('')
    j['cel'].update('')
    j['tel'].update('')
    j['email'].update('')
    j['Clieobs'].update('')
    j['cep'].update('')
    j['end'].update('')
    j['num'].update('')
    j['bairro'].update('')
    j['cidade'].update('')
    j['estado'].update('')
    j['ClieBOX'].update(N)
    j['VCBOX'].update(C)     


#=============== função para ler os campos da aba clientes ===============#
def pickClie(v):
    NOME = v['nome'].title()
    COD = int(v['cod'])
    RG = v['rg']
    CPF = v['cpf']
    CEL = v['cel']
    TEL = v['tel']
    EMAIL = v['email']
    OBS = v['Clieobs']
    CEP = v['cep']
    END = v['end']
    NUM = v['num']
    BAI = v['bairro']
    CID = v['cidade']
    EST = v['estado']

    return NOME, COD, RG, CPF, CEL, TEL, EMAIL, OBS, CEP ,END, NUM, BAI, CID, EST


#=============== função para atualizar as litsbox do programa ===============#
def attList():
    N = bd.read_clientes()
    P = bd.read_produtos()
    VP = bd.read_produtos()
    VC = bd.read_clientes()
    CP = bd.read_compras()
    VND = bd.read_venda()

    return N, P, VP, VC, CP, VND    


#=============== função para limpar os campos da aba produtos ===============#
def limpaProd(j, P, VP, CP, auto):
    j['produto'].update('')
    j['pcod'].update(auto)
    j['cate'].update('')
    j['marca'].update('')
    j['min'].update('')
    j['max'].update('')
    j['Prodobs'].update('')
    j['custo'].update('')
    j['atac'].update('')
    j['var'].update('')
    j['Insumo'].update(False)
    j['ProdBOX'].update(P)
    j['CPBOX'].update(CP)
    j['VPBOX'].update(VP)        

    
#=============== função para ler os campos da aba produtos ===============#
def pickProd(v):
    PROD = v['produto'].capitalize()
    PCOD = int(v['pcod'])
    CAT = v['cate'].capitalize()
    MARCA = v['marca']
    EMIN = v['min']
    EMAX = v['max']
    PRODOBS = v['Prodobs']
    CUSTO = v['custo'].replace(',', '.')
    VATA = v['atac'].replace(',', '.')
    VVAR = v['var'].replace(',', '.')    

    return PROD, PCOD, CAT, MARCA, EMIN, EMAX, PRODOBS, CUSTO, VATA, VVAR

   
#=============== função para limpar os campos da aba vendas ===============#
def pickVend(v):
    PRODUTO = v['prodv']
    CLIENTE = v['cliv']                               
    QUANTIDADE = v['qtd']
    VALOR = v['val'].replace(',', '.')
    DESCONTO = v['des'].replace(',', '.')
    FRETE = v['frete'].replace(',', '.')
    PAGAMENTO = v['pag']
    PARCELAMENTO = v['parc']
    VALORPARC = v['valpar'].replace(',', '.')
    VENCIMENTO = v['venc']

    return PRODUTO, CLIENTE, QUANTIDADE, VALOR, DESCONTO, FRETE, PAGAMENTO, PARCELAMENTO, VALORPARC, VENCIMENTO

    
#=============== função para ler os campos da aba vendas ===============#
def limpaVend(j, VND):
    j['cliv'].update('')
    j['prodv'].update('')
    j['qtd'].update('')
    j['val'].update('')
    j['des'].update('')
    j['frete'].update('')
    j['pag'].update('')
    j['parc'].update('1')
    j['valpar'].update('N/A')
    j['venc'].update('')
    j['VendBOX'].update(VND)    


#=============== função para fazer os cálculos da aba financeiro ===============#
def calculaFinan(j, v):
    inicio = v['perini']
    fim = v['perfim']

    try:
        receita_esperada = float(v['esperecei'].replace(',', '.'))
        despesa_esperada = float(v['espedesp'].replace(',', '.'))
        pega_vendas = bd.pick_vendas()
        pega_compras = bd.pick_compras()

        receitas = 0.0
        despesas = 0.0
        
        for i in range (0, len(pega_vendas)):
            if pega_vendas[i][1] >= inicio and pega_vendas[i][1] <= fim:
                receitas += pega_vendas[i][0]

        for i in range (0, len(pega_compras)):
            if pega_compras[i][1] >= inicio and pega_compras[i][1] <= fim:
                despesas += pega_compras[i][0]

        j['Receitas'].update(receitas)
        j['Despesas'].update(despesas)

        obtido_vendas = (receitas/receita_esperada)*100
        obtido_compras = (despesas/despesa_esperada)*100

        j['pc1'].update(str(obtido_vendas) + '%')
        j['pc2'].update(str(obtido_compras) + '%')

        j['recei'].update(obtido_vendas)
        j['despe'].update(obtido_compras)

    except ValueError:
        resposta(15)


#=============== função para limpar os campos da aba compras ===============#
def limpaComp(j):
    j['quanti'].update('')
    j['prodc'].update('')
    j['Compqtd'].update('')
    j['Compval'].update('')


#=============== função para calcular os reajustes ao fazer uma compra ===============#
def reajusta(v, dia):
    prod = v['prodc']
    qtd = v['Compqtd']
    custo_total = v['Compval']

    old_qtd = bd.antiga_quant(prod)
    old_price = bd.antigos_precos(prod)
    old_custo = bd.antigo_custo(prod)
    atac = float(old_price[0])
    var = float(old_price[1])   
    custo = round(float(custo_total.replace(',', '.'))/int(qtd), 2)
    new_qtd = int(qtd) + int(old_qtd[0])
    margem = round(custo/float(old_custo[0]), 2)

    if atac != 0.0 and var != 0.0: 
        new_atac = round(atac*margem, 2)
        new_var = round(var*margem, 2)
    else:
        new_atac = round(custo*margem, 2)
        new_var = round(custo*margem, 2)
    
    bd.altera_quant(new_qtd, prod)
    bd.altera_custo(custo, prod)
    bd.altera_preco(new_atac, new_var, prod)
    atividade = f'Item {prod} atualizado:\ncompra de {qtd} unidade(s) no valor de R$ {custo_total},\nresultando em um custo unitário de R$ {custo} no dia {dia}.\nValores atualizados:\nDe R$ {old_price[0]} para atacado e R$ {old_price[1]} para varejo\npara R$ {new_atac} para atacado e R$ {new_var} para varejo.'   
    bd.add_ativ(atividade)
    aux = (float(custo_total.replace(',', '.')))
    bd.registra_compra(aux, dia)

