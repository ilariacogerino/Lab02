import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        parola = input()
        t.handleAdd(parola)
        pass
    if int(txtIn) == 2:
        print("Ok, quale parola devo cercare?")
        parola = input()
        t.handleTranslate(parola)
    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare?")
        parola = input()
        t.handleWildCard()
    if int(txtIn) == 4:
        t.loadDictionary()
    if int(txtIn) == 5:
        break