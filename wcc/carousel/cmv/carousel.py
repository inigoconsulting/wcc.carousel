from five import grok
from collective.portlet.collectionmultiview import BaseRenderer
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from wcc.carousel import MessageFactory as _
import binascii

class CarouselRenderer(BaseRenderer):
    title = _(u'WCC Frontpage Slideshow')
    template = ViewPageTemplateFile('templates/carousel.pt')

    def get_tile(self, obj):
        tile = obj.unrestrictedTraverse("wcc-featured-view")
        if tile is None:
            return ''
        return tile()
