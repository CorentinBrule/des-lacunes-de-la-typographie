# Apropos

Les analyse de Reconnaisance Optique de Charactère ont été faites avec [Tesseract]. Les images des pages (500dpi) sont disponibles dans le fichier */Pages*.

script python pour Tesseract :

    import subprocess
    p=336
    while p<357:
        subprocess.call(["tesseract","-l","fra","../Pages/p"+str(p)+".png","p"+str(p)])
        p+=1

Corrections typographique avec l'aide de [Grammalecte] (module pour LibreOffice)

[Tesseract]:<https://github.com/tesseract-ocr/tesseract>
[Grammalecte]:<http://www.dicollecte.org/grammalecte/>
