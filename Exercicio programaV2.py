# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 21:06:46 2018

@author: luvi01
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
             if novaloja in lojas:
                 print ('Esta loja já esta cadastrada!!' )
             lojas[novaloja]={}
         if opção == 2:
             lojaremovida = input('Loja a ser removida:')
             if lojaremovida not in lojas:
                 print ('Esta loja não esta cadastrada!!')
             else:
                 del (lojas [lojaremovida])
         if opção == 3:
#=================================================================================================================================
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
                    opção = int(input ('Faça sua escolha:'))
                    if opção == 0:
                        print ('Até Logo!')
                        lojas [lojaescolhida]=estoque
                        runmode=False
                    if opção == 1:
                            b = input('Nome do produto:')
                            if b in estoque:
                                print ('Esse item já está no estoque')
                            else:
                                a = int(input('Quantidade inicial:'))
                                if a<0:
                                    print ('A quntidade inicial não pode ser negativa')
                                else:
                                    estoque [b] = a
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
                        print (estoque)
#====================================================================================================================================
         if opção == 4:
             print('LISTA DE LOJAS')
             for k in lojas.keys():
                 print(k)
#=========================================================================================================================================


with open('Estoque.txt','w') as arquivo:
    estoquefinal=json.dumps(lojas, sort_keys=True, indent=4)
    arquivo.write(estoquefinal)
