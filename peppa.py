"""
MIT License

Copyright (c) 2021 Marcello Belanda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""



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