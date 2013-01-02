from collective.grok import gs
from wcc.carousel import MessageFactory as _

@gs.importstep(
    name=u'wcc.carousel', 
    title=_('wcc.carousel import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.carousel.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
