import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, scrolledtext

faila_nosaukums = "piezimes.txt"

# Funkcija: pievienot piezīmi
def pievienot_piezimi():
    teksts = ievades_lauks.get("1.0", tk.END).strip()
    if teksts:
        laiks = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ieraksts = f"{laiks} - {teksts}\n"
        with open(faila_nosaukums, "a", encoding="utf-8") as fails:
            fails.write(ieraksts)
        ievades_lauks.delete("1.0", tk.END)
        messagebox.showinfo("Veiksmīgi", "Piezīme pievienota!")
    else:
        messagebox.showwarning("Brīdinājums", "Lauks ir tukšs!")

# Funkcija: apskatīt visas piezīmes
def apskatit_piezimes():
    teksts = ""
    if os.path.exists(faila_nosaukums):
        with open(faila_nosaukums, "r", encoding="utf-8") as fails:
            teksts = fails.read()
    loga_skats.delete("1.0", tk.END)
    loga_skats.insert(tk.END, teksts)

# Funkcija: meklēt piezīmes pēc datuma
def mekle_piezimes():
    datums = mekle_lauks.get().strip()
    rezultats = ""
    if os.path.exists(faila_nosaukums):
        with open(faila_nosaukums, "r", encoding="utf-8") as fails:
            for rinda in fails:
                if datums in rinda:
                    rezultats += rinda
    loga_skats.delete("1.0", tk.END)
    loga_skats.insert(tk.END, rezultats if rezultats else "Nav piezīmju dotajā datumā.")

# GUI logs
logs = tk.Tk()
logs.title("Notikumu piezīmju ģenerators")

# Teksta ievades lauks
tk.Label(logs, text="Ievadi piezīmi:").pack()
ievades_lauks = scrolledtext.ScrolledText(logs, height=4, width=50)
ievades_lauks.pack()

tk.Button(logs, text="Pievienot piezīmi", command=pievienot_piezimi).pack(pady=5)
tk.Button(logs, text="Apskatīt visas piezīmes", command=apskatit_piezimes).pack()

# Meklēšanas lauks
tk.Label(logs, text="Meklēt pēc datuma (piem. 2025-05-26):").pack(pady=5)
mekle_lauks = tk.Entry(logs)
mekle_lauks.pack()
tk.Button(logs, text="Meklēt", command=mekle_piezimes).pack(pady=5)

# Rezultātu skats
loga_skats = scrolledtext.ScrolledText(logs, height=15, width=60)
loga_skats.pack(pady=10)

logs.mainloop()
