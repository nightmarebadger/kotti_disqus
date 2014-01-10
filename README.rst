Still in development, just some very basic work done.

============
kotti_disqus
============

This is an extension to the Kotti CMS that adds a commenting system to your
site. It uses `Disqus <http://disqus.com/>`_, so you need to register an
account there before you can use it.

`Find out more about Kotti`_

Setup
=====

To activate the ``kotti_disqus`` add-on in your Kotti site, you need to add an
entry to the ``kotti.configurators`` setting in your Paste Deploy config.  If
you don't have a ``kotti.configurators`` option, add one. ``kotti_disqus``
depends on ``kotti_settings`` so you need to add a line for this add-on too::

    kotti.configurators =
        kotti_settings.kotti_configure
        kotti_disqus.kotti_configure

You can choose on which types to enable the comments via the
``kotti_disqus.available_types`` setting, like this::

    kotti_disqus.available_types =
        kotti.resources.Document
        kotti.resources.Image

If you do not specify the types, it defaults to Kotti's ``Document`` and
``Image``.

There are two settings to adjust for the Disqus commenting system. You can
change them at the settings page (http://your.domain/@@settings or use the
submenu of "Site Setup").

+------------------+--------------------------------------------------------+
| Option           | Explanation                                            |
+==================+========================================================+
| Disqus Shortname | The shortname you registered at Disqus. Necessary for  |
|                  | the commenting system to work!                         |
+------------------+--------------------------------------------------------+
| Disqus Base URL  | A way to change the base URL - useful if you move your |
|                  | site to another URL but want to keep your comments.    |
|                  | Will use the current URL if not set.                   |
+------------------+--------------------------------------------------------+


.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
