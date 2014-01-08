from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_disqus')


def kotti_configure(settings):

    settings['pyramid.includes'] += ' kotti_disqus'


def includeme(config):
    config.add_translation_dirs('kotti_disqus:locale')
    config.scan(__name__)
