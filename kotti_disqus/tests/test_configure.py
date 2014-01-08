from pyramid.interfaces import ITranslationDirectories

from kotti_disqus import includeme
from kotti_disqus import kotti_configure


def test_kotti_configure():

    settings = {
        'kotti.available_types': '',
        'pyramid.includes': '',
        }

    kotti_configure(settings)

    assert settings['pyramid.includes'] == ' kotti_disqus'
    assert settings['kotti.available_types'] == ' kotti_disqus.resources.content_type'


def test_includeme(config):

    includeme(config)

    utils = config.registry.__dict__['_utility_registrations']
    k = (ITranslationDirectories, u'')

    # test if the translation dir is registered
    assert k in utils
    assert utils[k][0][0].find('kotti_disqus/locale') > 0
