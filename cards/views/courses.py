from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, View

from cards.forms import CourseForm, ShareForm
from cards.models import Card, Course


class Courses(LoginRequiredMixin, FormView):
    template_name = "courses.html"
    form_class = CourseForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_has_access = (
            Q(owner=self.request.user) |
            Q(access=self.request.user)
        )
        context['courses'] = Course.objects.filter(user_has_access)
        return context

    def form_valid(self, form):
        import_text = form.cleaned_data.pop("import_text")
        form.cleaned_data["owner"] = self.request.user
        course = Course(**form.cleaned_data)
        course.save()
        if import_text:
            for (term, definition) in import_text:
                card = Card(term=term, definition=definition, course=course)
                card.save()
        return super().form_valid(form)


class ShareView(LoginRequiredMixin, FormView):
    template_name = "share.html"
    form_class = ShareForm
    success_url = reverse_lazy('courses')

    def form_valid(self, form):
        course = Course.objects.get(
            id=self.request.GET.get('course')
        )
        for user in form.cleaned_data.get("user", []):
            course.access.add(user)
        course.save()
        return super().form_valid(form)


class CourseDoneView(LoginRequiredMixin, View):

    def get(self, request):
        status = "ok"
        print(request.GET.get('id'))
        return JsonResponse({
            "status": status
        })
