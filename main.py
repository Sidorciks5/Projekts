import os
from datetime import datetime
import pytz

# Faila nosaukums piezīmēm
faila_nosaukums = "piezimes.txt"

# Laika josla Latvijai
latvijas_laiks = pytz.timezone("Europe/Riga")

def dabut_laiku():
    return datetime.now(latvijas_laiks).strftime("%d-%m-%Y %H:%M:%S")

def pievienot_piezimi():
    piezime = input("Ieraksti savu piezīmi: ")
    if piezime.strip():
        laiks = dabut_laiku()
        ieraksts = f"{laiks} - {piezime.strip()}\n"
        with open(faila_nosaukums, "a", encoding="utf-8") as fails:
            fails.write(ieraksts)
        print("✅ Piezīme saglabāta!")
    else:
        print("⚠️ Tukša piezīme netiks saglabāta.")

def apskatit_piezimes():
    if os.path.exists(faila_nosaukums):
        with open(faila_nosaukums, "r", encoding="utf-8") as fails:
            saturs = fails.read()
            print("\n--- Visas piezīmes ---")
            print(saturs)
    else:
        print("Nav nevienas piezīmes.")

def mekle_piezimes():
    datums = input("Ievadi datumu (DD-MM-YYYY): ").strip()
    if not datums:
        print("⚠️ Datums nav ievadīts.")
        return
    atrastas = []
    if os.path.exists(faila_nosaukums):
        with open(faila_nosaukums, "r", encoding="utf-8") as fails:
            for rinda in fails:
                if datums in rinda:
                    atrastas.append(rinda.strip())
    if atrastas:
        print("\n--- Atrastās piezīmes ---")
        for ieraksts in atrastas:
            print(ieraksts)
    else:
        print("🔍 Nav piezīmju šajā datumā.")

def izveidot_kopiju():
    if not os.path.exists(faila_nosaukums):
        print("📁 Nav piezīmju ko kopēt.")
        return

    ar_laiku = datetime.now(latvijas_laiks).strftime("%d-%m-%Y_%H-%M-%S")
    jaunais_fails = f"piezimes_kopija_{ar_laiku}.txt"

    with open(faila_nosaukums, "r", encoding="utf-8") as ori:
        saturs = ori.read()

    with open(jaunais_fails, "w", encoding="utf-8") as kopija:
        kopija.write(saturs)

    print(f"✅ Piezīmes izkopētas failā: {jaunais_fails}")

def izvelne():
    while True:
        print("\nIzvēlies darbību:")
        print("1. Pievienot jaunu piezīmi")
        print("2. Apskatīt visas piezīmes")
        print("3. Meklēt piezīmes pēc datuma")
        print("4. Iziet")

        izvele = input("Tava izvēle: ")
        if izvele == "1":
            pievienot_piezimi()
        elif izvele == "2":
            apskatit_piezimes()
        elif izvele == "3":
            mekle_piezimes()
        elif izvele == "4":
            # Piedāvā kopiju pirms iziešanas
            atbilde = input("Vai vēlies izveidot kopiju visām piezīmēm pirms aizvēršanas? (j/n): ").lower()
            if atbilde == "j":
                izveidot_kopiju()
            print("👋 Programma beidzas.")
            break
        else:
            print("⚠️ Nepareiza izvēle.")

if __name__ == "__main__":
    try:
        import pytz
    except ImportError:
        print("Nepieciešama bibliotēka `pytz`. Instalē ar:\n  pip install pytz")
    else:
        izvelne()
