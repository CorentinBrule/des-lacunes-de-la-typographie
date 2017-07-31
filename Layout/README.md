# Apropos

### HOCR ou PAGE ?

* [HOCR] est un format de donnée de "OLR" (optical layout recognition) basé sur le html. L'outil en ligne de commande de [Tesseract] avec l'option HOCR ne arretait qu'au niveau des mots.
* Le labo de recherche [PRImA] a développé sont propre format le PAGE basé sue le xml. Ils proposent des outils open-source pour les visualiser et les éditer mais l'outil permettant de générer ces analyses n'est disponible que sur windows et les sources sont introuvables. Pourtant TPT utilise Tesseract et permet de générer un OLR jusqu'au niveau des caractères. 

*Mais :*

voir : [issue #135](https://github.com/tesseract-ocr/tesseract/issues/135), [pull request #310](https://github.com/tesseract-ocr/tesseract/issues/310). L'option `hocr_char_boxes` n'est pas disponible dans la version 3.04.01 dispo sur debian stretch (ni branch la master 4.00.00alpha) . Il faut donc compiler un [fork de la 3.05](https://github.com/nickjwhite/tesseract/tree/hocrcharboxes) `git clone --branch hocrcharboxes https://github.com/nickjwhite/tesseract.git` [avec ce tuto](https://github.com/tesseract-ocr/tesseract/wiki/Compiling-%E2%80%93-GitInstallation) ne pas oublier [le(s) fichier(s) de langue et d'osd](https://github.com/tesseract-ocr/tesseract/wiki/Data-Files#data-files-for-version-304305) à mettre dans `/usr/local/share/tessdata/` ou spécifier à la main avec l'option `--tessdate-dir`
Possibilité de convertir le HORC en PAGE avec http://www.prima.cse.salford.ac.uk/tools/PAGEConverterValidator

## Analyse
Analyses de mise en page réalisées sur les fichiers dans */Pages*.

* [Tesseract] -> **HOCR**(html) : zones et mots:
  * code :  `tesseract -l fra [input image] [output file] hocr`
  * */Layout/hocr*

* [Tesseract charboxes] -> **HOCR**(html) : zones, lignes, mots et glyphes : 
  * code : `tesseract {image file} -c tessedit_create_hocr=1 -c hocr_char_boxes=1 {output name}`
  * */Layout/hocr-charboxes*

* [PRImA Tesseract OCR to PAGE] (disponible que sur windows)
  * -> **PAGE**(xml) : zones:
    * code :  `...`
    * */Layout/T2P-layout*
  * -> **PAGE**(xml) : zones, lignes, mots et glyphes :
    * code :  `...`
    * */Layout/T2P-layout-glyphs*

[HOCR]:<https://en.wikipedia.org/wiki/HOCR>
[PRImA]:<http://primaresearch.org>
[Tesseract]:<https://github.com/tesseract-ocr/tesseract>
[PRImA Tesseract OCR to PAGE]:<http://www.prima.cse.salford.ac.uk/tools/TesseractOCRToPAGE>


## WebViewer
Visonneuse d'analyses de mise en page (layout) en HTML sur les scans des pages. Lecture du format PAGE.
```
python -m SimpleHTTPServer 8000 # depuis la racine du projet.
```
Ouvir le navigateur et entrer l'url : `localhost:8000/Layout/WebViewer`
