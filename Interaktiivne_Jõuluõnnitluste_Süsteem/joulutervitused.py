from onnitleja import kogu_soovid, kogu_saajad, koosta_onnitlused, saada_email

try:
    kogu_soovid()
    kogu_saajad()
except ValueError as viga:
    print("Viga andmete sisestamisel:", viga)
    exit()

# Запрос пароля один раз для всех писем
parool = input("Sisesta rakenduse parool: ")

while True:
    try:
        print("\n🎁 JÕULUÕNNITLUSTE MENÜÜ")
        print("1 - Õnnitle kõiki saajaid")
        print("2 - Õnnitle ühte saajat")
        print("3 - Õnnitle mitut saajat")
        print("0 - Välju")

        valik = int(input("Sinu valik: "))

        if valik == 1:
            tulemused = koosta_onnitlused()
        elif valik == 2:
            email = input("Sisesta e-posti aadress: ")
            tulemused = koosta_onnitlused([email])
        elif valik == 3:
            sisend = input("Sisesta e-postid komaga: ")
            aadressid = [e.strip() for e in sisend.split(",")]
            tulemused = koosta_onnitlused(aadressid)
        elif valik == 0:
            print("Programm lõpetatud 🎄")
            break
        else:
            print("Vale valik!")
            continue

        for t in tulemused:
            print(t)
            saaja = t.split(":")[0]
            sisu = t.split(":")[1].strip()
            # Передаем пароль в функцию
            saada_email(saaja_email=saaja)

    except ValueError as v:
        print("Viga:", v)
    except Exception as e:
        print("Tundmatu viga:", e)

