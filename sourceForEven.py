# coding: utf8

from flat import font, text, strike, document, view
import bs4 as BeautifulSoup

with open('/home/macrico/Documents/enCours/des-lacunes-de-la-typographie/Book/book.html','r') as f: 
    soup = BeautifulSoup.BeautifulSoup(f.read(), "html.parser")
    
print(soup.body.findAll()[1])
    
def layout(author, title, *paragraphs):
    # Vollkorn by Friedrich Althausen
    # http://friedrichalthausen.de/vollkorn/
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

doc = layout(u"Vitruévius", u"Ten Books on Architecture",
    u"Chapter I \u2014 The Education of the Architect", "",
    ("1. The architect should be equipped with knowledge of many branches of "
        "study and varied kinds of learning, for it is by his judgement that all "
        "work done by the other arts is put to test. This knowledge is the child "
        "of practice and theory. Practice is the continuous and regular exercise "
        "of employment where manual work is done with any necessary material "
        "according to the design of a drawing. Theory, on the other hand, is the "
        "ability to demonstrate and explain the productions of dexterity on the "
        "principles of proportion."), "",
    ("2. It follows, therefore, that architects who have aimed at acquiring "
        "manual skill without scholarship have never been able to reach a "
        "position of authority to correspond to their pains, while those who "
        "relied only upon theories and scholarship were obviously hunting the "
        "shadow, not the substance. But those who have a thorough knowledge of "
        "both, like men armed at all points, have the sooner attained their "
        "object and carried authority with them."), "",
    ("3. In all matters, but particularly in architecture, there are these two "
        u"points:\u2014the thing signified, and that which gives it its significance. "
        "That which is signified is the subject of which we may be speaking; and "
        "that which gives significance is a demonstration on scientific "
        "principles. It appears, then, that one who professes himself an "
        "architect should be well versed in both directions. He ought, therefore, "
        "to be both naturally gifted and amenable to instruction. Neither natural "
        "ability without instruction nor instruction without natural ability can "
        "make the perfect artist. Let him be educated, skilful with the pencil, "
        "instructed in geometry, know much history, have followed the "
        "philosophers with attention, understand music, have some knowledge of "
        "medicine, know the opinions of the jurists, and be acquainted with "
        "astronomy and the theory of the heavens."))

view(doc.pdf())