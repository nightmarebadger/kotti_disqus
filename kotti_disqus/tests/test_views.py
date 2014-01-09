from kotti import get_settings
from kotti.resources import Document
from kotti.resources import get_root
from kotti.resources import Image
from kotti_settings.util import set_setting
from pyramid.exceptions import PredicateMismatch

from kotti_disqus import kotti_configure
from kotti_disqus.views import disqus_comments_view


def test_views(db_session, dummy_request):

    root = get_root()
    root['test-document'] = Document()
    root['test-image'] = Image()

    # Setup
    kotti_configure(get_settings())

    # Is shown on Document with the default URL if we do not set it
    set_setting('disqus_shortname', 'test_shortname')
    set_setting('disqus_base_url', '')
    assert disqus_comments_view(root['test-document'], dummy_request) == \
        {
            'disqus_url': 'http://example.com/test-document/',
            'disqus_shortname': 'test_shortname'
        }

    # If we set the URL, it overrides the default one
    set_setting('disqus_base_url', 'http://testing.com/')
    assert disqus_comments_view(root['test-document'], dummy_request) == \
        {
            'disqus_url': 'http://testing.com/test-document/',
            'disqus_shortname': 'test_shortname'
        }

    # Is not shown if we aren't on a Document object, raises PredicateMismatch
    try:
        disqus_comments_view(root['test-image'], dummy_request)
    except PredicateMismatch:
        pass
