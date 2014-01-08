# -*- coding: utf-8 -*-

from colander import SchemaNode
from colander import String
from kotti.views.edit.content import ContentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_disqus import _
from kotti_disqus.resources import content_type
from kotti_disqus.fanstatic import kotti_disqus


class content_typeSchema(ContentSchema):
    """Schema for add / edit forms of content_type"""

    example_attribute = SchemaNode(
        String(),
        title=_(u'Example Attribute'),
        missing=u"",
        )


@view_config(name=content_type.type_info.add_view,
             permission='add',
             renderer='kotti:templates/edit/node.pt')
class content_typeAddForm(AddFormView):

    schema_factory = content_typeSchema
    add = content_type
    item_type = _(u"content_type")


@view_config(name='edit',
             context=content_type,
             permission='edit',
             renderer='kotti:templates/edit/node.pt')
class content_typeEditForm(EditFormView):

    schema_factory = content_typeSchema


@view_defaults(context=content_type, permission='view')
class content_typeView(object):
    """View(s) for content_type"""

    def __init__(self, context, request):

        self.context = context
        self.request = request

    @view_config(name='view',
                 renderer='kotti_disqus:templates/content_type.pt')
    def view(self):

        kotti_disqus.need()

        return {}

    @view_config(name='alternative-view',
                 renderer='kotti_disqus:templates/content_type-alternative.pt')
    def alternative_view(self):

        return {}
