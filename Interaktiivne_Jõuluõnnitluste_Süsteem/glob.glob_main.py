from faili import *
 


while True:
    print("\n--- MENÜÜ -------------------------------")
    print("1 – Otsi faile laiendi järgi")
    print("2 – Analüüsi faili sisu")
    print("3 – Loo raporti kataloog")
    print("4 – Otsi faile algustähe järgi")
    print("5 - ")
    print("6 – Lõpetamine")
    print("----------------------------------------")

    valik = input("Vali tegevus: ")

    if valik == "1":
        otsi_faile_laiendi_jargi()

    elif valik == "2":
        analuusi_fail()

    elif valik == "3":
        loo_raporti_kataloog()

    elif valik == "4":
        otsi_faile_algustahega()

    elif valik == "5":
        otsi_faili()

    elif valik == "6":
        print("Programmi töö lõppes.")
        break

    else:
        print("Vale valik!")

