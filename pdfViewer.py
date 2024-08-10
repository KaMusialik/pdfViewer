import sys
import subprocess
import os

from PyQt5.QtWidgets import QFileDialog, QApplication


def zeigePDF(filename):

    if not filename:
        print("keine Datei festgelegt!!!")
        sys.exit(0)

    if pruefeObDateiExistiert(filename) == 1:
        print('Datei existiert nicht. Abbruch')
        sys.exit(0)

    oefnePDF(filename)

def pruefeObDateiExistiert(filename):
    if os.path.isfile(filename):
        print('pruefeObDateiExistiert: Datei existiert.')
        return 0
    else:
        print('pruefeObDateiExistiert: Datei existiert nicht.')
        return 1

def pruefeObVerzeichnisExistiert(dir):
    if os.path.isdir(dir):
        print('pruefeObVerzeichnisExistiert: Verzeichnis existiert.')
        return 0
    else:
        print('pruefeObVerzeichnisExistiert: Verzeichnis existiert nicht.')
        return 1


def oefnePDF(filename):

    if sys.platform == "Windows":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


def waehleEinPDF(workDir = None):

    app = QApplication(sys.argv)

    if workDir == None:
        filename, _ = QFileDialog.getOpenFileName(filter="PDF (*.pdf)")
    else:
        if pruefeObVerzeichnisExistiert(workDir) == 1:  # Verzeichnis existiert nicht
            filename, _ = QFileDialog.getOpenFileName(filter="PDF (*.pdf)")
        else:
            filename, _ = QFileDialog.getOpenFileName(filter="PDF (*.pdf)", directory=workDir)

    return filename

if __name__ == "__main__":

    anzahlArrgumente = len(sys.argv)
    if anzahlArrgumente == 1:  # keine Arrgumente übergeben
        print('keine Arrgumente übergeben')
        filename = waehleEinPDF()
    elif anzahlArrgumente == 2:  # genau eine Datei Übergeben
        print('genau eine Datei übergeben')
        filename = sys.argv[1]
    else:  # meherere dateine übergeben
        print('Es wurden mehrere Dateien übergeben. Es wird aber nur eine erwartet. Daher Abbruch!')
        sys.exit(0)

    zeigePDF(filename)