from time import sleep 
print("-"*40)
print("Olá,seja bem vindo ao conversor de Decimal")
print("-"*40)
print("Confira seu funcionamneto logo abaixo:")
print("""[1]-Para coverter decimal para binário
[2]-Para converter decimal para hexadecimal
[3]-Para converter decimal para octal""")
n=str(input("Vamos lá !!!,Qual é o seu nome ?")).strip()
e=str(input("Escolha uma das opções de conversão por favor...")).strip()
d=int(input("Digite um numero decimal"))
d2=d
print("Processando")
sleep(1)
if e=="1":
 base=""
 while d!=0:
  r=d%2
  base=str(r)+base
  d=d//2
 print('O numero {} em dicimal apos a conversão se tornou {} em binário'.format(d2, base))
elif e=="2":
 lista={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
 base=""
 while d!=0:
  r=d%16
  base=str(lista[r])+base
  d=d//16
 print("O numero {} em dicimal apos a conversão se tornou {} em hexadecimal".format(d2, base ))
elif e=="3":
 base=""
 while d!=0:
  r=d%8
  base=str(r)+base
  d=d//8
 print("O numero {} em dicimal apos a conversão se tornou {} em octal".format(d2, base))
else:
    print("Opção invalida...tente novamente")
print('Obrigado por utilizar nosso programa,',n,',volte sempre')    
 

 
