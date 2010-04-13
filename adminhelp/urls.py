from django.conf.urls.defaults import *
from adminhelp.views import help_index, help_page

help_index_url = url(
    regex=r'^$',
    view=help_index,
    name='help_index',
)

help_page_url = url(
    regex=r'^(?P<id>\d+)/$',
    view=help_page,
    name='help_page',
)

urlpatterns = patterns('', help_index_url, help_page_url)
