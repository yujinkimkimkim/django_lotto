from django.contrib import admin

from .models import GuessNumbers
# 자신이 속한 폴더 내 models를 갖고 오고 싶다는 의미로 .models라고만 해도 됨
# Register your models here.
admin.site.register(GuessNumbers)