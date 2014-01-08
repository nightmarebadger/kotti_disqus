# -*- coding: utf-8 -*-

from kotti.views.slots import assign_slot
from pyramid.view import view_config


@view_config(name="disqus_comments",
             renderer="kotti_disqus:templates/disqus_comments.pt")
def disqus_comments_view(context, request):
    return {}


def includeme(config):
    assign_slot('disqus_comments', 'belowcontent')
