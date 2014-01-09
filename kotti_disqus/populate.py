from colander import MappingSchema
from colander import SchemaNode
from colander import String

from kotti_disqus import _
from kotti_settings.util import add_settings


class DisqusShortnameSchemaNode(SchemaNode):
    name = 'disqus_shortname'
    title = _(u'Disqus shortname')
    description = _(u'The shortname you with which you registered your site. '
                    u'Required for the commenting system to work!')
    missing = ''
    default = ''


class DisqusBaseUrlSchemaNode(SchemaNode):
    name = 'disqus_base_url'
    title = _(u'Base URL')
    description = _(u'Base URL for Disqus commenting system. Useful if you '
                    u'move your site to another URL but want to keep '
                    u'comments. Defaults to current application URL.')
    missing = ''
    default = ''


class KottiDisqusSettingsSchema(MappingSchema):
    disqus_shortname = DisqusShortnameSchemaNode(String())
    disqus_base_url = DisqusBaseUrlSchemaNode(String())

KottiDisqusSettings = {
    'name': 'kotti_disqus_settings',
    'title': _(u'Disqus settings'),
    'description': _(u"Settings for kotti_disqus"),
    'success_message': _(u"Successfully saved Disqus settings."),
    'schema_factory': KottiDisqusSettingsSchema,
}


def populate_settings():
    add_settings(KottiDisqusSettings)
