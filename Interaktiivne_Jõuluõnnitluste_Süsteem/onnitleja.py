import email
import smtplib, ssl
from email.message import EmailMessage

def saada_email(saaja_email):
    print("Kirjuta oma sõnum või kood, lõpeta sõnaga END")
    rida_list = []
    while True:
        rida = input()
        if rida == "END":
            break
        rida_list.append(rida)
    kiri = "\n".join(rida_list)

    teema="test e-kiri pythonist"
    saatja_email="kosgaponenko@gmail.com"
    parool=input("sisesta rakenduse parool: ")
    smtp_server="smtp.gmail.com"
    port=587
    context=ssl.create_default_context()

    msg=EmailMessage()
    msg.set_content(kiri)
    msg["subject"]=teema
    msg["from"]=saatja_email
    msg["to"]=saaja_email

    with open(r"C:\Users\opilane\source\repos\Interaktiivne_Jõuluõnnitluste_Süsteem\Interaktiivne_Jõuluõnnitluste_SüsteemJPG.jpg", "rb") as f:
        image_data = f.read()

    msg.add_attachment(
        image_data,
        maintype="image",
        subtype="jpg",
        filename="JPG.jpg"
    )

    try:
        with smtplib.SMTP(smtp_server,port) as server:
            server.starttls(context=context)
            server.login(saatja_email,parool)
            server.send_message(msg)
        print("e-kiri saadetud")
    except Exception as e:
        print(f"midagi läks valesti..{e}")

kellele=input("sisesta saaja e-posti address: ")
saada_email(kellele)