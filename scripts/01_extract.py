#mit "python3 01_extract.py" im terminal ausführen

import tarfile
import os

# Verzeichnisse und Pfade festlegen
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = os.path.join(PROJECT_DIR, "tageszeitungen_gesamt")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "data-lake")

# .tar entpacken
os.makedirs(OUTPUT_DIR, exist_ok=True) #Verzeichnis wird erstellt, falls dieses bereits existiert, läuft das Programm dennoch weiter

for filename in os.listdir(SOURCE_DIR):
    if filename.endswith(".tar"):
        FILE_PATH = os.path.join(SOURCE_DIR, filename)
        with tarfile.open(FILE_PATH, "r:*") as tar:
            # Entpacken ohne Unterordner
            for member in tar.getmembers():
                # Den Pfad jedes Members im Archiv entfernen > flacher Auspackvorgang!
                member.name = os.path.basename(member.name)
                tar.extract(member, path=OUTPUT_DIR)