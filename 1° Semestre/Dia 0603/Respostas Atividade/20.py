# Leia tempo em segundos (int). Converta para minutos inteiros com //= 60 e depois use %= para obter segundos restantes.

segundos = int(input("Insira os segundos: "))


#Não entendi ao certo como os segundos extras poderiam ser pegos, se segundos sempre vira minutos, ent fiz assim
minutos = segundos // 60
segundos %= 60

print(minutos, segundos)