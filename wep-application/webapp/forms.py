from django import forms
from django.utils.translation import ugettext_lazy as _

from webapp.models import Feedback, OrderOfMaster, Subscriber, News


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'phone', 'message', 'service')

    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'uk-input popInput', 'placeholder': _('Имя')}))
    phone = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'uk-input popInput', 'placeholder': 'Телефон'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'uk-textarea popArea', 'placeholder': _('Напишите свой вопрос или пожелание')}))
    service_slug = forms.SlugField(required=False, widget=forms.TextInput(attrs={'class': 'uk-hidden'}))


class MasterForm(forms.ModelForm):
    class Meta:
        model = OrderOfMaster
        fields = ('name', 'phone')


class SubscriberForm(forms.ModelForm):
    email = forms.EmailField(max_length=100, required=True,
                             widget=forms.EmailInput(attrs={'class': 'uk-input footerInput', 'placeholder': 'e-mail'}))

    class Meta:
        model = Subscriber
        fields = ('email',)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ()

    send_to_subscribers = forms.BooleanField()
