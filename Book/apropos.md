Ces fichiers sont compilés à partir des sources présentes à la racine du projet.

# Pandoc :

* md -> pdf : `pandoc TYPOGRAPHIE-JBAMarcellinJobard-1842-p336_356.md --latex-engine=xelatex -o Book/book.pdf`
* md -> html : `pandoc TYPOGRAPHIE-JBAMarcellinJobard-1842-p336_356.md -s -o Book/book.html`

## problèmes :

* avec les images inline : `pandoc source-inlineImages.md --latex-engine=xelatex -o Book/book-inlineImages.pdf`
les images  ne s'affichent pas dans l'export pdf ! Ni avec la syntaxe image HTML : `<img src="../Glyphes/specialChar/special3.png" alt="special3" style="width:1.2em;height:auto;"/>` ni avec la syntaxe image MarkDown : `![special2](../Glyphes/specialChar/special2.png){.encoreClasse #encoreId width=1.2em height=auto}`
(alors que nickel avec l'html : `pandoc source-inlineImagesHTML.md -s -o Book/book-inlineImages.html`)

# Even :

"sourceForEven.py" avec [Even](http://xxyxyz.org/even/), IDE graphique de la librairie [Flat](http://xxyxyz.org/flat)
