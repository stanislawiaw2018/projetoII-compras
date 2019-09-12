from django.contrib import admin
from .models import *
# Register your models here.
class ComprasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'unidades', 'quant_mes',
                    'preco', 'preco_max')


admin.site.register(Compras,ComprasAdmin)
