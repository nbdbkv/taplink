from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from apps.taplink.forms import (
    TapLinkURLForm, TapLinkEditorForm, TapLinkAvatarForm, TapLinkMessengerForm
)
from .models import TapLink, TapLinkEditor, TapLinkMessenger


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/index.html'
    login_url = 'sign-in_page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_form'] = TapLinkURLForm
        context['editor_form'] = TapLinkEditorForm
        context['avatar_form'] = TapLinkAvatarForm
        context['messenger_form'] = TapLinkMessengerForm
        context['object'] = TapLink.objects.get(user=self.request.user)
        return context


class TapLinkURLFormView(LoginRequiredMixin, FormView):
    template_name = 'pages/index.html'
    form_class = TapLinkURLForm

    def form_valid(self, form):
        taplink = TapLink.objects.filter(user=self.request.user).first()
        taplink.url = form.cleaned_data["url"]
        taplink.save()
        return redirect('index_page')


class TapLinkEditorFormView(LoginRequiredMixin, FormView):
    template_name = 'pages/index.html'
    form_class = TapLinkEditorForm

    def form_valid(self, form):
        taplink = TapLink.objects.filter(user=self.request.user).first()
        TapLinkEditor.objects.create(
            taplink=taplink,
            editor=form.cleaned_data["editor"],
        )
        return redirect('index_page')


class TapLinkAvatarFormView(LoginRequiredMixin, FormView):
    template_name = 'pages/index.html'
    form_class = TapLinkAvatarForm

    def form_valid(self, form):
        taplink = TapLink.objects.filter(user=self.request.user).first()
        taplink.avatar = form.cleaned_data["avatar"]
        taplink.save()
        return redirect('index_page')


class TapLinkMessengerFormView(LoginRequiredMixin, FormView):
    template_name = 'pages/index.html'
    form_class = TapLinkMessengerForm
    success_url = reverse_lazy('index_page')

    def form_valid(self, form):
        taplink = TapLink.objects.filter(user=self.request.user).first()
        TapLinkMessenger.objects.create(
            taplink=taplink,
            telegram=form.cleaned_data["telegram"],
            whatsapp=form.cleaned_data["whatsapp"],
        )
        return redirect('index_page')
