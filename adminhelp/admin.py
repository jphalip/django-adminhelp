from django.contrib import admin
from adminhelp.models import HelpPage, Topic

class HelpPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'path', 'topic', 'position')
    list_filter  = ('topic',)
    save_as = True

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')

admin.site.register(HelpPage, HelpPageAdmin)
admin.site.register(Topic, TopicAdmin)
