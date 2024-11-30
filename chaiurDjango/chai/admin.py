from django.contrib import admin
from .models import chaiReview ,ChaiVarity , ChaiCertificate , Store


# Register your models here.
class ChaiReviewInLine(admin.TabularInline):
    model = chaiReview 
    extra = 2


class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name' ,'type' ,  'date_added')
    inlines=[ChaiReviewInLine]

class StoreAdmin(admin.ModelAdmin):
    list_display=('name', 'location')
    filter_horizontal = ('chai_varities' ,)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display= ('chai' ,'issued_date')

admin.site.register(ChaiVarity , ChaiVarityAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)

