from five import grok
from Products.ATContentTypes.interface import IATContentType
grok.templatedir('templates')

class DefaultTile(grok.View):
    grok.context(IATContentType)
    grok.template('default_tile')
    grok.name('wcc-featured-view')
