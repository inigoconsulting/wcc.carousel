from collective.grok import gs
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interfaces.link import IATLink
from Products.ATContentTypes.interfaces.event import IATEvent
# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade wcc.carousel to 1002',
                description=u'Upgrade wcc.carousel to 1002',
                source='1001', destination='1002',
                sortkey=1, profile='wcc.carousel:default')
def to1002(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.carousel.upgrades:to1002')

    catalog = getToolByName(context, 'portal_catalog')
    for brain in catalog(object_provides=IATLink.__identifier__):
        obj = brain.getObject()
        obj.reindexObject()

    for brain in catalog(object_provides=IATEvent.__identifier__):
        obj = brain.getObject()
        obj.reindexObject()

@gs.upgradestep(title=u'Upgrade wcc.carousel to 1001',
                description=u'Upgrade wcc.carousel to 1001',
                source='1', destination='1001',
                sortkey=1, profile='wcc.carousel:default')
def to1001(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.carousel.upgrades:to1001')
