
#menu
import os

print("1 - Nova venda")
print("2 - Gerar relatório")
print("3 - Sobre")
print("4 - Sair")
opcao = input ("Digite a opção desejada: ")

if (opcao == "1"):
  os.system('clear')
  sal = int(input ("Digite a quantidades de pães de sal: "))
  leite = int(input("Digite a quantidades de pães de leite: "))
  milho = int(input("Digite a quantidades de pães de milho: "))
  os.system('clear')
  print ("O total de pães vendidos foi",sal + milho + leite)
 
 


elif(opcao == "2"):
  print("Relatório")
  print("O total de pães vendidos foi:")
  print()
elif(opcao == "3"):
 print("Sobre")
elif(opcao == "4"):
  print("Sair")