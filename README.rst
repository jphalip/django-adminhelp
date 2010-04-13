=================
Django Admin Help
=================

**Django Admin Help** is a pluggable help system for `Django Web Framework`_
to be used with administration application.

Admin Help was inspired by help system of `Django Grappelli`_.

.. _`Django Web Framework`: http://www.djangoproject.com
.. _`Django Grappelli`: http://django-grappelli.googlecode.com

Project page
    http://github.com/semente/django-adminhelp


Installing & Setup
==================

Admin Help is in the `Python Package Index (PyPI)`_ and you can easily install
the latest stable version of it using the tools ``pip`` or
``easy_install``. Try::

  pip install django-adminhelp

or::

  easy_install django-adminhelp

.. _`Python Package Index (PyPI)`: http://pypi.python.org


Alternatively, you can install Admin Help from source code running the follow
command on directory that contains the file ``setup.py``::

  python setup.py install

After installation you need configure your project to recognizes the Admin Help
application adding ``'adminhelp'`` to your ``INSTALLED_APPS`` setting and setup
the project *URLConf* like follow::

  urlpatterns = patterns('',
      # ...
      (r'^admin/help/', include('adminhelp.urls')), # put it before admin urls
      (r'^admin/', include(admin.site.urls)),
  )

*Don't forget to run the command syncdb.*

Admin Help also provides templates to show a "help" button on some admin
pages. You can setup the ModelAdmin you are interested like follow::

    class ExampleAdmin(admin.ModelAdmin):
        change_form_template = 'adminhelp/admin/change_form.html'
        change_list_template = 'adminhelp/admin/change_list.html'
        ...


Contributing
============

If you find any problems in the code or documentation, please take 30 seconds
to fill out a issue `here <http://github.com/semente/django-admihelp/issues>`_.

The contributing with code or translation is MUCH-APPRECIATED. You feel free to
fork or send patchs.

See AUTHORS file for a complete authors list of this application.

Thanks to `Interaction Consortium <http://interactionconsortium.com/>`_ for
sponsoring the project. Donate you too!


Copying conditions
==================

Django Admin Help is free software; you can redistribute it and/or modify it
under the terms of the `GNU Lesser General Public License`_ as published by the
Free Software Foundation; either version 3 of the License, or (at your option)
any later version.

Django Admin Help is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for
more details.

You should have received a copy of the GNU Lesser General Public License along
with this program; see the file COPYING.LESSER. If not, see
http://www.gnu.org/licenses/.

.. _`GNU Lesser General Public License`: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
