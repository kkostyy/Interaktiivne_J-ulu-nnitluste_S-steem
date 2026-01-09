import glob
import os

f = open("data.txt","r")
print(dir(f))
f.close

def leia_projektifailid(laiend):
    if not laiend.startswith("."):
        laiend = "." + laiend
    return glob.glob(f"*{laiend}")
laiend = input("Sisesta faililaiend: ")
tulemus = leia_projektifailid(laiend)
print(tulemus)

def analuusi_faili_sisu(failitee):
    ridade_koguarv = 0
    tyhjade_ridade_arv = 0
    todo_esinemised = 0
    fixme_esinemised = 0
    try:
        with open(failitee, "r", encoding="utf-8", errors="ignore") as f:
            for rida in f:
                ridade_koguarv += 1
                if rida.strip() == "":
                    tyhjade_ridade_arv += 1
                todo_esinemised += rida.count("TODO")
                fixme_esinemised += rida.count("FIXME")
    except FileNotFoundError:
        print(f"Faili '{failitee}' ei leitud.")
        return None
    return {
        "ridade_koguarv": ridade_koguarv,
        "tyhjade_ridade_arv": tyhjade_ridade_arv,
        "todo_esinemiste_arv": todo_esinemised,
        "fixme_esinemiste_arv": fixme_esinemised
    }

failinimi = input("Sisesta failinimi: ").strip()
laiend = input("Sisesta faililaiend: ").strip()

if not laiend.startswith("."):
    laiend = "." + laiend

failitee = failinimi + laiend
tulemus = analuusi_faili_sisu(failitee)
print(tulemus)





    
     







