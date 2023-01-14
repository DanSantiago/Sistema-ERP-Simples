import PySimpleGUI as sg
from datetime import datetime
import bancodados as bd
import imagens as im

#=============== definições de fonte, tamanho e tema dos layouts ===============#
sg.theme('SystemDefaultForReal')
fonte = ("Arial Black", 23)
ft_m = ('Arial Black', 18)
ft = ('Arial Black', 15)
finput = ('Arial Black', 10)
sz = (31, 1)
sz_inp = (38, 1)

#=============== criação do layout da tela de login ===============#
def loginLayout():
  login = [
      [sg.Text('Nome da loja:        ', font=('Arial Black', 15)), sg.Input(key='nomeloja', size=(38, 1), font=('Arial Black', 10), enable_events = True, tooltip = 'Esse espaço só precisa ser preenchido em caso de cadastro de usuários (tamanho máximo de 15 letras)')],
      [sg.Text('Nome do usuário:  ', font=('Arial Black', 15)), sg.Input(key='nomeusu', size=(38, 1), font=('Arial Black', 10), enable_events = True, tooltip = 'Tamanho máximo de 15 letras')],
      [sg.Text('Senha:                   ', font=('Arial Black', 15)), sg.Input(key='senha', size=(38, 1), font=('Arial Black', 10), password_char='*', tooltip = 'Senha de login do usuário')],
      [sg.Text('Senha mestre:       ', font=('Arial Black', 15)), sg.Input(key='mastersenha', size=(38, 1), font=('Arial Black', 10), password_char='*', tooltip = 'Esse espaço só precisa ser preenchido em caso de remoção ou cadastro de usuários')],
      [sg.Text('Cargo:                   ', font=('Arial Black', 15)), sg.Checkbox('Dono             ', font=('Arial Black', 15), default=False, key='D'), sg.Checkbox('Funcionário', font=('Arial Black', 15), default=False, key='F')],
      [sg.Button('', image_data = im.Acce, key = 'ENTRAR', border_width=0, bind_return_key=True, tooltip = 'Botão para fazer login'), sg.Button('', image_data = im.Addusu, key = 'ADDUSU', border_width=0, tooltip = 'Botão para cadastrar um usuário'), sg.Button('', image_data = im.Removeusu, key = 'REMUSU', border_width=0, tooltip = 'Botão para remover um usuário')],
      [sg.Text('')],
      [sg.Push(), sg.Button('', image_data = im.manu, key = 'MANU', border_width=0, bind_return_key=True, tooltip = 'Instruções de uso.')]
  ]

  return login

#=============== criação do layout da barra superior do programa ===============#
def supLayout(lj, dt, hr, usu):
  sup = [
      [sg.Button('', image_data = im.home, key = 'HOME', border_width=0), sg.Text(lj.title(), font=fonte, size=(17,1)), sg.Text(dt, font=fonte, size=(17,2)), sg.Text(hr + 'h', font=fonte, key='horario', size=(17,1)), sg.Text('Bem-vindo,\n'+ usu.title(), font=fonte, size=(17,2)), sg.Button('', image_data = im.sair, key = 'SAIR', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)]
  ]

  guias = [
      [sg.Button('', image_data = im.clientes, key = 'CLIENTES', border_width=0), sg.Button('', image_data = im.produtos, key = 'PRODUTOS', border_width=0), sg.Button('', image_data = im.compras, key = 'COMPRAS', border_width=0), sg.Button('', image_data = im.vendas, key = 'VENDAS', border_width=0), sg.Button('', image_data = im.financeiro, key = 'FINANCEIRO', border_width=0), sg.Button('', image_data = im.config, key = 'CONFIG', border_width=0)]

  ]
  return sup, guias


#=============== criação do layout da tela inicial ===============#
def homeLayout():  
  #define um size a ser usado nos boards
  sz = (35, 1)

  supleft = [
      [sg.Text('Produtos cadastrados:' , font=('Arial Black', 30), size = sz)],
      [sg.Text('Teste' , font=('Arial Black', 30), size = sz, key = 'qtdprod')],
      [sg.Text('Produtos que precisam de reposição:' , font=('Arial Black', 30), size = sz)],
      [sg.Text('Teste' , font=('Arial Black', 30), size = sz, key = 'repoprod')],
  ]

  supright = [
      [sg.Text('Vendas do dia:' , font=('Arial Black', 30), size = sz)],
      [sg.Text('Teste' , font=('Arial Black', 30), size = sz, key = 'vendia')],
      [sg.Text('Vendas do mês:' , font=('Arial Black', 30), size = sz)],
      [sg.Text('Teste' , font=('Arial Black', 30), size = sz, key = 'vendmes')],
  ]

  infleft = [
      [sg.Text('Compras do dia:' , font=('Arial Black', 30), size = sz)],
      [sg.Text('Teste' , font=('Arial Black', 30), size = sz, key = 'compdia')],
      [sg.Text('Compras do mês:' , font=('Arial Black', 30), size = sz)],
      [sg.Text('Teste' , font=('Arial Black', 30), size = sz, key = 'compmes')],
  ]

  infright = [
      [sg.Text('Gastos do mês:' , font=('Arial Black', 30), size = sz)],
      [sg.Text('Teste' , font=('Arial Black', 30), size = sz, key = 'gastosmes')],
      [sg.Text('Valores a receber:' , font=('Arial Black', 30), size = sz)],
      [sg.Text('Teste' , font=('Arial Black', 30), size = sz, key = 'recmes')],
  ]
 
  home = [
      [sg.Text('')],
      [sg.Text('Boards', font = ('Arial Black', 40))],
      [sg.Text('')],
      [sg.Text('')],
      [sg.HorizontalSeparator()],
      [sg.Column(supleft, element_justification='center'), sg.VerticalSeparator(), sg.Column(supright, element_justification='center')],
      [sg.HorizontalSeparator()],
      [sg.Column(infleft), sg.VerticalSeparator(), sg.Column(infright)],
      [sg.HorizontalSeparator()]
  ]

  return home


#=============== criação do layout da tela de clientes ===============#
def clieLayout(N):
  autocode = bd.clie_geracode()
  
  clie1 = [
      [sg.Text('')],
      [sg.Text('')],
      [sg.Text('')],
      [sg.Text('Ficha cadastral do cliente', font=fonte, size=(44,1))],
      [sg.HorizontalSeparator()],
      [sg.Text('Nome', font=ft, size=sz), sg.Text('Código', font=ft, size=sz)], 
      [sg.Input(key='nome', size=sz_inp, font=finput), sg.Text('                    '), sg.Input(key='cod', size=sz_inp, font=finput, default_text=autocode)], 
      [sg.Text('RG', font=ft, size=sz), sg.Text('CPF', font=ft)],
      [sg.Input(key='rg', size=sz_inp, font=finput), sg.Text('                    '), sg.Input(key='cpf', size=sz_inp, font=finput)],
      [sg.Text('Celular', font=ft, size=sz), sg.Text('Telefone', font=ft, size=sz), sg.Text('Email', font=ft, size=sz)],
      [sg.Input(key='cel', size=sz_inp, font=finput), sg.Text('                    '), sg.Input(key='tel', size=sz_inp, font=finput), sg.Text('                    '), sg.Input(key='email', size=sz_inp, font=finput)],
      [sg.Text('Observação', font=ft, size=sz)],
      [sg.Input(key='Clieobs', size=(138, 1), font=finput)],
      [sg.Text('                    '), sg.Text('                    '), sg.Text('                    '), sg.Text('                    ')],
      [sg.Text('Endereço', font=ft_m)],
      [sg.HorizontalSeparator()],
      [sg.Text('CEP', font=ft, size=sz), sg.Text('Endereço', font=ft, size=sz), sg.Text('Nº', font=ft, size=sz)],
      [sg.Input(key='cep', size=sz_inp, font=finput), sg.Text('                    '), sg.Input(key='end', size=sz_inp, font=finput), sg.Text('                    '), sg.Input(key='num', size=sz_inp, font=finput)],
      [sg.Text('Bairro', font=ft, size=sz), sg.Text('Cidade', font=ft, size=sz), sg.Text('Estado', font=ft, size=sz)],
      [sg.Input(key='bairro', size=sz_inp, font=finput), sg.Text('                    '),  sg.Input(key='cidade', size=sz_inp, font=finput), sg.Text('                    '), sg.Input(key='estado', size=sz_inp, font=finput)],
      [sg.Text('')],
      [sg.Text('')],
      [sg.Push(), sg.Button('', image_data = im.Clieadd, key='ClieADD', border_width=0, tooltip = 'Adicionar cliente'), sg.Push()]
  ]

  clie2 = [
      [sg.Text('Lista de clientes cadastrados', font=ft)],
      [sg.Text('Código | Cliente', font=ft)],
      [sg.Listbox(N, size=(80, 25), key='ClieBOX', font=finput)],
      [sg.Text('', font=('Arial Black', 14))],
      [sg.Push(), sg.Button('', image_data = im.Clieremove, key = 'ClieREMOVE', border_width=0, tooltip = 'Remover cliente'), sg.Button('', image_data = im.Clieedit, key = 'ClieEDIT', border_width=0, tooltip = 'Abrir modo de edição'), sg.Button('', image_data = im.Clieshow, key = 'ClieSHOW', border_width=0, tooltip = 'Mostrar informações'),sg.Push()],
      [sg.Push(), sg.Button('', image_data = im.Acce, key = 'ClieACCEDIT', border_width=0, tooltip = 'Fechar modo de edição') ,sg.Push()]
  ]

  clientes = [
      [sg.Column(clie1, element_justification = 'left'), sg.VerticalSeparator(), sg.Column(clie2, element_justification = 'center')]
  ]

  return clientes


#=============== criação do layout da tela de produtos ===============#
def prodLayout(P):  
  pcod = bd.prod_geracode()
  
  prod1 = [
      [sg.Text('')],
      [sg.Text('')],
      [sg.Text('')],
      [sg.Text('Cadastrar Produto', font=fonte, size=(44,1))],
      [sg.HorizontalSeparator()],
      [sg.Text('Produto', font=ft, size=sz), sg.Text('Código', font=ft, size=sz)], 
      [sg.Input(key='produto', size=sz_inp, font=finput), sg.Text('                    '), sg.Input(key='pcod', size=sz_inp, font=finput, default_text = pcod)], 
      [sg.Text('Categoria', font=ft, size=sz), sg.Text('Marca', font=ft)],
      [sg.Input(key='cate', size=sz_inp, font=finput), sg.Text('                    '), sg.Input(key='marca', size=sz_inp, font=finput)],
      [sg.Text('Estoque mínimo', font=ft, size=sz), sg.Text('Estoque máximo', font=ft, size=sz)],
      [sg.Input(key='min', size=sz_inp, font=finput), sg.Text('                    '), sg.Input(key='max', size=sz_inp, font=finput)],
      [sg.Text('Observação', font=ft, size=sz)],
      [sg.Input(key='Prodobs', size=(65, 1), font=finput), sg.Text('                   '), sg.Checkbox('Insumo', font=('Arial Black', 15), default=False, key='Insumo')],
      [sg.Text('                    '), sg.Text('                    '), sg.Text('                    '), sg.Text('                    ')],
      [sg.Text('Preço', font=ft_m)],
      [sg.HorizontalSeparator()],
      [sg.Text('Custo', font=ft), sg.Text('(Última compra)', font=('Arial Black', 10))],
      [sg.Input(key='custo', size=sz_inp, font=finput)],        
      [sg.Text('Venda Atacado', font=ft, size=sz), sg.Text('Venda Varejo', font=ft, size=sz)],
      [sg.Input(key='atac', size=sz_inp, font=finput), sg.Text('                    '), sg.Input(key='var', size=sz_inp, font=finput)],
      [sg.Text('')],
      [sg.Text('')],
      [sg.Push(), sg.Button('', image_data = im.Prodadd, key = 'ProdADD', border_width=0, tooltip = 'Adicionar produto'), sg.Push()]
  ]

  prod2 = [
      [sg.Text('Lista de produtos cadastrados', font=ft)],
      [sg.Text('Código | Produto', font=ft)],
      [sg.Listbox(P, size=(130, 25), key='ProdBOX', font=finput)],
      [sg.Text('', font=('Arial Black', 14))],
      [sg.Push(), sg.Button('', image_data = im.Prodremove, key = 'ProdREMOVE', border_width=0, tooltip = 'Remover produto'), sg.Button('', image_data = im.Prodedit, key = 'ProdEDIT', border_width=0, tooltip = 'Abrir modo de edição'), sg.Button('', image_data = im.Prodshow, key = 'ProdSHOW', border_width=0, tooltip = 'Mostrar informações') ,sg.Push()],
      [sg.Push(), sg.Button('', image_data = im.Acce, key = 'ProdACCEDIT', border_width=0, tooltip = 'Fechar modo de edição') ,sg.Push()]
  ]

  produtos = [
      [sg.Column(prod1, element_justification = 'left'), sg.VerticalSeparator(), sg.Column(prod2, element_justification = 'center')]
  ]

  return produtos


#=============== criação do layout da tela de compras ===============#
def compLayout(R, C):
  comp1 = [
      [sg.Text('')],
      [sg.Text('Compras', font=fonte, size=(44,1))],
      [sg.HorizontalSeparator()],
      [sg.Text('Produto', font=ft, size=sz)],
      [sg.Input(key='prodc', size=sz_inp, default_text = '', font=finput, enable_events=True), sg.Button('', image_data = im.VendPFind, key = 'CompPFind', border_width=0, tooltip = 'Selecionar produto')],        
      [sg.Text('Produtos cadastrados | Quantidade', font=ft, size=sz)],
      [sg.Listbox(C, size=(60, 4), key='CPBOX', font=finput)],
      [sg.Text('')],
      [sg.Text('Alterar quantidade do produto', font=ft, size=(24, 1)), sg.Button('', image_data = im.CompraQTD, key = 'CompPQTD', border_width=0, tooltip = 'Atualizar quantidade')],
      [sg.Input(key='quanti', size=sz_inp, font=finput)],
      [sg.Text('')],        
      [sg.Text('Quantidade', font=ft, size=sz)],
      [sg.Input(key='Compqtd', size=sz_inp, font=finput)],
      [sg.Text('Custo Total', font=ft, size=sz)],
      [sg.Input(key='Compval', size=sz_inp, font=finput)],
      [sg.Text(' ')],
      [sg.Text(' ')],
      [sg.Text('                                                      '),sg.Button('', image_data = im.Compadd, key = 'CompADD', border_width=0, tooltip = 'Adicionar compra')]
  ]

  comp3 = [
      [sg.Text('Registro de atividades', font=ft)],
      [sg.Listbox(R, size=(60, 30), key='RegBOX', font=finput)],
      [sg.Text('', font = ('Arial Black', 13))],
      [sg.Button('', image_data = im.RegLimp, key = 'RegLIMPE', border_width=0, tooltip = 'Limpar todo o registro')]
  ]

  comp2 = [
      [sg.Text('Controle de produtos                ', font=ft)],
      [sg.Multiline(size=(78, 36), font=finput, reroute_stdout=True, reroute_stderr=True, reroute_cprint=True, do_not_clear=False)],
      [sg.Text('', font=('Arial Black', 44))],           
  ]


  compras = [
      [sg.Column(comp1, element_justification = 'left', size = (618, 800)), sg.VerticalSeparator(), sg.Column(comp2, element_justification = 'center', size = (618, 800)), sg.VerticalSeparator(), sg.Column(comp3, element_justification = 'center', size = (618, 800))]
  ]

  return compras


#=============== criação do layout da tela de vendas ===============#
def vendLayout(C, P, V):
  vend1 = [
      [sg.Text('')],
      [sg.Text('Vendas', font=fonte, size=(44,1))],
      [sg.HorizontalSeparator()],
      [sg.Text('Cliente', font=ft, size=sz), sg.Text('         '), sg.Text('Produto', font=ft, size=sz)],
      [sg.Input(key='cliv', size=sz_inp, default_text = '', font=finput, enable_events=True), sg.Button('', image_data = im.VendCFind, key = 'ClieFIND', border_width=0, tooltip = 'Selecionar cliente'), sg.Push(), sg.Input(key='prodv', size=sz_inp, default_text = '', font=finput, enable_events=True), sg.Button('', image_data = im.VendPFind, key = 'VendPFind', border_width=0, tooltip = 'Selecionar produto')],        
      [sg.Text('Código | Clientes cadastrados', font=ft, size=sz), sg.Text('         '), sg.Text('Código | Produtos cadastrados', font=ft, size=sz)],
      [sg.Listbox(C, size=(45, 4), key='VCBOX', font=finput), sg.Text('              '), sg.Listbox(P, size=(45, 4), key='VPBOX', font=finput)],
      [sg.Text('Quantidade', font=ft, size=sz), sg.Text('         '), sg.Text('Valor', font=ft)],
      [sg.Input(key='qtd', size=sz_inp, font=finput), sg.Text('                                '), sg.Input(key='val', size=sz_inp, font=finput)],
      [sg.Text('Desconto', font=ft, size=sz), sg.Text('         '), sg.Text('Frete', font=ft, size=sz)],
      [sg.Input(key='des', size=sz_inp, font=finput), sg.Text('                                '), sg.Input(key='frete', size=sz_inp, font=finput)],
      [sg.Text('Forma de pagamento', font=ft, size=sz), sg.Text('         '), sg.Text('Parcelamento', font=ft, size=sz)],
      [sg.Combo(['Dinheiro', 'Débito', 'Crédito', 'PIX'], default_value='', s=(28,28), enable_events=True, readonly=True, k='pag', font=finput), sg.Text('                                                    '),sg.Combo(['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], default_value='1', s=(28,28), enable_events=True, readonly=True, k='parc', font=finput)],    
      [sg.Text('Valor das parcelas', font=ft, size=sz), sg.Text('         '),  sg.Text('Data de entrega', font=ft, size=sz)],
      [sg.Input(key='valpar', size=sz_inp, default_text = 'N/A', font=finput), sg.Text('                                '), sg.Input(key='venc', size=sz_inp, font=finput)],
      [sg.Text('')],
      [sg.Text('')],
      [sg.Push(), sg.Button('', image_data = im.Vendadd, key = 'VendADD', border_width=0, tooltip = 'Adicionar venda'), sg.Push()]
  ]

  vend2 = [
      [sg.Text('Lista de vendas realizadas', font=ft)],
      [sg.Text('Cliente | Produto | Data de entrega', font=ft)],
      [sg.Listbox(V, size=(130, 25), key='VendBOX', font=finput)],
      [sg.Text('', font=('Arial Black', 14))],        
      [sg.Push(), sg.Button('', image_data = im.Vendremove, key = 'VendREMOVE', border_width=0, tooltip = 'Remover venda'), sg.Button('', image_data = im.Vendedit, key = 'VendEDIT', border_width=0, tooltip = 'Abrir modo de edição'), sg.Button('', image_data = im.VendEntre, key = 'VendENTRE', border_width=0, tooltip = 'Finalizar venda'), sg.Button('', image_data = im.Vendshow, key = 'VendSHOW', border_width=0, tooltip = 'Mostrar informações'), sg.Push()],
      [sg.Push(), sg.Button('', image_data = im.Acce, key = 'VendACCEDIT', border_width=0, tooltip = 'Fechar modo de edição') ,sg.Push()]
  ]


  vendas = [
      [sg.Column(vend1, element_justification = 'left'), sg.VerticalSeparator(), sg.Column(vend2, element_justification = 'center')]
  ]
  
  return vendas


#=============== criação do layout da tela do financeiro ===============#
def finanLayout():
  fina_sup = [
      [sg.Text('')],
      [sg.Text('')],
      [sg.Text('                                                                                                                                                                                                              '), sg.Text('Período para análise', font=ft)],
      [sg.Text('                                                                                                                                                                                      '), sg.Text('De', font=ft, size=(3, 1)), sg.Input(key='perini', size=sz_inp, font=finput, tooltip = 'Formato da data dd/mm/aaaa')],                             
      [sg.Text('                                                                                                                                                                                      '), sg.Text('Até', font=ft, size=(3, 1)), sg.Input(key='perfim', size=sz_inp, font=finput, tooltip = 'Formato da data dd/mm/aaaa')],
      [sg.Text('                                                                                                                                                                                                                         '), sg.Button('', image_data = im.FinaFind, key = 'FinaFIND', border_width=0, tooltip = 'Buscar informações')]
  ]
  max_v = 100

  
  fina1 = [
      [sg.Text('')],
      [sg.Text('')],
      [sg.Text('Valor de receita esperado', font=ft, size=sz)],
      [sg.Input(key='esperecei', size=sz_inp, font=finput)],   
      [sg.Text('Total de Receitas', font=fonte)],
      [sg.Text('R$', font=fonte), sg.Text('', font=fonte, key='Receitas')],
      [sg.Text('')],
      [sg.Text('')],
      [sg.Text('Porcentagem atingida da meta', font=ft)],
      [sg.ProgressBar(max_value = 100, orientation = 'h', key = 'recei', size = (70, 20), bar_color = ('green', 'white')), sg.Text('', font=ft, key = 'pc1')],
  ]

  
  fina2 = [
      [sg.Text('')],
      [sg.Text('')],
      [sg.Text('Valor de despesa esperado', font=ft, size=sz)],                            [sg.Input(key='espedesp', size=sz_inp, font=finput)],         
      [sg.Text('Total de Despesas', font=fonte)],
      [sg.Text('R$', font=fonte), sg.Text('', font=fonte, key='Despesas')],
      [sg.Text('')],
      [sg.Text('')],
      [sg.Text('Porcentagem atingida da meta', font=ft)],
      [sg.ProgressBar(max_value = 100, orientation = 'h', key = 'despe', size = (70, 20), bar_color = ('red', 'white')), sg.Text('', font=ft, key = 'pc2')],
  ]
  
  financeiro = [
  [sg.Column(fina_sup)],
  [sg.HorizontalSeparator()],
  [sg.Column(fina1, element_justification = 'left', size = (940, 800)), sg.VerticalSeparator(), sg.Column(fina2, element_justification = 'left', size = (940, 800))]
  ]

  return financeiro


#=============== criação do layout da tela de configuração ===============#
def confLayout():
  config1 = [       
  ]

  config2 = [        
  ]
  
  config = [
  [sg.Column(config1, element_justification = 'left', size = (940, 800)), sg.VerticalSeparator(), sg.Column(config2, element_justification = 'left', size = (940, 800))]
  ]

  return config
