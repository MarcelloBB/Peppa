from os import system
import os

while True:                                    # LOOP
    c = input("> ")                            # Prompt. Altere como bem entender

    if c == "exit":                            # Sair ?    
        break

    elif c == "":                              # Repetir ?
        pass
    
    else:
        parts = c.split()                      # Dividir e conquistar. Só que não

        # FOLDER (name) => Cria uma pasta com o nome (name)
        if parts[0] == "folder":               # APAGUE SE QUISER (OPCIONAL)
            system("mkdir " + parts[1])

        # FILE (file) => Cria um arquivo com o nome (file)
        elif parts[0] == "file":               # APAGUE SE QUISER (OPCIONAL)
            with open(parts[1], "w") as file:
                pass

        # WRITE (msg) => Escreve o parâmetro (msg) na tela
        elif parts[0] == "write":              # APAGUE SE QUISER (OPCIONAL)
            if len(parts) > 2:
                for l in c[6:]:                # Verifica: deixa as separações (parts) de lado
                    print(l, end="")           # e analisa a partir do 6º caractere no comando raiz (c)
                print()
            else:
                print(parts[1])
            
        # Coloque seus comandos e condições aqui
        # ...