import PySimpleGUI as sg
import bancodados as bd
import imagens as im
import func as f
import layouts as lt
import cryptocode
from datetime import datetime

#========================================================================================================= função main ==================================================================================================================
def main():

    #pega a chave da criptografia e a senha mestre
    chave, senha = f.chaves()
    
    #comandos para ler os bancos de dados e mostrá-los nas list box
    NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
    registros = f.attREG()

    #pega informações da hora e do dia
    hora = f.calcHora()
    dia = datetime.strftime(datetime.now(), '%d/%m/%Y')
    data = dia + '\n' + f.converteDia(datetime.today().weekday())

    #puxa o layout e cria a tela de login
    login_layout = lt.loginLayout()           
    telalogin = sg.Window('Tela de Cadastro/Login', login_layout, size=(800, 350), element_justification='center').Finalize()

    ft = ('Arial Black', 15)
    
    while (True):
        usuarios = bd.checa_usuario()
        event, values = telalogin.read()
        
        if len(values['nomeloja']) > 15:
            telalogin['nomeloja'].update(values['nomeloja'][:-1])

        if len(values['nomeusu']) > 15:
            telalogin['nomeusu'].update(values['nomeusu'][:-1])
        
        if event == 'MANU':
            f.resposta(1)
            
        cont = 0 
        if event == 'ADDUSU':
            if values['D'] == True and values['F'] == True:
                f.resposta(2)
                f.falseBox(telalogin)
                
            elif values['D'] == False and values['F'] == False:
                f.resposta(3)
                f.falseBox(telalogin)
                
            else:   
                for i in range(0, len(usuarios)):
                    if values['nomeusu'] == usuarios[i][0]:
                        f.resposta(4)
                        telalogin['nomeloja'].update('')
                        f.falseBox(telalogin)
                        telalogin['mastersenha'].update('')
                        cont += 1
                
                if cont == 0:
                    usuario = values['nomeusu']
                    loja = values['nomeloja']
                    senha = values['senha']
                    master = values['mastersenha']
                    cont = 0
                    encry_sen = cryptocode.encrypt(senha, chave)
                    
                    if values['D'] == True:
                        cargo = 'D'
                        
                    elif values['F'] == True:
                        cargo = 'F'                   

                    if values['mastersenha'] == 'gerald':
                        bd.add_usu(loja, usuario, encry_sen, cargo)
                        f.limpaLogin(telalogin)
                        f.resposta(5)
                        
                    else:
                        f.resposta(6)
                        telalogin['mastersenha'].update('')
                
        elif event == 'REMUSU':
            usuario = values['nomeusu']
            cont = 0
            
            for i in range(0, len(usuarios)):
                if values['nomeusu'] == usuarios[i][0]:
                    cont += 1
                    if values['mastersenha'] == 'gerald':
                        bd.rmv_usu((usuario, ))
                        f.resposta(7)
                        f.limpaLogin(telalogin)
                        
                    else:
                        f.resposta(6)
                        telalogin['mastersenha'].update('')
                        f.falseBox(telalogin)
                        
            if cont == 0:
                f.resposta(8)
                cont = 0            
                f.limpaLogin(telalogin)
    
        elif event == sg.WIN_CLOSED:
            telalogin.close()
            break

        usuario = values['nomeusu']
        if event == 'ENTRAR':
            cont = 0
            
            for i in range(0, len(usuarios)):
                if usuario == usuarios[i][0]:
                    info = bd.pega_info((usuario, ))
                    cont +=1
                    
                    if values['senha'] == cryptocode.decrypt(info[0][1], chave):
                        senha = cryptocode.decrypt(info[0][1], chave)
                        loja = info[0][0]
                        cargo = info[0][2]                        
                        telalogin.close()

                        #=============== definição dos layouts das abas ===============#
                        layout_sup, layout_guias = lt.supLayout(loja, data, hora, usuario)                      
                        home_layout = lt.homeLayout()
                        clientes_layout = lt.clieLayout(NOMES)
                        produtos_layout = lt.prodLayout(PRODU)
                        compras_layout = lt.compLayout(registros, CP)
                        vendas_layout = lt.vendLayout(VC, VP, VENDA)
                        financeiro_layout = lt.finanLayout()
                        config_layout = lt.confLayout()

                        #=============== layout final ===============#
                        inilayout = [
                            [sg.Text('', font=('Arial Black', 10))],
                            [layout_sup],
                            [sg.Text('', font=('Arial Black', 10))],
                            [sg.HorizontalSeparator(color='black')],
                            [layout_guias],     
                            [sg.HorizontalSeparator(color='black')],        
                            [sg.Column(home_layout, key = 'LayHome', element_justification = 'center'), sg.Column(clientes_layout, visible = False, key = 'LayClie', element_justification = 'left'), sg.Column(produtos_layout, visible=False, key = 'LayProd', element_justification = 'left'), sg.Column(vendas_layout, visible = False, key = 'LayVend', element_justification = 'left'), sg.Column(compras_layout, visible = False, key = 'LayComp', element_justification = 'left'), sg.Column(financeiro_layout, visible = False, key = 'LayFina', element_justification = 'left'), sg.Column(config_layout, visible = False, key = 'LayConf', element_justification = 'left')]                                                                                                    
                        ]
                        
                        #=================================================================================================== definições da tela =============================================================================================================

                        #cria a janela da tela inicial do programa
                        janela = sg.Window('Sistema de Loja', inilayout).Finalize()

                        #garante que a tela abrirá em tamanho máximo
                        janela.Maximize()
                        f.attBoard(janela, dia)
            
                        #===================================================================================================== execução do programa =========================================================================================================

                        while True:                                
                            hora = f.calcHora()
                            janela['horario'].update(hora + 'h')
                            
                            #detector de ações da janela
                            event, values = janela.read()

                            #================================================================================================ ABA CLIENTES ==================================================================================================================
                            autocode = bd.clie_geracode()
                            pcod = bd.prod_geracode()
                            QTD = 0   

                            if event == 'CLIENTES':
                                f.mostraClie(janela)
                                
                            if event == 'ClieADD':
                                NOME, COD, RG, CPF, CEL, TEL, EMAIL, OBS, CEP, END, NUM, BAI, CID, EST = f.pickClie(values)
                                clireturn = 0
                                codes = bd.checa_clicode()
                                
                                if len(codes) == 0:
                                    codes = ['Correção']
                                    
                                for i in range(0, len(codes)):
                                    if COD == codes[i][0]:
                                        f.resposta(9)
                                        clireturn = 1
                                        break

                                if clireturn == 0:
                                    if NOME != '' and COD != '' and RG != '' and CPF != '' and CEL != '' and TEL != '' and EMAIL != '' and OBS != '' and CEP != '' and END != '' and NUM != '' and BAI != '' and CID != '' and EST != '':
                                        bd.add_clientes(NOME, COD, RG, CPF, CEL, TEL, EMAIL, OBS, CEP, END, NUM, BAI, CID, EST)
                                        NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                        autocode = bd.clie_geracode()
                                        f.limpaClie(janela, NOMES, VC, autocode)                
                                        
                            if event == 'ClieREMOVE':
                                if cargo == 'D':
                                    if NOMES:
                                        try:
                                            x = values['ClieBOX'][0]
                                            bd.rmv_clientes(x)
                                            NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                            janela['ClieBOX'].update(NOMES)
                                            janela['VCBOX'].update(NOMES)
                                            janela['cod'].update(x[0])
                                        except IndexError:
                                            x = ['', '', '']
                            
                                else:
                                    f.resposta(10)

                            if event == 'ClieSHOW':
                                if NOMES:
                                    try:
                                        x = values['ClieBOX'][0]
                                        show = bd.show_clientes_info(x)
                                        ft = ('Arial Black', 15)
                                        sg.popup(f'Nome: {show[0]}\nCódigo: {show[1]}\nRG: {show[2]}\nCPF: {show[3]}\nCelular: {show[4]}\nTelefone: {show[5]}\nE-mail: {show[6]}\nObservação: {show[7]}\nCEP: {show[8]}\nEndereço: {show[9]}\nNúmero: {show[10]}\nBairro: {show[11]}\nCidade: {show[12]}\nEstado: {show[13]}\n', font=ft, title='Informações')         
                                    except IndexError:
                                        x = ['', '', '']
                                    
                            if event == 'ClieEDIT':
                                if NOMES:
                                    try:
                                        x = values['ClieBOX'][0]
                                        pick = bd.pick_clientes_info(x)
                                        janela['nome'].update(pick[0])
                                        janela['cod'].update(pick[1])
                                        janela['rg'].update(pick[2])
                                        janela['cpf'].update(pick[3])
                                        janela['cel'].update(pick[4])
                                        janela['tel'].update(pick[5])
                                        janela['email'].update(pick[6])
                                        janela['Clieobs'].update(pick[7])
                                        janela['cep'].update(pick[8])
                                        janela['end'].update(pick[9])
                                        janela['num'].update(pick[10])
                                        janela['bairro'].update(pick[11])
                                        janela['cidade'].update(pick[12])
                                        janela['estado'].update(pick[13])  
                                    except IndexError:
                                        x = ['', '', '']             

                            if event == 'ClieACCEDIT':
                                if NOMES:
                                    try:
                                        x = values['ClieBOX'][0]
                                        NOME, COD, RG, CPF, CEL, TEL, EMAIL, OBS, CEP, END, NUM, BAI, CID, EST = f.pickClie(values)

                                        if NOME != '' and COD != '' and RG != '' and CPF != '' and CEL != '' and TEL != '' and EMAIL != '' and OBS != '' and CEP != '' and END != '' and NUM != '' and BAI != '' and CID != '' and EST != '':
                                            bd.att_clientes(NOME, COD, RG, CPF, CEL, TEL, EMAIL, OBS, CEP, END, NUM, BAI, CID, EST, x)    
                                            NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                            autocode = bd.clie_geracode()
                                            f.limpaClie(janela, NOMES, VC, autocode)
                                            
                                    except IndexError:
                                        x = ['', '', '']
                                
                            #================================================================================================ ABA PRODUTOS ==================================================================================================================
                            if event == 'PRODUTOS':
                                f.mostraProd(janela)

                            if event == 'ProdADD':                                
                                if values['Insumo'] == True:
                                    insumo = 'S'
                                else:
                                    insumo = 'N'

                                PROD, PCOD, CAT, MARCA, EMIN, EMAX, PRODOBS, CUSTO, VATA, VVAR = f.pickProd(values)
                                pcodes = bd.checa_prodcode()
                                
                                if len(pcodes) == 0:
                                    pcodes = ['Correção']

                                prodreturn = 0
                                
                                for i in range(0, len(pcodes)):
                                    if PCOD == pcodes[i][0]:
                                        f.resposta(9)
                                        prodreturn = 1
                                        break
                                    
                                if prodreturn == 0:
                                    if PROD != '' and PCOD != '' and CAT != '' and MARCA != '' and EMIN != '' and EMAX != '' and PRODOBS != '' and CUSTO != '' and VATA != '' and VVAR != '':
                                        bd.add_produtos(PROD, PCOD, CAT, MARCA, EMIN, EMAX, PRODOBS, CUSTO, VATA, VVAR, QTD, insumo)                                            
                                        NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                        pcod = bd.prod_geracode()
                                        f.limpaProd(janela, PRODU, VP, CP, pcod)

                            if event == 'ProdREMOVE':
                                if cargo == 'D':
                                    if PRODU:
                                        try:
                                            x = values['ProdBOX'][0]
                                            bd.rmv_produtos(x)
                                            NOMES, PRODU, VP, VC, CP, VENDA = f.attList()                
                                            janela['ProdBOX'].update(PRODU)
                                            janela['CPBOX'].update(CP)
                                            janela['VPBOX'].update(VP)
                                            janela['pcod'].update(x[0])
                                        except IndexError:
                                            x = ['', '']

                                else:
                                    f.resposta(10)
                                    
                            if event == 'ProdSHOW':
                                if PRODU:
                                    try:
                                        x = values['ProdBOX'][0]
                                        show = bd.show_produtos_info(x)

                                        if show[11] == 'S':
                                            insumo = 'Sim'
                                            
                                        else:
                                            insumo = 'Não'
                                            
                                        sg.popup(f'Produto: {show[0]}\nCódigo: {show[1]}\nCategoria: {show[2]}\nMarca: {show[3]}\nEstoque mínimo: {show[4]}\nEstoque máximo: {show[5]}\nObservação: {show[6]}\nCusto: R$ {show[7]}\nValor de venda atacado: R$ {show[8]}\nValor de venda varejo: R$ {show[9]}\nQuantidade: {show[10]}\nInsumo: {insumo}', font=ft, title='Informações') 
                                    except IndexError:
                                        x = ['', '']                                    

                            if event == 'ProdEDIT':
                                if PRODU:
                                    try:
                                        x = values['ProdBOX'][0] 
                                        pick = bd.pick_produtos_info(x)
                                        janela['produto'].update(pick[0])
                                        janela['pcod'].update(pick[1])
                                        janela['cate'].update(pick[2])
                                        janela['marca'].update(pick[3])
                                        janela['min'].update(pick[4])
                                        janela['max'].update(pick[5])
                                        janela['Prodobs'].update(pick[6])
                                        janela['custo'].update(pick[7])
                                        janela['atac'].update(pick[8])
                                        janela['var'].update(pick[9])

                                        if pick[11] == 'S':
                                            janela['Insumo'].update(True)
                                            
                                        else:
                                            janela['Insumo'].update(False)
                                            
                                    except IndexError:
                                        x = ['', '']

                            if event == 'ProdACCEDIT':
                                if PRODU:
                                    try:
                                        x = values['ProdBOX'][0]
                                        
                                        if values['Insumo'] == True:
                                            insumo = 'S'

                                        else:
                                            insumo = 'N'
                                            
                                        PROD, PCOD, CAT, MARCA, EMIN, EMAX, PRODOBS, CUSTO, VATA, VVAR = f.pickProd(values)
                                
                                        if PROD != '' and PCOD != '' and CAT != '' and MARCA != '' and EMIN != '' and EMAX != '' and PRODOBS != '' and CUSTO != '' and VATA != '' and VVAR != '':
                                            bd.att_produtos(PROD, PCOD, CAT, MARCA, EMIN, EMAX, PRODOBS, CUSTO, VATA, VVAR, insumo, x)
                                            NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                            pcod = bd.prod_geracode()
                                            f.limpaProd(janela, PRODU, VP, CP, pcod)
                                            
                                    except IndexError:
                                        x = ['', '']                                    
                                    
                            #================================================================================================ ABA VENDAS ==================================================================================================================
                            try:
                                if values['val'] != '' and values['parc'] != '1' and values['des'] != '' and values['frete'] != '':
                                    janela['valpar'].update(round((float(values['val'].replace(',', '.')) - float(values['des'].replace(',', '.')) + float(values['frete'].replace(',', '.')))/float(values['parc']), 2))

                            except TypeError:
                                janela['valpar'].update('')
                            
                            if event == 'VENDAS':
                                f.mostraVend(janela)

                                
                            if event == 'cliv':
                                lista2 = []
                                for i in range (0, len(VC)):
                                    lista2.append(VC[i][1])
                                vczinho = [i for i in lista2 if values['cliv'].lower() in i.lower()]
                                janela['VCBOX'].update(vczinho)

                                if values['cliv'] == '':
                                    janela['VCBOX'].update(VC)
                                    
                            if event == 'prodv':
                                lista3 = []
                                for i in range (0, len(VP)):
                                    lista3.append(VP[i][1])
                                vpzinho = [i for i in lista3 if values['prodv'].lower() in i.lower()]
                                janela['VPBOX'].update(vpzinho)

                                if values['prodv'] == '':
                                    janela['VPBOX'].update(VP)

                            if event == 'ClieFIND':
                                try:
                                    x = values['VCBOX'][0]
                                    
                                    if values['cliv'] == ''  or len(x)==2:
                                        janela['cliv'].update(x[1])

                                    else:
                                        janela['cliv'].update(x)              

                                except IndexError:
                                    x = ['', '']
                                    
                            if event == 'VendPFind':
                                try:
                                    x = values['VPBOX'][0]
                                    if values['prodv'] == '' or len(x)==2:
                                        janela['prodv'].update(x[1])

                                    else:
                                        janela['prodv'].update(x)

                                except IndexError:
                                    x = ['', '']

                            if event == 'VendADD':
                                
                                checagem = bd.checa_prod()
                                contagem = 0
                                checagem_cli = bd.checa_cli()
                                conta_cli = 0

                                for i in range(0, len(checagem)):
                                    if values['prodv'] == checagem[i][0]:
                                        j = i
                                        contagem += 1

                                for i in range(0, len(checagem_cli)):
                                    if values['cliv'] == checagem_cli[i][0]:
                                        conta_cli += 1

                                if conta_cli != 0:                                        
                                    if contagem != 0:

                                        if checagem[j][1] == 'N': 
                                            PRODUTO, CLIENTE, QUANTIDADE, VALOR, DESCONTO, FRETE, PAGAMENTO, PARCELAMENTO, VALORPARC, VENCIMENTO = f.pickVend(values)

                                            if VALOR != ''  and DESCONTO != ''  and FRETE != '': 
                                                TOTAL = round((float(VALOR) - float(DESCONTO) + float(FRETE)), 2)

                                            if CLIENTE != '' and PRODUTO != '' and QUANTIDADE != '' and VALOR != '' and DESCONTO != '' and FRETE != '' and PAGAMENTO != '' and PARCELAMENTO != '' and VALORPARC != '' and VENCIMENTO != '':
                                                bd.add_venda(CLIENTE, PRODUTO, QUANTIDADE, VALOR, DESCONTO, FRETE, TOTAL, PAGAMENTO, PARCELAMENTO, VALORPARC, VENCIMENTO)
                                                NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                                f.limpaVend(janela, VENDA)

                                        else:
                                            f.resposta(11)
                                            janela['prodv'].update('')
                                            NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                            janela['VPBOX'].update(VP)

                                    else:
                                        f.resposta(12)
                                        janela['prodv'].update('')
                                        NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                        janela['VPBOX'].update(VP)

                                else:
                                    f.resposta(13)
                                    janela['cliv'].update('')
                                    NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                    janela['VCBOX'].update(VC)
                                    
                            if event == 'VendREMOVE':
                                if cargo == 'D':
                                    if VENDA:
                                        try:
                                            x = values['VendBOX'][0]
                                            bd.rmv_venda(x)
                                            NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                            f.limpaVend(janela, VENDA)

                                        except IndexError:
                                            x = ['', '']
                                else:
                                    f.resposta(10)
                                        
                            if event == 'VendEDIT':
                                if VENDA:
                                    try:
                                        x = values['VendBOX'][0]
                                        pick = bd.pick_venda_info(x)
                                        janela['cliv'].update(pick[0])
                                        janela['prodv'].update(pick[1])
                                        janela['qtd'].update(pick[2])
                                        janela['val'].update(pick[3])
                                        janela['des'].update(pick[4])
                                        janela['frete'].update(pick[5])
                                        janela['pag'].update(pick[6])
                                        janela['parc'].update(pick[7])
                                        janela['valpar'].update(pick[8])
                                        janela['venc'].update(pick[9])
                                    except IndexError:
                                        x = ['', '', '']             

                            if event == 'VendACCEDIT':
                                if VENDA:
                                    try:
                                        x = values['VendBOX'][0]
                                        PRODUTO, CLIENTE, QUANTIDADE, VALOR, DESCONTO, FRETE, PAGAMENTO, PARCELAMENTO, VALORPARC, VENCIMENTO = f.pickVend(values)
                                        
                                        if VALOR != ''  and DESCONTO != ''  and FRETE != '': 
                                            TOTAL = round((float(VALOR) - float(DESCONTO) + float(FRETE)), 2)

                                        if CLIENTE != '' and PRODUTO != '' and QUANTIDADE != '' and VALOR != '' and DESCONTO != '' and FRETE != '' and PAGAMENTO != '' and PARCELAMENTO != '' and VALORPARC != '' and VENCIMENTO != '':
                                            bd.att_venda(CLIENTE, PRODUTO, QUANTIDADE, VALOR, DESCONTO, FRETE, TOTAL, PAGAMENTO, PARCELAMENTO, VALORPARC, VENCIMENTO, x)
                                            NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                            f.limpaVend(janela, VENDA)
                                            
                                    except IndexError:
                                        x = ['', '', '']

                            if event == 'VendENTRE':
                                if VENDA:
                                    try:
                                        x = values['VendBOX'][0]
                                        aux = bd.pega_valor(x)
                                        bd.registra_venda(float(aux[0]), dia)
                                        aux2 = bd.pick_venda_info(x)
                                        aux3 = bd.antiga_quant(x[1])                                      
                                        qtd = int(aux3[0]) - int(aux2[2])
                                        bd.altera_quant(qtd, aux2[1])
                                        bd.rmv_venda(x)
                                        NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                        f.limpaVend(janela, VENDA)
                                        janela['CPBOX'].update(CP)
                                                                               
                                    except IndexError:
                                        x = ['', '', '']
                                        
                            if event == 'VendSHOW':
                                if VENDA:
                                    try:
                                        x = values['VendBOX'][0]
                                        show = bd.show_venda_info(x)
                                        if show[9] != 'N/A':
                                            sg.popup(f'Cliente: {show[0]}\nProduto: {show[1]}\nQuantidade: {show[2]}\nValor: R$ {show[3]}\nDesconto: R$ {show[4]}\nFrete: R$ {show[5]}\nValor total: R$ {show[6]}\nPagamento: {show[7]}\nParcelamento: {show[8]}\nValor das parcelas: R$ {show[9]}\nData de entrega: {show[10]}\n', font=ft, title='Informações') 

                                        else:
                                            sg.popup(f'Cliente: {show[0]}\nProduto: {show[1]}\nQuantidade: {show[2]}\nValor: R$ {show[3]}\nDesconto: R$ {show[4]}\nFrete: R$ {show[5]}\nValor total: R$ {show[6]}\nPagamento: {show[7]}\nParcelamento: {show[8]}\nValor das parcelas: {show[9]}\nData de entrega: {show[10]}\n', font=ft, title='Informações') 

                                    except IndexError:
                                        x = ['', '']                                   
                            #================================================================================================ ABA COMPRAS ==================================================================================================================            
                            if event == 'COMPRAS':
                                f.mostraComp(janela)
                                f.attProd() 
                                        
                            if event == 'prodc':
                                lista = []
                                
                                for i in range (0, len(CP)):
                                    lista.append(CP[i][0])

                                cpzinho = [i for i in lista if values['prodc'].lower() in i.lower()]
                                janela['CPBOX'].update(cpzinho)

                                if values['prodc'] == '':
                                    janela['CPBOX'].update(CP)

                            if event == 'CompPFind':                                
                                try:
                                    x = values['CPBOX'][0]
                                except IndexError:
                                    x = ['', '']

                                f.attProd()
                                        
                                if values['prodc'] == '' or len(x)==2:
                                    janela['prodc'].update(x[0])

                                else:
                                    janela['prodc'].update(x)
                                        
                            if event == 'CompPQTD':
                                chec_prod =  bd.checa_prod()
                                count = 0

                                for i in range(0, len(chec_prod)):
                                    if values['prodc'] == chec_prod[i][0]:
                                        j = i
                                        count += 1

                                if count != 0:                                                                     
                                    if cargo == 'D':
                                        if values['quanti'] != '' and values['prodc']:
                                            qtd = values['quanti']
                                            
                                            try:
                                                x = values['CPBOX'][0]
                                            except IndexError:
                                                x = ['', '']
                                                
                                            if x[0] != '':
                                                if isinstance(x, str):                                                    
                                                    old_quant = bd.antiga_quant(x)
                                                    bd.altera_quant(qtd, x)
                                                    
                                                    NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                                    janela['ProdBOX'].update(PRODU)
                                                    janela['CPBOX'].update(CP)
                                                    janela['VPBOX'].update(VP)
                                                    f.limpaComp(janela)
                                                    atividade = f'Item {x} atualizado:\nquantidade alterada de {old_quant[0]} para {qtd} no dia {dia}.'                                                   
                                                    bd.add_ativ(atividade)
                                                    registros = f.attREG()
                                                    janela['RegBOX'].update(registros)
                                                else:
                                                    old_quant = bd.antiga_quant(x[0])
                                                    bd.altera_quant(qtd, x[0])
                                                    
                                                    NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                                    janela['ProdBOX'].update(PRODU)
                                                    janela['CPBOX'].update(CP)
                                                    janela['VPBOX'].update(VP)
                                                    f.limpaComp(janela)
                                                    atividade = f'Item {x[0]} atualizado:\nquantidade alterada de {old_quant[0]} para {qtd} no dia {dia}.'                                                   
                                                    bd.add_ativ(atividade)
                                                    registros = f.attREG()
                                                    janela['RegBOX'].update(registros)
                                        f.attProd()
                                        
                                    else:
                                        f.resposta(10)
                                        f.attProd()
                                        
                                else:
                                    f.resposta(12)
                                    f.limpaComp(janela)
                                    NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                    janela['CPBOX'].update(CP)                                            
                                    registros = f.attREG()
                                    janela['RegBOX'].update(registros)                                
                                    f.attProd()                                   

                            if event == 'CompADD':
                                checa_produto = bd.checa_prod()
                                existe = 0

                                for i in range(0, len(checa_produto)):
                                    if values['prodc'] == checa_produto[i][0]:
                                        j = i
                                        existe += 1

                                if existe != 0:                         
                                    prod = values['prodc']
                                    qtd = values['Compqtd']
                                    custo_total = values['Compval']

                                    if values['prodc'] != '' and values['Compqtd'] != '' and values['Compval'] != '':
                                        f.reajusta(values, dia)  
                                        registros = f.attREG()
                                        NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                        janela['RegBOX'].update(registros)
                                        janela['ProdBOX'].update(PRODU)
                                        janela['CPBOX'].update(CP)
                                        janela['VPBOX'].update(VP)
                                        f.limpaComp(janela)
                                    f.attProd()

                                else:
                                    f.resposta(12)
                                    f.limpaComp(janela)
                                    NOMES, PRODU, VP, VC, CP, VENDA = f.attList()
                                    janela['CPBOX'].update(CP)
                                    registros = f.attREG()
                                    janela['RegBOX'].update(registros)                                
                                    f.attProd()
                                
                            if event == 'RegLIMPE':
                                if cargo == 'D':
                                    bd.limpa_registro()
                                    registros = f.attREG()
                                    janela['RegBOX'].update(registros)
                                    f.attProd()
                                    
                                else:
                                    f.resposta(10)
                                    f.attProd()
                                    
                            #================================================================================================ FECHAR JANELA ==================================================================================================================            
                            if event == 'SAIR':
                                janela.close()
                                break
                              
                            if event == sg.WIN_CLOSED:
                                janela.close()
                                break

                            #================================================================================================ ABA VENDAS ==================================================================================================================                    
                            if event == 'HOME':
                                f.mostraHome(janela)
                                f.attBoard(janela, dia)

                            #================================================================================================ ABA FINANCEIRO ==================================================================================================================            
                            if event == 'FINANCEIRO':
                                if cargo == 'D':
                                    f.mostraFinan(janela)
                                    
                                else:
                                    f.resposta(14)          

                            if event == 'FinaFIND':
                                if values['perini'] != '' and values['perfim'] != '' and values['esperecei'] != '' and values ['espedesp'] != '':
                                    f.calculaFinan(janela, values)
                                                                        
                                else:
                                    f.resposta(16)

                            #================================================================================================ ABA CONFIG ==================================================================================================================            
                            if event == 'CONFIG':
                                if cargo == 'D':
                                    f.mostraConf(janela)
                                else:
                                    f.resposta(14)
                                    
                    else:
                        f.resposta(17)
                        f.limpaLogin(telalogin)
                        
            if cont == 0:
                f.resposta(8)
                f.limpaLogin(telalogin)
                cont = 0

if __name__ == '__main__':
    main()
