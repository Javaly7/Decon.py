from termcolor import colored
import base64
#Author: Javaly
#Versao: 1.0
#Enjoy!
while True:
    print(colored("""
    *   1) Encoder de base64
    *   2) Decoder de base64
    *   Bom dia!
    """, 'green'))
    try:
        quest = int(input(colored("Escolha uma Opcao: ", 'green')))
        if(quest == 1):
            quest2 = str(input(colored("Digite o Texto: ", 'green')))
            print(base64.b64encode(quest2.encode('ascii')))
        elif(quest == 2):
            quest3 = str(input(colored("Digite o Texto: ", 'green')))
            print(base64.b64decode(quest3.encode('ascii')))
        else:
          print("opçao invalida")
    except KeyboardInterrupt:
        print("Enjoy")
        break
    except:
        print("esse campo de valores so aceita valores inteiros!")
