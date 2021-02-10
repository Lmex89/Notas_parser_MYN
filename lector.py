""" 
Este programa recibe los archivos de texto que fueron previamente 
dividos from main.py toma como entrada los nombre de los archivos 
en la varibale name = 'name._# txt' y el total de archivos 
partidos

Escrito por Luis Mex
Recuerda que total es el numero de archivos que tiene + 1
 """

import csv
name = "Ene_2021_"
ext = ".txt"
total = 53


def lectura(name, i):
    ext = ".txt"
    namec = name+repr(i)+ext

    current_line = 1
    linea_7 = ""
    data = []
    with open(namec, 'r') as file:
        for line in file:
            if current_line == 3 or current_line == 4 or current_line == 5:
                # print(line.split())
               # print("current",current_line)
                data.append(line.split())
            if current_line >= 7 and current_line != 8:
                linea_7 += (line)
               # print(linea_7)
                data.append(linea_7.split())
            current_line += 1
    return data


# with open("final.txt",'w') as f:
with open('final_notas.csv', 'w', newline='') as csvfile:
    fieldnames = ['Nota_de_venta', 'Cliente', 'Nombre_de_cliente', 'Observaciones']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(0, total):
        archivo = lectura(name, i)
        print('Nota de venta : {}'.format(archivo[0][5]))
        print("cliente: {}".format(archivo[1][1]))
        print("Nombre de Cliente : {}".format(archivo[2][1]))
        final = len(archivo) - 3
        a = (archivo[final])
        obs = ''
        for j in (a):
            obs += (j) + ' '
        print(obs)

        #print( f'{archivo[final]:1} {archivo[0][5]:5}')

        #f.write(archivo[0][5]+" "+archivo[1][1] +" "+archivo[2][1] +" \n" +archivo[final].ljust(10))
        #f.write("{0} {1} {2} \t {3} \n".format(archivo[0][5].rjust(10),archivo[1][1].rjust(10),archivo[2][1].rjust(10),obs ))

        writer.writerow(
            {'Nota_de_venta': archivo[0][5],
             'Cliente': archivo[1][1],
             'Nombre_de_cliente': archivo[2][1],
             'Observaciones': obs})


""" 
with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['Nota_de_venta', 'Cliente','Nombre_de_cliente','Observaciones']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Nota_de_venta': archivo[0][5], 'Cliente': archivo[1][1],'Nombre_de_cliente' : archivo[2][1],'Observaciones': obs })
  """
