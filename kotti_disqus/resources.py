from kotti.interfaces import IDefaultWorkflow
from kotti.resources import Content
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from zope.interface import implements

from kotti_disqus import _


class content_type(Content):
    """My content type"""

    implements(IDefaultWorkflow)

    id = Column(
        Integer(),
        ForeignKey('contents.id'),
        primary_key=True
        )

    # Add additional columns here
    example_attribute = Column(
        Unicode()
        )

    type_info = Content.type_info.copy(
        name=u'content_type',
        title=_(u'Content Type'),
        add_view=u'add_content_type',
        addable_to=['Document', ],
        selectable_default_views=[
            ('alternative-view', _(u"Alternative View")),
            ],
        )

    def __init__(self, example_attribute=u"", **kwargs):

        super(content_type, self).__init__(**kwargs)

        self.example_attribute = example_attribute
