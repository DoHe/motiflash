from django.contrib import admin
from django.urls import include, path

from cards.views import Index, Cards

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cards.urls'))
]
