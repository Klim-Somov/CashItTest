from django import forms
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import logging

class ContactForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'medium-input',
            'placeholder': 'Ваше имя'
        }
    ))
    phone = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'type': 'tel',
            'class': 'medium-input',
            'placeholder': 'Телефон'
        }
    ))

    def send_email(self, request):
        title = 'Форма с сайта CashIt.ru'
        name = self.cleaned_data['name']
        phone = self.cleaned_data['phone']
        button = request.POST['button']
        logger = logging.getLogger('django')

        html = render_to_string(
            'mail/callback.html',
            {
                'name': name,
                'phone': phone,
                'button': button,
                'title': title
            }
        )
        res = send_mail(
            title,
            html,
            settings.EMAIL_SENDER,
            settings.EMAIL_RECIPIENT,
            fail_silently=True,
            html_message=html
        )
        if res:
            logger.info('Send email ' + name + ' ' + phone + ' ' + button)
            messages.success(request, 'С вами свяжутся в ближайшее время')
        else:
            logger.error('Send email error ' + name + ' ' + phone + ' ' + button)
            messages.error(request, 'Ошибка отправки')


class QuestionForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'medium-input',
            'placeholder': 'Ваше имя'
        }
    ))
    email = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'type': 'email',
            'class': 'medium-input',
            'placeholder': 'Ваш e-mail'
        }
    ))
    subject = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            'type': 'text',
            'class': 'medium-input',
            'placeholder': 'Ваш вопрос'
        }
    ))