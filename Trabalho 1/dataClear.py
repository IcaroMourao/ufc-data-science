arq = open('crx.data', 'r')

i = 0
linhas = arq.readlines()

for i in range(0,len(linhas)):
	linhas[i] = linhas[i].split(',')

for linha in linhas:
	if linha[3] == 't':
		linha[3] = 3
	if linha[4] == 'g':
		linha[4] = 0
	if linha[4] == 'p':
		linha[4] = 1
	if linha[5] == 'j':
		linha[5] = 4
	if linha[5] == 'ff':
		linha[5] = 13
	if linha[6] == 'j':
		linha[6] = 3
	if linha[6] == 'ff':
		linha[6] = 7	
	if linha[8] == 't':
		linha[8] = 0		
	if linha[8] == 'f':
		linha[8] = 1
	if linha[9] == 't':
		linha[9] = 0
	if linha[9] == 'f':
		linha[9] = 1
	if linha[11] == 't':
		linha[11] = 0
	if linha[11] == 'f':
		linha[11] = 1
	if linha[12] == 'g':
		linha[12] = 0
	if linha[12] == 'p':
		linha[12] = 1

arq.close()

arq = open('crx.data', 'w')

for linha in linhas:
	for i in range(0,len(linha)):
		if i < 15:
			arq.write(str(linha[i])+',')
		else:
			arq.write(str(linha[i]))

arq.close()

