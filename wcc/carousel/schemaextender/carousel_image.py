from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from Products.Archetypes import atapi
from Products.ATContentTypes.interfaces import IATContentType
from zope.interface import Interface
from five import grok
from wcc.carousel.interfaces import IProductSpecific, ICarouselImageEnabled
from wcc.carousel import MessageFactory as _
from wcc.carousel.validators import ArchetypeImageSizeValidator

# Visit http://pypi.python.org/pypi/archetypes.schemaextender for full 
# documentation on writing extenders

class ExtensionImageField(ExtensionField, atapi.ImageField):
    pass

class ExtensionStringField(ExtensionField, atapi.StringField):
    pass


class CarouselImage(grok.Adapter):

    # This applies to all AT Content Types, change this to
    # the specific content type interface you want to extend
    grok.context(ICarouselImageEnabled)
    grok.name('wcc.carousel.carousel_banner')

    grok.implements(IOrderableSchemaExtender, IBrowserLayerAwareExtender)
    grok.provides(IOrderableSchemaExtender)

    layer = IProductSpecific

    fields = [
        # add your extension fields here
        ExtensionImageField('carousel_image',
            required=0,
            languageIndependent = 1,
            pil_quality = 100,
            validators=(ArchetypeImageSizeValidator(),),
            storage = atapi.AttributeStorage(),
            schemata='settings',
            widget = atapi.ImageWidget(
                label = _(u'Slider image'),
                description = _(u'Upload sliderimage.')
            )
        ),

        ExtensionStringField('carousel_title',
            required=0,
            storage = atapi.AttributeStorage(),
            schemata='settings',
            widget = atapi.StringField._properties['widget'](
                label=_(u'Slider title'),
                description=_(u'If set, the slider will use this title instead'
                                ' of the content title')
            )
        ),

        ExtensionStringField('carousel_description',
            required=0,
            storage = atapi.AttributeStorage(),
            schemata='settings',
            widget = atapi.StringField._properties['widget'](
                label=_(u'Slider description'),
                description=_(u'Text to display below title on slider'),
            )
        )
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

    def getOrder(self, schematas):
        # you may reorder the fields in the schemata here
        return schematas
