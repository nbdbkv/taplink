from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import TemplateView, FormView

from apps.taplink.forms import (
    PathNameForm, EditorForm, AvatarForm,
    MessengerForm
)
from .models import TapLink, Editor, Messenger


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/index.html'
    login_url = 'sign-in_page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pathname_form'] = PathNameForm
        context['editor_form'] = EditorForm
        context['avatar_form'] = AvatarForm
        context['messenger_form'] = MessengerForm
        context['taplink'] = TapLink.objects.filter(
            user=self.request.user
        ).prefetch_related('messengers', 'editors')
        return context


class PathNameFormView(LoginRequiredMixin, FormView):
    template_name = 'pages/index.html'
    form_class = PathNameForm

    def form_valid(self, form):
        taplink = TapLink.objects.filter(user=self.request.user).first()
        if form.cleaned_data["pathname"]:
            taplink.pathname = slugify(form.cleaned_data["pathname"])
        else:
            taplink.pathname = form.cleaned_data["pathname"]
        taplink.save()
        return redirect('index_page')


class EditorFormView(LoginRequiredMixin, FormView):
    template_name = 'pages/index.html'
    form_class = EditorForm

    def form_valid(self, form):
        taplink = TapLink.objects.filter(user=self.request.user).first()
        Editor.objects.create(
            taplink=taplink,
            editor=form.cleaned_data["editor"],
        )
        return redirect('index_page')


class AvatarFormView(LoginRequiredMixin, FormView):
    template_name = 'pages/index.html'
    form_class = AvatarForm

    def form_valid(self, form):
        taplink = TapLink.objects.filter(user=self.request.user).first()
        taplink.avatar = form.cleaned_data["avatar"]
        taplink.save()
        return redirect('index_page')


class MessengerFormView(LoginRequiredMixin, FormView):
    template_name = 'pages/index.html'
    form_class = MessengerForm
    success_url = reverse_lazy('index_page')

    def form_valid(self, form):
        taplink = TapLink.objects.filter(user=self.request.user).first()
        Messenger.objects.create(
            taplink=taplink,
            telegram=form.cleaned_data["telegram"],
            title_t=form.cleaned_data["title_t"],
            whatsapp=form.cleaned_data["whatsapp"],
            title_wa=form.cleaned_data["title_wa"],
        )
        return redirect('index_page')
