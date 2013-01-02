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
        fields=['carousel_image']
    )

    # -*- Your Zope schema definitions here ... -*-
    carousel_image = namedfile.NamedBlobImage(
        title=_(u'Carousel Image'),
        description=_(u'Upload carousel image. Required size is 550x290px'),
        required=False
    )

@form.validator(field=ICarouselImage['carousel_image'])
def validateCarouselImage(value):
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
