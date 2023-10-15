#https://replit.com/join/zzxopmwtol-a00573942 
precio = int(input("ingresa el precio de tu producto: "))
categoria = int(input("ingresa la cattegoría del producto (A=1, B=2, C=3): "))
unidades = int(input("ingresa la cantidad de unidades: "))

if (categoria == 1):
  descuento = precio-(precio*0.1)
elif (categoria ==2):
  descuento = precio-(precio*0.05)
else :
 descuento = precio-(precio*0.02)
   
if (unidades > 10):
  print("tu precio final es de: ", descuento -(descuento *0.05))

else:
  print(descuento)
