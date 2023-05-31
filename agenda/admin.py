from django.contrib import admin
from agenda.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('compromisso','descricao','deadline')
    search_fields = ('deadline',)


admin.site.register(Task, TaskAdmin)