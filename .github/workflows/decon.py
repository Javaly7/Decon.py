#versao sem termcolor
import base64
#Author: Javaly
#Versao: 1.0
#Enjoy!
while True:
    print("""
    *   1) Encoder de base64
    *   2) Decoder de base64
    *   Bom dia!
    """)
    try:
        quest = int(input("Escolha uma Opcao: "))
        if(quest == 1):
            quest2 = str(input("Digite o Texto: "))
            print(base64.b64encode(quest2.encode('ascii')))
        elif(quest == 2):
            quest3 = str(input("Digite o Texto: "))
            print(base64.b64decode(quest3.encode('ascii')))
        else:
          print("opçao invalida")
    except KeyboardInterrupt:
        print("Enjoy")
        break
    except:
        print("esse campo de valores so aceita valores inteiros!")
