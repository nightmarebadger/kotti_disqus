from kotti.resources import get_root

from kotti_disqus.resources import content_type
from kotti_disqus.views import content_typeView


def test_views(db_session, dummy_request):

    root = get_root()
    content = content_type()
    root['content'] = content

    view = content_typeView(root['content'], dummy_request)

    assert view.view() == {}
    assert view.alternative_view() == {}
