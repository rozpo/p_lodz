from pathlib import Path
path = Path('./lista.txt')


if path.exists():
    file = open('lista.txt','r')
    text = file.read()
    print(text)
    templist = []
    templist.extend(text)
    file.close()
    file = open('lista.txt','a')
    list = input("[imie, nazwisko, grupa]:").split()
    file.write(list[0] + " " + list[1] + " " + list[2] + '\n')
else:
    text = open('lista.txt','a')
    list = input("[imie, nazwisko, grupa]:").split()
    text.write(list[0] + " " + list[1] + " " + list[2] + '\n')
    print("utworzono liste w pliku!")