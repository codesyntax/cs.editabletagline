__version__ = '$Id: tagline.py 9335 2008-02-04 16:25:14Z lur $'

from zope.component import adapts
from zope.interface import implements
from zope.formlib import form

from plone.app.controlpanel.form import ControlPanelForm
from plone.app.layout.viewlets.common import ViewletBase

try:
    from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget
    KUPU_WIDGET = True
except ImportError:
    KUPU_WIDGET = False



from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.utils import safe_unicode
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFCore.utils import getToolByName

from cs.editabletagline import EditableTaglineMessageFactory as _
from cs.editabletagline.interfaces import IEditableTagline
class EditableTaglineControlPanelAdapter(SchemaAdapterBase):
    adapts(IPloneSiteRoot)
    implements(IEditableTagline)

    def __init__(self, context):
        super(EditableTaglineControlPanelAdapter, self).__init__(context)
        self.portal = context
        pprop = getToolByName(self.portal, 'portal_properties')
        self.context = pprop.site_properties
        self.encoding = pprop.site_properties.default_charset
        self.fprops = pprop.tagline_properties

    def get_tagline_text(self):
	language = self.portal.REQUEST.get('LANGUAGE', '')
	ida='tagline_text_' + language
        text = getattr(self.fprops, ida, u'')
        return safe_unicode(text)
        
    def set_tagline_text(self, value):
	language = self.portal.REQUEST.get('LANGUAGE', '')
	ida='tagline_text_' + language
	if value is not None:
	    value=value.encode(self.encoding)
	else:
	    value=''
	    
	if self.fprops.hasProperty(ida):
	    setattr(self.fprops, ida, value)
	else:
	    self.fprops.manage_addProperty(ida,value,'text')


    tagline_text = property(get_tagline_text, set_tagline_text)



class EditableTaglineControlPanel(ControlPanelForm):
    form_fields = form.FormFields(IEditableTagline)

    if KUPU_WIDGET:
        form_fields['tagline_text'].custom_widget = WYSIWYGWidget

    form_name = _(u'Editable tagline')
    label = _(u'Editable tagline content')
    description = _(u'Enter the content of the tagline')


class EditableTaglineViewlet(ViewletBase):

    def update(self):
	language = self.request.get('LANGUAGE', '')
	ida='tagline_text_' + language
        pprops = getToolByName(self.context, 'portal_properties')
        fprops = pprops.tagline_properties
        text = getattr(fprops, ida, u'')
        self.tagline_text = safe_unicode(text)

    render = ViewPageTemplateFile('tagline.pt')

    
    
 
