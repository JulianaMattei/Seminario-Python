nombres_arch = open('nombres_1.txt','r', encoding="utf-8")
eval1_arch = open('eval1.txt', 'r')
eval2_arch = open('eval2.txt', 'r')

nombres = [linea.strip('\', \n \'') for linea in nombres_arch]
notas1 = [int(linea.strip(', \n ')) for linea in eval1_arch]
notas2 = [int(linea.strip(', \n ')) for linea in eval2_arch]

nombres_arch.close()
eval1_arch.close()
eval2_arch.close()

notas = []
for i, w in enumerate(notas1):
	notas.append(notas1[i] + notas2[i])

promedio = round(sum(notas)/len(notas), 2)

alumnos_todos = list(zip(nombres, notas))

alumnos_bajo_promedio = list(filter(lambda x: x[1] < promedio, alumnos_todos))

print(f"Alumnos con nota menor al promedio ({promedio}):")
for i, nombre in enumerate(alumnos_bajo_promedio):
	print(alumnos_bajo_promedio[i][0])
