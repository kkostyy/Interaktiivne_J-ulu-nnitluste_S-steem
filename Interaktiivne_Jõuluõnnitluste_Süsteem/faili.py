from multiprocessing import JoinableQueue
import os
import glob


def otsi_faile_laiendi_jargi():
    laiend = input("Sisesta faililaiend: ").strip()
    if not laiend.startswith("."):
        laiend = "." + laiend

    failid = glob.glob(f"*{laiend}")
    print("Leitud failid:")
    print(failid)


def analuusi_fail():
    failinimi = input("Sisesta failinimi (ilma laiendita): ").strip()
    laiend = input("Sisesta faililaiend: ").strip()

    if not laiend.startswith("."):
        laiend = "." + laiend

    failitee = failinimi + laiend

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
        return

    print("\nFaili analüüsi tulemus:")
    print(f"Ridade koguarv: {ridade_koguarv}")
    print(f"Tühjade ridade arv: {tyhjade_ridade_arv}")
    print(f"TODO esinemisi: {todo_esinemised}")
    print(f"FIXME esinemisi: {fixme_esinemised}")


def loo_raporti_kataloog():
    nimi = "Analüüsi_Raportid"
    if not os.path.exists(nimi):
        os.mkdir(nimi)
        print("Raporti kataloog loodi.")
    else:
        print("Raporti kataloog on juba olemas.")


def otsi_faile_algustahega():
    taht = input("Sisesta faili algustäht: ").strip()
    failid = glob.glob(f"{taht}*.*")
    print("Leitud failid:")
    print(failid)

def otsi_faili(otsingu_tee="."):
    faili_nimi = input("Sisesta otsitava faili nimi (nt minu_fail.txt): ")
    for juur,kasutad,failid in os.walk(otsingu_tee):
        if faili_nimi in failid:
            return os.path.join(juur, faili_nimi)
    return "Faili ei leitud"
    tulemus = otsi_faili(otsitav_faili)
    print(tulemus)
