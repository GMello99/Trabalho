
import json
with open('Estoque.txt','r') as arquivo:
    estoque=json.loads(arquivo.read())

controle_on = True 
while controle_on == True:
	print ('Controle de estoque')
	print ('0 - Sair')
	print ('1 - Adicionar item')
	print ('2 - Remover item')
	print ('3 - Alterar item')
	print ('4 - Imprimir estoque')
	opção = int(input ('Faça sua escolha:'))
	if opção == 0:
		print ('Até Logo!')
		controle_on = False
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

with open('Estoque.txt','w') as arquivo:
    estoquefinal=json.dumps(estoque, sort_keys=True, indent=4)
    arquivo.write(estoquefinal)
