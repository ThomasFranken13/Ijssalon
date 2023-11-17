mijn_dictionary = {
    "Voornaam" : "Harry",
    "Geboortedatum" : "31-maart-1992",
    "Registratienummer" : "AA18891"
}

print()
for k, v in mijn_dictionary.items():
    print (k, v)
    
mijn_dictionary["Achternaam"] = "de Vries"
print()
for k, v in mijn_dictionary.items():
    print (k, v)
    
    

print(len(mijn_dictionary))