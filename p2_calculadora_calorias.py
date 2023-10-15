#https://replit.com/join/kxghdulbfb-a00573942
#sólo responde en caso de que aplique
peso = int(input("ingresa tu peso ej kg: "))
km = int(input("ingresa los kilómetros recorridos: "))
m = int(input("ingresa la distancia recorrida en metros: "))
tiempo = int(input("ingresa el tiempo en minutos: "))
tipo = int(input("si corriste escribe 1, si nadaste escribe 2, si anduviste en bici escribe 3: "))

if (tipo == 1):
  print("corriendo quemaste estas calorías: ", peso*km)

elif (tipo == 2):
  print("nadando quemaste estas calorías: ", (m*0.88)(peso*2.22*tiempo))

else:
  print("andando en bici quemaste estas calorías: ", 0.071*(peso*2.22)(tiempo))
