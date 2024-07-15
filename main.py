from datetime import datetime



#inserindo data e hora
data_atual =datetime.now()


print('Ronda Preventiva TI-2024 ')
unidade =str(input("Digite a Unidade:.."))
andar=str(input("Digite o Andar:.."))
setor= str(input("Informe o setor:..."))
nome=str(input("Digite o nome do colaborador:... "))
cargo=str(input("Digite o cargo:"))
ocorrencia = int(input("Teve ocorrência?"))
if ocorrencia == 0:
    print("----RONDA PREVENTIVA TI-----")
    print(datetime.now())
    print(" Ronda realizada na unidade HAF-{}, Andar {} e o Setor Informado {} sem intercorrencias, validado por : {} função :{}".format(unidade,andar,setor,nome,cargo))
else:
     
    print("-----RONDA PREVENTIVA TI-----")
    print(datetime.now())
    print(" Ronda realizada na unidade HAF-{}, Andar {} e o Setor Informado {} com  intercorrencias, informado plantão TI".format(unidade,andar,setor,nome,cargo))

