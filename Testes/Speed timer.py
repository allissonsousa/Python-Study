from random import choice
import time
import keyboard

cronometro_ativo = False
inicio = 0
tempos = list()
resultado = list()
lista1 = ["R", "L", "B", "D", "F", "U"]
lista2 = ["", "2", "´"]
while len(resultado) != 12:
    cd1 = choice(lista1)
    cd2 = choice(lista2)
    cd3 = cd1 + cd2
    if not resultado:
        resultado.append(cd3)
    elif resultado[-1] != cd1 and resultado[-1] != cd3:
        resultado.append(cd3)
lista_sem_aspas = [elemento.replace("'", "") for elemento in resultado]
print(10 * "-=-")
print(resultado)
print(10 * "-=-")
resultado.clear()

print("Pressione [ESPAÇO] para iniciar/parar o cronômetro. Pressione [ESC] para sair.")

while True:

    if keyboard.is_pressed('space'):
        if not cronometro_ativo:
            inicio = time.time()
            cronometro_ativo = True
            print(f"⏱️ Iniciado...")
            print(10 * "-=-")
            while keyboard.is_pressed('space'):
                pass  # aguarda soltar a tecla para evitar múltiplas ativações
        else:
            fim = time.time()
            tempo = fim - inicio
            minutos = int(tempo) // 60
            segundos = int(tempo) % 60
            milissegundos = int((tempo - int(tempo)) * 1000)
            if minutos != 0:
                tempo_final = f"{minutos:02d}:{segundos:02d}.{milissegundos:03d}"
            elif segundos != 0:
                tempo_final = f"{segundos:02d}.{milissegundos:03d}"
            else:
                tempo_final = f"{segundos:02d}.{milissegundos:03d}"

            tempos.append(tempo_final)
            print(f"⏹️ Parado: {tempo_final} sg")
            print(10 * "-=-")
            tempos.append(tempo_final)
            cronometro_ativo = False
            while keyboard.is_pressed('space'):
                resultado.clear()
                pass
            while len(resultado) != 12:
                cd1 = choice(lista1)
                cd2 = choice(lista2)
                cd3 = cd1 + cd2
                if not resultado:
                    resultado.append(cd3)
                elif resultado[-1] != cd1 and resultado[-1] != cd3:
                    resultado.append(cd3)
            lista_sem_aspas = [elemento.replace("'", "") for elemento in resultado]
            print(resultado)
            print(10 * "-=-")


    elif keyboard.is_pressed('esc'):
        print("Encerrando.")
        print(10 * "-=-")
        break

print(tempos)
