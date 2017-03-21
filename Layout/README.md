# Apropos

## Analyse
Analyses de mise en page réalisées sur les fichiers dans */Pages*.

* [Tesseract] -> **HOCR**(html) : zones et mots:
  * code :  `tesseract -l fra [input image] [output file] hocr`
  * */Layout/hocr*


* [PRImA Tesseract OCR to PAGE] (disponible que sur windows)
  * -> **PAGE**(xml) : zones:
    * code :  `...`
    * */Layout/T2P-layout*
  * -> **PAGE**(xml) : zones, lignes, mots et glyphes :
    * code :  `...`
    * */Layout/T2P-layout-glyphs*

[Tesseract]:<https://github.com/tesseract-ocr/tesseract>
[PRImA Tesseract OCR to PAGE]:<http://www.prima.cse.salford.ac.uk/tools/TesseractOCRToPAGE>

## WebViewer
Visonneuse d'analyses de mise en page (layout) en HTML sur les scans des pages, généré avec Javascript.
```
python -m SimpleHTTPServer 8000 # depuis la racine du projet.
```
Ouvir le navigateur et entrer l'url : `localhost:8000/Layout/WebViewer`
