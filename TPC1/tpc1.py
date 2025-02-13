import sys

def soma_on_off(input_file : str) -> None:
    with open(input_file, "r") as file:
        texto = file.read().lower()

    total = 0
    i = 0
    ligado = True

    while i < len(texto):
        if texto[i] == 'o':  
            if texto[i: i + 2] == 'on':  
                ligado = True
                i += 1
            elif texto[i: i + 3] == 'off':  
                ligado = False
                i += 3
        elif texto[i] == '=':
            print(total)
        elif ligado and texto[i].isdigit():
            total += int(texto[i])
        i += 1

if __name__ == "__tpc1__":
    input_file = sys.argv[1]
    soma_on_off(input_file)
