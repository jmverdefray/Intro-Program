
#Verifica si dos casillas de un tablero son del mismo color


#Entrada datos
cas1X=int(input("Primera X:"))
cas1Y=int(input("Primera Y:"))
cas2X=int(input("Segunda X:"))
cas2Y=int(input("Segunda Y:"))



if ((cas1X+cas1Y+cas2X+cas2Y)%2==0):
  print("Mismo color")
  
else:
  print("Distinto color")