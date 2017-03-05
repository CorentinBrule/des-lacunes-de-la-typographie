# !/usr/bin/env python


#import sys
#sys.path.append('/usr/share/inkscape/extensions') # or another path, as necessary
#   U t i l i s a t i o n   du  module   i n k e x   avec   des   e f f e t s   p r e d e f i n i s
import inkex
from simplestyle import *
class Project(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)

        # Define string option "--what" with "-w" shortcut and default value "World".
        self.OptionParser.add_option('-w', '--how', action = 'store',
          type = 'int', dest = 'how', default = 30,
          help = 'What would you like to greet')

    def effect(self):

        # Get script's "--what" option value.
        how = self.options.how

        svg = self.document.getroot()

        # Again, there are two ways to get the attibutes:
        width  = self.unittouu(svg.get('width'))
        height = self.unittouu(svg.attrib['height'])

        # Create a new layer.
        layer = inkex.etree.SubElement(svg, 'g')
        layer.set(inkex.addNS('label', 'inkscape'), 'Hello %s Layer' % str(how))
        layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')

        # Create text element
        #text = inkex.etree.Element(inkex.addNS('text','svg'))
        #text.text = 'Hello %s!' % str(how)
        


        # Set text position to center of document.
        text.set('x', str(width / 2))
        text.set('y', str(height / 2))

        # Center text horizontally with CSS style.
        style = {'text-align' : 'center', 'text-anchor': 'middle'}
        text.set('style', formatStyle(style))

        # Connect elements together.
        layer.append(text)

proj = Project()
proj.affect()
