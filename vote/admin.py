from django.contrib import admin
from vote.models import Vote
from import_export.admin import ExportActionMixin

# Register your models here.
class VoteExport(ExportActionMixin, admin.ModelAdmin):
  list_display = ('currentDate', 'nome', 'turma', 'flor')

admin.site.register(Vote,VoteExport)