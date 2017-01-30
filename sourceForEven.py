# coding: utf8

from flat import font, text, strike, document, view
import bs4

with open('/home/macrico/Documents/enCours/des-lacunes-de-la-typographie/Book/book.html','r') as f: 
    soup = bs4.BeautifulSoup(f.read(), "html.parser") #open in utf8?
    
truc = soup.body.findAll()
#print(truc[0])
test = soup.body
print(test.contents[3].contents)
print(test.contents[3].contents[0].encode("utf8"))
print(test.contents[3].contents[1].contents[0].encode("utf8"))
print(test.contents[3].contents[1].name)
for c in test.children:
    print(c)
#print(truc.encode("utf8"))

def layout(author, title, *paragraphs):

    regular = font.open("/home/macrico/FONTS/Inknut-Antiqua/TTF-OTF/InknutAntiqua-Regular.ttf")
    bold = font.open("/home/macrico/FONTS/Inknut-Antiqua/TTF-OTF/InknutAntiqua-Bold.ttf")
    body = strike(regular).size(12, 16)
    headline = strike(bold).size(12, 16)
    story = text(
        body.paragraph(author),
        headline.paragraph(title),
        body.paragraph(""),
        *[body.paragraph(p) for p in paragraphs])
    
    doc = document(148, 210, "mm")
    page = doc.addpage()
    block = page.place(story).frame(18, 21, 114, 167)
    while block.overflow():
        page = doc.addpage()
        block = page.chain(block).frame(18, 21, 114, 167)
    return doc

doc = layout(u"JBAM-Jobard", u"Des lacunes de la typographie",test.contents[3].contents[0]+test.contents[3].contents[1].text)
    
    
view(doc.pdf())