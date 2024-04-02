import csv
import sys

CR3 = sys.argv[1]

PTR = sys.argv[2]
tables = sys.argv[3]
Address = sys.argv[4]


Address = Address[6:]  #remove first 4 digits of address
offset = Address[-3:]  #store offset in variabe
Address = Address[:-3]  #remove offset from address


binary = bin(int(Address, 16))[2:]  #convert to binary
while(len(binary)<36):              # asegurarse que el digito tenga 36 bits.
   binary = '0' +binary


chunks = [binary[i:i + 9] for i in range(0, len(binary), 9)]        #dividir en cantos de 9 bits
# print (chunks)
table_index=[]                                                      #contiene los valores de los indexes


for i in chunks:                                                   #loop para convertir a decimal
    table_index.append(int(i, 2))

# print(table_index)

with open(tables, 'r') as f:                               #csv
    reader = csv.reader(f)
    data =list(reader)                                     # convertir csv a lista   probablemente era mejor convertirlo a dict




def buscar(nemo):                                            # funcion para el page miss
  off = nemo[-3:]                                            #decoding
  nemo =nemo[6:]
  nemo = nemo[:-3]
  h = []                                                     #tendra las tablas encontradas para llevar cuenta del proceso
  b = bin(int(nemo, 16))[2:]                              #convertir a binario
  while(len(b) < 36):                                        #asegurar que sea 36-bit
     b = '0' + b
  c = [b[i:i + 9] for i in range(0, len(b), 9)]                #dividir en 4 pedazos de 9 bits
  spots = []                                                #contiene los valores de los indexes

  for i in c:                                                 #convertir de binario a decimal
    spots.append(int(i, 2))
  
  for i in range(len(data[0])):                              #este loop busca la tabla de ept ptr y anade el valor de la segunda tabla a un array
    if(data[0][i] == PTR):
      h.append(data[spots[0]+1][i])
      # print(t)
      break

  for i in range(len(data[0])):
    if(data[0][i] == h[0]):
      h.append(data[spots[1]+1][i])
      # print(t)
      break

  for i in range(len(data[0])):
    if(data[0][i] == h[1]):
      h.append(data[spots[2]+1][i])
      # print(t)
      break

  for i in range(len(data[0])):
    if(data[0][i] == h[2]):
      h.append(data[spots[3]+1][i])
      # print(t)
      break

  h[3] = h[3][:-3] + off
  
  return h[3]
  

   


t = []

for i in range(len(data[0])):
  if(data[0][i] == CR3):
    t.append(data[table_index[0]+1][i])
    # print(t)
    break

if(len(t) <1):
    sys.exit()

for i in range(len(data[0])):
  if(data[0][i] == t[0]):
    t.append(data[table_index[1] +1][i])
    break

if(len(t)<2):
    t.append(buscar(t[0]))
    

for i in range(len(data[0])):
  if(data[0][i] == t[1]):
    t.append(data[table_index[2] +1][i])
    break

if(len(t)<3):
    t.append(buscar(t[1]))
    

for i in range(len(data[0])):
  if(data[0][i] == t[2]):
    t.append(data[table_index[3] +1][i])
    break

if(len(t)<4):
    t.append(buscar(t[2]))
    

result  = t[3]
result = result[:-3]
result =result +offset



# print(t)
print(result)

    
    



