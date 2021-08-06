import os
## VARIÁVEIS GLOBAIS (Disponível para acesso em todo o código)##

# Valor por unidade dos Pães
VMILHO = 0.15
VSAL = 0.25
VLEITE = 0.35

quantidade_vendas = 0

# valor total de cada tipo vendido
sal_tt = 0
milho_tt = 0
leite_tt = 0

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
   pao_vendas_dia=qtsal + qtmilho + qtleite
   #Valor total
   valortt=qtleite*VLEITE+qtmilho*VMILHO+qtsal*VSAL

   print ("O total de pães vendidos foi %.0f:"% pao_vendas_dia)
   print ("O valor total foi R$  %.2f reais:"% valortt)

   # A cada venda o valor dessa variável é incrementada em 1
   global quantidade_vendas, sal_qtd, milho_qtd, leite_qtd, pao_vendas_dia
   quantidade_vendas = quantidade_vendas + 1
   sal_qtd = sal_qtd + sal
   milho_qtd = milho_qtd + milho
   leite_qtd = leite_qtd + leite
 
   input("\n\nPressione ENTER para continuar: ")
   os.system('clear') #limpa a tela

   def relatorio():
    os.system('clear')
    print ("  ***Relatório do Dia***")
    print ("\n")
    print ("Quantidades de vendas do dia:" pao_vendas_dia)
    print ("\nQuantidade por tipo de pão:")
    print ("\t+ Sal: %.f unidades = R$ X reais" % (sal_tt,sal_tt*VSAL))
    print ("\t+ Leite: %.2f unidades = R$ X reais" % (leite_tt,leite_tt*VLEITE))
    print ("\t+ Milho: %.2f unidades = R$ X reais" % (milho_tt,milho_tt*VMILHO))

    v_tt=sal_tt*VSAL+leite_tt*VLEITE+milho_tt*VMILHO
    print("\nValor total do dia: R$ %.2f reais" % v_tt)
    q_tt=sal_tt + leite_tt + milho_tt
    print("Quantidade total de pães:%.0f unidades" %q_tt)

    input("\n\nPressione ENTER para continuar: ")
    os.system('clear')


 ######## MENU #########
 print(" *** PANIFICADORA PÃO DURO ***\n")
 print("Quantidade de vendas realizadas hoje: ",quantidade_vendas)
 while(True): # loop infinito
  print("1 - Nova venda")
  print("2 - Gerar relatório")
  print("3 - Sobre")
  print("4 - Sair")
  opcao = input ("Digite a opção desejada: ")


# Verificar qual opção o usuário escolheu
  if (opcao == "1"): # NOVA VENDA 
    novaVenda() # Chamar uma função
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