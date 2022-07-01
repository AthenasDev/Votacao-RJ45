from django.contrib import admin
from .models import Alunos

# Register your models here.

class AlunosAdmin(admin.ModelAdmin):
  list_display = ['nome', 'matricula', 'voto_rei', 'voto_rainha', 'statusvoto']
admin.site.register(Alunos, AlunosAdmin)