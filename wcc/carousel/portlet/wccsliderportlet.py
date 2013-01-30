from zope import schema
from zope.component import getMultiAdapter
from AccessControl import getSecurityManager
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from wcc.carousel import MessageFactory as _
from plone.app.vocabularies.catalog import SearchableTextSourceBinder

from plone.app.form.widgets.uberselectionwidget import UberMultiSelectionWidget
from wcc.carousel.interfaces import ICarouselImageEnabled

class IWCCSliderPortlet(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    items = schema.List(
        title=_(u'Items to display'),
        required=True,
        value_type=schema.Choice(
            source=SearchableTextSourceBinder(
                {'object_provides': ICarouselImageEnabled.__identifier__},
                default_query='path:'
            )
        )
    )

class Assignment(base.Assignment):
    implements(IWCCSliderPortlet)

    items = []

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def title(self):
        return _('WCC Slider Portlet')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/wccsliderportlet.pt')

    @property
    def available(self):
        return True

    def items(self):
        result = []
        for path in self.data.items:
            item = self._get_item(path)
            if item:
                result.append(item)
        return result

    def _get_item(self, path):
        if not path:
            return None

        if path.startswith('/'):
            path = path[1:]

        portal_state = getMultiAdapter((self.context, self.request),
                name=u'plone_portal_state')

        portal = portal_state.portal()

        if isinstance(path, unicode):
            path = str(path)

        result = portal.unrestrictedTraverse(path, default=None)

        if result is not None:
            sm = getSecurityManager()
            if not sm.checkPermission('View', result):
                result = None

        return result

    def get_tile(self, obj):
        tile = obj.unrestrictedTraverse("wcc-featured-view")
        if tile is None:
            return ''
        return tile()


class AddForm(base.AddForm):
    form_fields = form.Fields(IWCCSliderPortlet)
    form_fields['items'].custom_widget = UberMultiSelectionWidget
    label = _(u"Add WCC Slider Portlet")
    description = _(u"")

    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    form_fields = form.Fields(IWCCSliderPortlet)
    form_fields['items'].custom_widget = UberMultiSelectionWidget
    label = _(u"Edit WCC Slider Portlet")
    description = _(u"")
