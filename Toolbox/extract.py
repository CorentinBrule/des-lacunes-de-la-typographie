# coding: utf8
## Test sequence
from xml.dom import minidom
from PIL import Image
import re,operator
# import extract,re
# xml = minidom.parse("../Layout/T2P-layout-glyphs/ocr-p336.xml")
#imgPage = Image.open("../Pages/p336.png")
#node = xml.getElementsByTagName("Glyph")[0]

def margin(coord,w=2,h=2,W=2,H=2):
        coord[0][0] -= w
        coord[0][1] -= h
        coord[1][0] += W
        coord[1][1] += H
        return coord

def getCoords(node):
    coords = node.getElementsByTagName('Coords')[0].getAttribute('points')
    coords = coords.split(' ')
    coordCrop = []

    if "Glyph" in node.tagName :
        coordCrop = [coords[0].split(','),coords[2].split(',')]
        for c in coordCrop:
            c[0] = int(c[0])
            c[1] = int(c[1])

    else :
        coordsTmp = []
        for i,c in enumerate(coords):
            coordsTmp.append(c.split(','))
            coordsTmp[i][0] = int(coordsTmp[i][0])
            coordsTmp[i][1] = int(coordsTmp[i][1])

        minX = sorted(coordsTmp,key=operator.itemgetter(0))[0][0]
        maxX = sorted(coordsTmp,key=operator.itemgetter(0))[-1][0]
        minY = sorted(coordsTmp,key=operator.itemgetter(1))[0][1]
        maxY = sorted(coordsTmp,key=operator.itemgetter(1))[-1][1]
        coordCrop.append([minX,minY])
        coordCrop.append([maxX,maxY])

    #print(coordCrop)
    return coordCrop

def test(stri):
    print(re.findall("c",stri))

def findElementById(xml,id):
    tags = ["Page","TextRegion","TextLine","Word","Glyph"]
    t = id[0]
    if "p" in id : tag = tags[0]
    if "r" in id : tag = tags[1]
    if "l" in id : tag = tags[2]
    if "w" in id : tag = tags[3]
    if "c" in id : tag = tags[4]

    ls = xml.getElementsByTagName(tag)

    for i in ls:
        if i.getAttribute("id") == id:
            return i

def extract(imgPage,node):
    pageNode = node
    print(pageNode)
    while "Page" not in pageNode.tagName:
        pageNode = pageNode.parentNode

    pageNum = re.findall(r"\d+",pageNode.getAttribute("imageFilename"))[0] #extract digit

    char=""
    #get glyph's name (char)
    if node.tagName == "Glyph":
        char = node.getElementsByTagName('Unicode')[0].firstChild.nodeValue
    idNode = node.getAttribute("id")
    #unicodeChars.append(char)
    # get glyph's coords (and parse from xml)
    coordCrop = getCoords(node)

    #textLine = node.parentNode.parentNode #get the textLine parent balise

    # margining
    coordCrop = margin(coordCrop)

    # crop the image of in the glyph in the image of the page
    area = imgPage.crop((coordCrop[0][0],coordCrop[0][1],coordCrop[1][0],coordCrop[1][1]))
    outputName = char+pageNum+"-"+idNode+".png";
    #area.save(folderOutputPath+char+pageNum+"-"idGlyph+".png")
    return area,outputName

if __name__ == "__main__": #no working
    from xml.dom import minidom
    from PIL import Image
    import re,os
    xml = minidom.parse("../Layout/T2P-layout-glyphs/ocr-p336.xml")
    imgPage = Image.open("../Pages/p336.png")
    #nodes = xml.getElementsByTagName("Glyph")
    node = xml.getElementsByTagName("TextLine")[3]
    #print(findElementById(xml,"c4").getAttribute("id"))
    area,outputName = extract(imgPage,node)
    area.save("TEST-"+outputName)
    #os.system("pause")
    #print(test)
