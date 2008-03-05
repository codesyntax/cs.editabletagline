from zope import schema
from zope.interface import Interface

from cs.editabletagline import EditableTaglineMessageFactory as _

class IProductLayer(Interface):
    """ Custom interface for our layer """

class IEditableTagline(Interface):
    """ The infterface for the editable footer """

    tagline_text = schema.Text(title=_(u'Tagline text'),
                              description=_(u'Insert here the HTML that will appear in the tagline'),
                              required=False,
                              )
