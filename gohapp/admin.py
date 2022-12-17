from django.contrib import admin
from .models import FashionJewellery,PreciousJewellery,Orders,Contact
# Register your models here.
admin.site.register(FashionJewellery)
admin.site.register(PreciousJewellery)

admin.site.register(Orders)
admin.site.register(Contact)