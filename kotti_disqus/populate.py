from colander import MappingSchema
from colander import SchemaNode
from colander import Set
from colander import String
from deform.widget import CheckboxChoiceWidget
from kotti import get_settings

from kotti_disqus import _
from kotti_settings.util import add_settings


def populate_settings():

    def get_types():
        foo = get_settings()['kotti.available_types']
        bar = [(str(i)[8:-2], str(i)[8:-2]) for i in foo]
        return bar

    class DisqusShortnameSchemaNode(SchemaNode):
        name = 'disqus_shortname'
        title = _(u'Disqus shortname')
        description = _(u'The shortname with which you registered your site. '
                        u'Required for the commenting system to work!')
        missing = ''
        default = ''

    class DisqusBaseUrlSchemaNode(SchemaNode):
        name = 'disqus_base_url'
        title = _(u'Base URL')
        description = _(u'Base URL for Disqus commenting system. Useful if '
                        u'you move your site to another URL but want to keep '
                        u'comments. Defaults to current application URL.')
        missing = ''
        default = ''

    class DisqusAvailableTypesSchemaNode(SchemaNode):
        name = 'disqus_available_types'
        title = _(u'Available types')
        description = _(u'Select the types on which you want to enable '
                        u'comments')
        missing = []
        default = []
        widget = CheckboxChoiceWidget(values=get_types())

    class KottiDisqusSettingsSchema(MappingSchema):
        disqus_shortname = DisqusShortnameSchemaNode(String())
        disqus_base_url = DisqusBaseUrlSchemaNode(String())
        disqus_available_types = DisqusAvailableTypesSchemaNode(Set())

    KottiDisqusSettings = {
        'name': 'kotti_disqus_settings',
        'title': _(u'Disqus settings'),
        'description': _(u"Settings for kotti_disqus"),
        'success_message': _(u"Successfully saved Disqus settings."),
        'schema_factory': KottiDisqusSettingsSchema,
    }

    add_settings(KottiDisqusSettings)
