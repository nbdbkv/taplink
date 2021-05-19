from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import TemplateView, FormView

from apps.taplink.forms import (
    TapLinkNickNameForm, TapLinkEditorForm, TapLinkAvatarForm,
    TapLinkMessengerForm
)
from .models import TapLink, TapLinkEditor, TapLinkMessenger


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/index.html'
    login_url = 'sign-in_page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nickname_form'] = TapLinkNickNameForm
        context['editor_form'] = TapLinkEditorForm
        context['avatar_form'] = TapLinkAvatarForm
        context['messenger_form'] = TapLinkMessengerForm
        context['taplink'] = TapLink.objects.filter(user=self.request.user)\
            .prefetch_related('messengers').prefetch_related('editors')
        return context


class TapLinkNickNameFormView(LoginRequiredMixin, FormView):
    template_name = 'pages/index.html'
    form_class = TapLinkNickNameForm

    def form_valid(self, form):
        taplink = TapLink.objects.filter(user=self.request.user).first()
        if form.cleaned_data["nickname"]:
            taplink.nickname = slugify(form.cleaned_data["nickname"])
        else:
            taplink.nickname = form.cleaned_data["nickname"]
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
            title_t=form.cleaned_data["title_t"],
            whatsapp=form.cleaned_data["whatsapp"],
            title_wa=form.cleaned_data["title_wa"],
        )
        return redirect('index_page')
