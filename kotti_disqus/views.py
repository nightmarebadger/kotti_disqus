# -*- coding: utf-8 -*-

from kotti import get_settings
from kotti.views.slots import assign_slot
from pyramid.exceptions import PredicateMismatch
from pyramid.util import DottedNameResolver
from pyramid.view import view_config


@view_config(name="disqus_comments",
             renderer="kotti_disqus:templates/disqus_comments.pt")
def disqus_comments_view(context, request):
    available = get_settings().get('kotti_disqus.available_types', '').split()
    resolver = DottedNameResolver(None)
    types = tuple(resolver.resolve(typ) for typ in available)

    if not isinstance(context, types):
        raise PredicateMismatch()

    return {}


def includeme(config):
    assign_slot('disqus_comments', 'belowcontent')
