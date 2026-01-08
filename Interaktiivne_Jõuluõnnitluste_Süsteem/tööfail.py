def kirjuta_failisse(failinimi:str,loend:list):
    while True:
        reziim = input("Sisesta faili avamise reziim(w - kirjutamine, a - lisamine): ")
        if reziim not in ["w","a"]:
            print("Vale reziim! Proovi uuesti.")
        else:
            break
    for i in range(5):
        element = input("Sisesta rida, mida faili lisada: ")
        loend.append(element)
    with open(failinimi+".txt",reziim,encoding="utf-8") as f:
        for rida in loend:
            f.write(rida+"\n")

def loe_failist(failinimi:str)->list:
    with open(failinimi+".txt","r",encoding="utf-8") as f:
        for rida in f:
            loend.append(rida.strip())
        return loend


loend=["Rida 1  ", "Rida 2"]
failinimi = input("Sisesta faili nimi (ilma laiendita)")
kirjuta_failisse(failinimi,loend)
sisu=loe_failist(failinimi)
print("Faili sisu: ")
print(sisu)
for rida in sisu:
    print(rida)

