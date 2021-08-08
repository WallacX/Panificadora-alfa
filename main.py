import os
import time
## VARIÁVEIS GLOBAIS (Disponível para acesso em todo o código)##

# Valor por unidade dos Pães
VMILHO = 0.15
VSAL = 0.25
VLEITE = 0.35

quantidade_vendas = 0

# valor total de cada tipo vendido
sal_qtd = 0
milho_qtd = 0
leite_qtd = 0

## --------------------------------------- ##

## MINHAS FUNÇÕES ##
def novavenda():#minha função
  os.system('clear') #limpa a tela

 # variáveis locais
  print ("+++++++ Nova venda +++++++ \n")
  qtsal = int(input ("Digite a quantidades de pães de sal: "))
  qtleite = int(input("Digite a quantidades de pães de leite: "))
  qtmilho = int(input("Digite a quantidades de pães de milho: "))

  # Quantidade total
  paovendasdia = qtsal + qtmilho + qtleite
  #Valor total
  valortt=qtleite*VLEITE+qtmilho*VMILHO+qtsal*VSAL

  print ("O total de pães vendidos foi %.0f:"% paovendasdia)
  print ("O valor total foi R$  %.2f reais:"% valortt)

  # A cada venda o valor dessa variável é incrementada em 1
  global quantidade_vendas, sal_qtd, milho_qtd, leite_qtd
  quantidade_vendas = quantidade_vendas + 1
  sal_qtd = sal_qtd + qtsal
  milho_qtd = milho_qtd + qtmilho
  leite_qtd = leite_qtd + qtleite
 
  input("\n\nPressione ENTER para continuar: ")
  os.system('clear') #limpa a tela



def relatorio():
  os.system('clear')
  print ("  ***Relatório do Dia***")
  print ("\n")
  print ("Quantidades de vendas do dia:" ,quantidade_vendas)
  print ("\nQuantidade por tipo de pão:")
  print ("\t+ Sal: %.f unidades = R$ %.2f reais" % (sal_qtd,sal_qtd*VSAL))
  print ("\t+ Leite: %.2f unidades = R$ %.2f reais" % (leite_qtd,leite_qtd*VLEITE))
  print ("\t+ Milho: %.2f unidades = R$ %.2f reais" % (milho_qtd,milho_qtd*VMILHO))

  v_tt=sal_qtd*VSAL+leite_qtd*VLEITE+milho_qtd*VMILHO
  print("\nValor total do dia: R$ %.2f reais" % v_tt)
  q_tt=sal_qtd + leite_qtd + milho_qtd
  print("Quantidade total de pães:%.0f unidades" %q_tt)

  input("\n\nPressione ENTER para continuar: ")
  os.system('clear')

 ######## MENU #########
 

while(True): # loop infinito
  print(" *** PANIFICADORA PÃO DURO ***")
  print("Quantidade de vendas realizadas hoje: ",quantidade_vendas)
  print("1 - Nova venda")
  print("2 - Gerar relatório")
  print("3 - Sobre")
  print("4 - Sair")

 # Pegar a opção do usuário
  opcao = input ("Digite a opção desejada: ")

 # Verificar qual opção o usuário escolheu
  if (opcao == "1"): # NOVA VENDA 
   novavenda() # Chamar uma função
  elif(opcao == "2"): #senao se
   relatorio()
  elif(opcao == "3"):
    os.system('clear') #limpa a tela
    print("Desenvolvido por Wallace Cardoso")
    time.sleep(10)
    os.system('clear') #limpa a tela
  elif(opcao == "4"):
    os.system('clear') #limpa a tela
    print("\n\nPrograma finalizado, obrigado pela preferência!")
    time.sleep(5)
    break #interrompe a executação do laço
  else:
    print("Opção inválida, tente novamente!")  