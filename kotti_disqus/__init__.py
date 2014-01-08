from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_disqus')


def kotti_configure(settings):

    settings['pyramid.includes'] += ' kotti_disqus'

    settings['kotti.available_types'] += ' kotti_disqus.resources.content_type'


def includeme(config):

    config.add_translation_dirs('kotti_disqus:locale')
    config.scan(__name__)
