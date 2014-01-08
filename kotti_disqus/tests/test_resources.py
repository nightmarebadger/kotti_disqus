from kotti.resources import get_root
from kotti.testing import DummyRequest

from kotti_disqus.resources import content_type


def test_content_type(db_session, config):
    config.include('kotti_disqus')

    root = get_root()
    content = content_type()
    assert content.type_info.addable(root, DummyRequest()) is True
    root['content'] = content
