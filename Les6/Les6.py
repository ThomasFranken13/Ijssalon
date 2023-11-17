mijn_lijst = ["Wafels", "Softijs", "Schepijs", "Pannenkoeken"]
mijn_lijst.append("Muffins")
for item in mijn_lijst:
    print(f"Wij verkopen", item)
    

mijn_dictionary = {
    "merk" : "Mitshubishi",
    "model" : "Colt",
    "Bouwjaar" : 2010,
    "Kleur" : "blauw",
    "Staat" : "Gebruikt"
}

print(mijn_dictionary)
print(mijn_dictionary["model"])

keys = mijn_dictionary.keys()
print(keys)

values = mijn_dictionary.values()
print(values)