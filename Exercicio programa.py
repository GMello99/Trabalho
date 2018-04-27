# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 21:06:46 2018

@author: Matheus
"""


import json
controle_on = True
try:
	with open('Estoque.txt','r') as arquivo:
		pass
except IOError:
	with open('Estoque.txt','a') as arquivo:
		arquivo.write("{}")
finally:
	with open('Estoque.txt','r') as arquivo:
		lojas=json.loads(arquivo.read())
        
#=====================================================================================================================================
	
	while controle_on == True:
         print ('PAINEL DE LOJAS:')
         print ('0-Sair')
         print ('1-Adicionar Loja')
         print ('2-Remover Loja')
         print ('3-Escolha de Loja')
         print ('4-Lojas no sistema')
         opção = int(input('Faça sua escolha:'))
         if opção == 0:
             print('até logo')
             controle_on = False
         if opção == 1:
             novaloja= input('Nome da Loja a ser adicionada:')
             print(type(novaloja))
             if novaloja in lojas:
                 print ('Esta loja já esta cadastrada!!' )
             else:
                 lojas[novaloja]={}
         if opção == 2:
             lojaremovida = input('Loja a ser removida:')
             if lojaremovida not in lojas:
                 print ('Esta loja não esta cadastrada!!')
             else:
                 del (lojas [lojaremovida])
         if opção == 3:
            estoque = {}
            lojaescolhida= input('Loja escolhida:')
            if lojaescolhida not in lojas:
                print ('Esta loja não esta cadastrada!!')
            else:
                estoque=lojas[lojaescolhida]
                runmode = True
                while runmode:
                    print ('Controle de estoque')
                    print ('0 - Sair e salvar')
                    print ('1 - Adicionar item')
                    print ('2 - Remover item')
                    print ('3 - Alterar item')
                    print ('4 - Imprimir estoque')
                    print ('5 - Alterar preço')
                    print ('6 - Lista dos produtos negativos')
                    print ('7 - Imprimir valor total')
                    opção = int(input ('Faça sua escolha:'))
                    if opção == 0:
                        print ('Até Logo!')
                        lojas [lojaescolhida]=estoque
                        runmode=False
                    
                    if opção == 1:
                            lista = []
                            b = input(str('Nome do produto:'))
                            if b in estoque:
                                print ('Esse item já está no estoque')
                            else:
                                a = int(input('Quantidade inicial:'))
                                lista.append(a)
                                p = float(input('valor do produto:'))                                                                    
                                if p < 0 : 
                                    print('somente valor positivo')
                                else :
                                    lista.append(p)
                                estoque[b] = lista
                                
                    
                    if opção == 2:
                        c = input ('Nome do produto:')
                        if c in estoque:
                            del (estoque [c])
                        else:
                            print ('Este item não foi encontrado')
                    if opção == 3:
                        d = input ('Nome do produto:')
                        if d not in estoque:
                            print ('Esse item não foi encontrado')
                        else:
                            e = int (input('Nova quantidade:'))
                            estoque [d] = (a+e)
                    if opção == 4:
                        print ('O estoque é composto pelos produtos, quantida e preço, respectivamente: {0}'.format(estoque))
                    if opção == 5:
                       k = input('nome do produto:')
                       if k not in estoque:
                           print('escolha um produto que esteja no estoque')
                       else :
                           p = float(input('valor do produto:'))
                           if p < 0 : 
                               print('somente valor positivo')
                           else :
                               estoque [k][1] = p 
                    
                    if opção == 6:
                        negativo = False
                        for l in estoque.values():
                            if l[0] < 0 :
                                negativo = True
                        if negativo == False:
                            print('não há valores negativos')
                        else:
                            for k, v in estoque.items():
                                if v[0] < 0 :
                                    print('Os produtos que estão em quantidade negativa são: {0}'.format(k,v[0]))
                    if opção == 7:
                        soma_total =  0
                        for w in estoque.values():
                            soma_total += (w[1] * w[0])
                        print('O valor total dos produtos no estoque é:{0} '.format(soma_total))
                        
#====================================================================================================================================
         if opção == 4:
             print('LISTA DE LOJAS')
             for k in lojas.keys():
                 print(k)
#=========================================================================================================================================


with open('Estoque.txt','w') as arquivo:
    estoquefinal=json.dumps(lojas, sort_keys=True, indent=4)
    arquivo.write(estoquefinal)