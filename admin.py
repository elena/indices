from django.contrib import admin
from models import IndexSection, IndexApp, IndexCustom


class IndexSectionAdmin(admin.ModelAdmin):
    model = IndexSection
    save_on_top = True
    list_display = ['order','desc','helper_text']


class IndexAppAdmin(admin.ModelAdmin):
    model = IndexApp
    save_on_top = True
    #list_display = [ 'section_order', 'section','order','header']
    list_display = ['header', 'section','order']


class IndexCustomAdmin(admin.ModelAdmin):
    model = IndexCustom
    save_on_top = True
    #list_display = [ 'model', 'app.section.order', 'app.order', 'order', 'app.section', 'app', 'shaded']
    list_display = [ 'model', 'order', 'app', 'alt_name', 'shaded']



admin.site.register(IndexSection, IndexSectionAdmin)
admin.site.register(IndexApp, IndexAppAdmin)
admin.site.register(IndexCustom, IndexCustomAdmin)


