class Translator:

    def __init__(self):
        pass

    def printMenu(self):
        print("--------------------------------")
        print("Translator Alien-Italian")
        print("--------------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        print("--------------------------------")
        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        pass

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        aliena = entry.split(" ")[0]
        italiana = entry.split(" ")[1]
        print(f"['{aliena}' - '{italiana}']")
        with open("dictionary.txt", "a", encoding="utf-8") as file:
            file.write(aliena + "\t" + italiana + "\n")
        print('Aggiunta!')
        pass

    def handleTranslate(self, query):
        with open("dictionary.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.split(" ")[0].__contains__(query):
                    traduzione = line.split(" ")[1]
                    #traduzione.strip()
                    print(f"[{traduzione}]")
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass


