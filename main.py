""" 
ESTE PROGRAMA DIVIDE LOS KARDEX EN ARCHIVOS PEQUEÑOS LLAMADOS COMO EN LA VARIABLE name
RECUERDA QUE DEBES ELIMINAR LAS PRIMEAS TRES LINEAS DEL ARVHIVO ORIGINAR QUE SON COMO SIGUEN


        Documentos:               Todos                    
        Clientes:                 Todos                      
        Desde producto:           206AAA                  Hasta producto:         206RC15P-M156
        Vendedores:             Todos                      

        Fecha inicial de elaboración:         01/07/2020                          Fecha final de elaboración:         31/07/2020

PARA QUE TODAS LAS NOTAS SEAN IGUALES

ESCRITO POR LUIS MEX 8/19/2020

 """
name_notas = 'notas_ene.txt'
name = "Ene_2021_"


text = []
with open(name_notas, 'r', encoding='latin-1') as f:
    for line in f:
        linea = line.split()
        if len(linea) != 0:
            text.append(linea)

# print(text[0:21])

ini = ['M', 'Y', 'N', 'DISTRIBUIDORA,', 'S.A.', 'DE', 'C.V.']
stop = ['----------------------------------------------------------------------------------']
list_index = []
contador = 0
for line in text:
    if line == ini:
        list_index.append(contador)
    if line == stop:
        list_index.append(contador)
    contador += 1


cont = 0


for i in range(0, ((len(list_index)))):
    if i+1 < len(list_index) and i % 2 == 0:
        nota = (text[list_index[i]:list_index[i + 1]])
        #print(list_index[i],list_index[i + 1])

        file = open(name+str(cont)+".txt", "w")
        # file.write(str(nota))
        cont += 1
        for j in nota:
            temp = " ".join(j)
            file.write(temp+"\n")
    file.close()

# print(list_index)
# print(text[14:27])

# print(headlines)
