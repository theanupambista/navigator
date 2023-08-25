from django.contrib import admin

from building_name_generator.models import Chowk, District, Municipality, Province, Road, Wardnumber

# Register your models here.
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Municipality)
admin.site.register(Wardnumber)
admin.site.register(Road)
admin.site.register(Chowk)
