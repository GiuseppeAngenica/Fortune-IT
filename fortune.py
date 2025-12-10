import os
import random
import textwrap
from pathlib import Path


def speech_bubble(text):
    lines = []
    for paragraph in text.split("\n"):
        # se la riga è vuota, la manteniamo per non perdere spazi
        if paragraph.strip() == "":
            lines.append("")
        else:
            # avvolge solo righe troppo lunghe, ma rispetta gli a capo originali
            wrapped = textwrap.wrap(paragraph, width=9999999)
            lines.extend(wrapped)

    # calcola la lunghezza della riga più lunga
    max_len = max(len(line) for line in lines) if lines else 0

    # costruisce la nuvoletta
    top = "  " + "_" * (max_len + 2)
    bottom1 = "  " + "-" * (max_len + 2)
    bottom2 = "     \\"
    bottom3 = "      \\"
    bubble_lines = [f"< {line.ljust(max_len)} >" for line in lines]

    return "\n".join([top] + bubble_lines + [bottom1] + [bottom2] + [bottom3])

def ascii_art():
    current_dir = str(Path(__file__).resolve().parent)
    ascii_folder = current_dir+"/ascii_art"

    # crea una lista di tutti i file che finiscono con .txt
    ascii_names = [f for f in os.listdir(ascii_folder) if f.endswith(".txt")]


    # sceglie un file casuale
    random_ascii = random.choice(ascii_names)
    # costruisce il percorso completo e apre il file
    ascii_folder = os.path.join(ascii_folder, random_ascii)
    with open(ascii_folder, "r", encoding="utf-8") as file:
        art = file.read()
    return art

def fortune():
    # percorso del file di testo
    current_dir = str(Path(__file__).resolve().parent)
    fortune_path = current_dir+"/phrases/fortune"

    # apri il file e leggi tutto il contenuto
    with open(fortune_path, "r", encoding="utf-8") as file:
        content = file.read()

    # dividi il testo in base al simbolo %
    phrases = [f.strip() for f in content.split("%") if f.strip()]

    # scegli una frase casuale
    random_fortune = random.choice(phrases)
    return random_fortune


#esecuzione
phrase = fortune()
bubble = speech_bubble(phrase)
art = ascii_art()

print(bubble)
print(art)
