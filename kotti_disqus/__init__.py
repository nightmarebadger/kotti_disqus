from pyramid.i18n import TranslationStringFactory

import kotti_disqus

_ = TranslationStringFactory('kotti_disqus')


def kotti_configure(settings):

    settings['pyramid.includes'] += ' kotti_disqus'
    settings['kotti.populators'] += ' kotti_disqus.populate.populate_settings'

    settings['kotti_disqus.available_types'] = "kotti.resources.Document"


def includeme(config):
    config.add_translation_dirs('kotti_disqus:locale')
    config.scan(__name__)

    kotti_disqus.views.includeme(config)
