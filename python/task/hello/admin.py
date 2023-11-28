from django.contrib import admin

# from .models import Question

#admin.site.register(Question)
# from .models import FirstModel, SecondModel

# admin.site.register(FirstModel)
# admin.site.register(SecondModel)
from .models import Currency, Product

admin.site.register(Currency)
admin.site.register(Product)