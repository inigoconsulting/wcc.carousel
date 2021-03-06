from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder
from wcc.carousel.validators import DexterityImageSizeValidator
from wcc.carousel import MessageFactory as _
from wcc.carousel.interfaces import ICarouselImageEnabled

class ICarouselImage(form.Schema, ICarouselImageEnabled):
    """
       Marker/Form interface for Carousel Image
    """

    form.fieldset('settings',
        label=_(u'Settings'),
        fields=['carousel_image', 'carousel_title', 'carousel_description']
    )

    # -*- Your Zope schema definitions here ... -*-
    carousel_image = namedfile.NamedBlobImage(
        title=_(u'Slider image'),
        description=_(u'Upload carousel image.'),
        required=False
    )

    carousel_title = schema.TextLine(
        title=_(u'Slider title'),
        description=_(u'If set, the slider will use this title instead'
                    ' of the content title'),
        required=False
    )

    carousel_description = schema.TextLine(
        title=_(u'Slider description'),
        description=_(u'Text to display below title on slider'),
        required=False
    )


@form.validator(field=ICarouselImage['carousel_image'])
def validateCarouselImage(value):
    if not value:
        return True
    validator = DexterityImageSizeValidator()
    validator.validate(value)
    return True

alsoProvides(ICarouselImage,IFormFieldProvider)

class CarouselImage(object):
    """
       Adapter for Carousel Image
    """
    implements(ICarouselImage)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
