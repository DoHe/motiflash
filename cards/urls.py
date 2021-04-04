from django.urls import path

from cards.views import Index, Cards, Courses

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('cards/', Cards.as_view(), name='cards'),
    path('courses/', Courses.as_view(), name='courses')
]
