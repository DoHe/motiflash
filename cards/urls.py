from django.urls import path

from cards.views import Index, Cards, Courses, CardAddView, SignUpView, ShareView, NotificationsView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('cards/', Cards.as_view(), name='cards'),
    path('courses/', Courses.as_view(), name='courses'),
    path('cards_add/', CardAddView.as_view(), name='cards_add'),
    path('share/', ShareView.as_view(), name='share'),
    path('notifications/', NotificationsView.as_view(), name='notifications'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
]
