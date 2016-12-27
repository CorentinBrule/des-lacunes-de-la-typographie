var debPage = 336;
var finPage = 350;
selector = document.querySelector("#selectPage");
for (var page = debPage; page < finPage + 1; page++) {
    option = document.createElement('option');
    option.value = page;
    option.textContent = "page n°" + page;
    selector.appendChild(option);
    if (page == debPage) {
        option.selected = "selected"
    }
}

document.querySelector("#selectPage").addEventListener('change', function() {
    loadFile(this.value);
});

function loadFile(page) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            functXML(xhttp);
        }
    };
    xhttp.open("GET", "/Layout/T2P-layout-glyphs/ocr-p" + page + ".xml", true);
    xhttp.send();
}

function checkImage(self) {
    var div = self.value;
    if (self.checked) {
        document.querySelector("#" + div).style.display = "block";
    } else {
        document.querySelector("#" + div).style.display = "none";
    }
}

function checkBorders(self) {
    var divs = document.querySelectorAll("." + self.value);
    var len = divs.length;
    if (self.checked) {
        for (i = 0; i < len; i++) {
            divs[i].style.borderStyle = "solid";
        }
    } else {
        for (i = 0; i < len; i++) {
            divs[i].style.borderStyle = "none";
        }
    }
}

function checkText(self) {
    var divs = document.querySelectorAll("." + self.value);
    var len = divs.length;
    if (self.checked) {
        for (i = 0; i < len; i++) {
            divs[i].style.color = "black";
            divs[i].style.fontSize = "initial";
        }
    } else {
        for (i = 0; i < len; i++) {
            divs[i].style.color = "transparent";
            divs[i].style.fontSize = "0";
        }
    }
}



function functXML(xml) {
    var response = xml["response"];
    parser = new DOMParser();
    xmlDoc = parser.parseFromString(response, "text/xml");

    //imgpath = "https://raw.githubusercontent.com/CorentinBrule/des-lacunes-de-la-typographie/master/Pages/p336.png";
    imgpath = "/Pages/" + xmlDoc.querySelector("Page").getAttribute("imageFilename");
    imgdiv = document.querySelector('#imagePage');
    imgdiv.style.width = "";
    imgdiv.style.height = "";
    imgdiv.src = imgpath;

    var reduction;
    var originalSize = [];
    imgdiv.onload = function() {

        originalSize = [imgdiv.width, imgdiv.height];
        imgdiv.style.width = "100%";
        imgdiv.style.height = "auto";
        reduction = parseInt(originalSize[0]) / parseInt(imgdiv.offsetWidth);

        layoutdiv = document.querySelector('#layoutPage');
        while (layoutdiv.firstChild) {
            layoutdiv.removeChild(layoutdiv.firstChild);
        }

        tRs = xmlDoc.getElementsByTagName("TextRegion");

        for (i = 0, iLen = tRs.length; i < iLen; i++) {
            tR = xml2html(layoutdiv, tRs[i]);

            tLs = tRs[i].getElementsByTagName("TextLine");
            for (j = 0, jLen = tLs.length; j < jLen; j++) {
                tL = xml2html(tR, tLs[j])

                words = tLs[j].getElementsByTagName("Word");
                for (k = 0, kLen = words.length; k < kLen; k++) {
                    word = xml2html(tL, words[k])

                    glyphs = words[k].getElementsByTagName("Glyph");
                    for (l = 0, lLen = glyphs.length; l < lLen; l++) {
                        glyph = xml2html(word, glyphs[l])
                    }
                }
            }
        }

        layoutElements = layoutdiv.querySelectorAll("div");
        //console.log(layoutElements);
        for (i = 0; i < layoutElements.length; i++) {
            var element = layoutElements[i];

            coordsRaw = getCoords(element);
            caption = document.createElement("span");
            caption.innerHTML = String(coordsRaw);
            caption.className = "caption"
            element.appendChild(caption)
            offsetCoords = coords2offset(coordsRaw, element, reduction);

            element.style.left = String(offsetCoords[0] + "px");
            element.style.top = String(offsetCoords[1] + "px");
            element.style.width = String(offsetCoords[2] + "px");
            element.style.height = String(offsetCoords[3] + "px");

            // /!\ problème de z index avec les autres div, ne capte que les Glyphes car elles sont au dessus
            // /!\ problème avec les caption dans l'addEventListener car il sort tout le temps la même (utiliser e,this,target?)
            /*
            element.addEventListener("mouseover", function() {
                if (element.style.borderStyle == "solid") {
                    caption.style.display = "block";
                    console.log(caption);
                }
            });
            element.addEventListener("mouseout", function() {
                caption.style.display = "none";
            });*/
        }
    }

    function sortFunctionX(a, b) {
        return (a[0] - b[0]);
    }

    function sortFucntionY(a, b) {
        return (a[1] - b[1]);
    }

    function sortFunctionXY(a, b) {
        return (a[0] - b[0]) + (a[1] - b[1]);
    }

    function xml2html(parentNode, xmlelement) {
        var div = document.createElement('div');
        div.className = xmlelement.tagName;
        div.id = xmlelement.getAttribute("id");

        textEquivS = xmlelement.getElementsByTagName("Unicode")
        textEquiv = textEquivS[textEquivS.length - 1].textContent;
        div.textContent = textEquiv;

        if (xmlelement.getElementsByTagName("Coords")[0] != undefined) {
            div.appendChild(xmlelement.getElementsByTagName("Coords")[0]);
        }

        parentNode.appendChild(div);
        return (div);
    }

    function getCoords(element) {
        if (element.getElementsByTagName("Coords")[0] != undefined) {
            coords = element.getElementsByTagName("Coords")[0].getAttribute("points");
        } else {
            coords = "0,0 0,0"
        }

        coords = coords.split(' ');

        for (l in coords) {
            list = coords[l].split(',');
            for (c in list) {
                list[c][0] = parseInt(c[0]);
                list[c][1] = parseInt(c[1]);
            }
            coords[l] = list
        }

        //clone coords to sort
        var coordsSX = coords.slice();
        var coordsSY = coords.slice();

        coordsSX.sort(sortFunctionX)[0];
        coordsSY.sort(sortFucntionY)[0];
        coordCrop = [
            [coordsSX[0][0], coordsSY[0][1]],
            [coordsSX.reverse()[0][0], coordsSY.reverse()[0][1]]
        ];

        var xDiv = (coordCrop[0][0]);
        var yDiv = (coordCrop[0][1]);
        var wDiv = (coordCrop[1][0] - coordCrop[0][0]);
        var hDiv = (coordCrop[1][1] - coordCrop[0][1]);

        return coordsRaw = [xDiv, yDiv, wDiv, hDiv];
    }

    function coords2offset(coordsRaw, element, reduction) {
        var xDiv = coordsRaw[0] / reduction;
        var yDiv = coordsRaw[1] / reduction;
        var wDiv = coordsRaw[2] / reduction;
        var hDiv = coordsRaw[3] / reduction;

        var tmp = element;
        while (tmp.parentNode.id != "layoutPage") {
            tmp = tmp.parentNode;
            xDiv -= tmp.offsetLeft;
            yDiv -= tmp.offsetTop;
        }

        return (offset = [xDiv, yDiv, wDiv, hDiv])
    }

}
