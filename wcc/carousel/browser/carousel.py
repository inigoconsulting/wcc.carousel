from five import grok
from Products.ATContentTypes.interface import IATContentType
from wcc.carousel.interfaces import ICarouselImageEnabled
grok.templatedir('templates')

class DefaultTile(grok.View):
    grok.context(IATContentType)
    grok.template('default_tile')
    grok.name('wcc-featured-view')


class CarouselImageTile(grok.View):
    grok.template('carousel_image_tile')
    grok.name('wcc-featured-view')
    grok.context(ICarouselImageEnabled)
