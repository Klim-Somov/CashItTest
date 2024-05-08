from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, DetailView, TemplateView
from .forms import ContactForm
from .forms import QuestionForm
from .models import Blog
from django.template.loader import render_to_string


class IndexView(FormView):
    template_name = 'main/index.html'
    form_class = ContactForm

    def form_valid(self, form):
        # contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class TestView(FormView):
    template_name = 'main/test.html'
    form_class = ContactForm

    def form_valid(self, form):
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


# class FaqView(TemplateView):
#     template_name = 'main/faq.html'

#     def get(self, request, *args, **kwargs):
#         contact_form = ContactForm(self.request.GET or None)
#         question_form = QuestionForm(self.request.GET or None)
#         context = self.get_context_data(**kwargs)
#         context['contact_form'] = contact_form
#         context['question_form'] = question_form
#         return self.render_to_response(context)


# class FaqContactFormView(FormView):
#     form_class = ContactForm
#     template_name = 'main/faq.html'


# class FaqQuestionFormView(FormView):
#     form_class = QuestionForm
#     template_name = 'main/faq.html'


class NewIndexView(FormView):
    template_name = 'main/newindex.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.send_email(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

class PaymentView(FormView):
    template_name = 'main/features/payment.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

class AcquiringView(FormView):
    template_name = 'main/features/acquiring.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

class SalaryView(FormView):
    template_name = 'main/features/salary.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

class DonateView(FormView):
    template_name = 'main/features/donate.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

class TipsView(FormView):
    template_name = 'main/features/tips.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class BusinessView(FormView):
    template_name = 'main/business.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class TaxiView(FormView):
    template_name = 'main/business/taxi.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class DeliveryView(FormView):
    template_name = 'main/business/delivery.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class FreelanceView(FormView):
    template_name = 'main/business/freelance.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class RecyclingView(FormView):
    template_name = 'main/business/recycling.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class DealersView(FormView):
    template_name = 'main/business/autodealers.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class RealtorsView(FormView):
    template_name = 'main/business/realtors.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class OthersView(FormView):
    template_name = 'main/business/others.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class AnyBusinessView(FormView):
    template_name = 'main/business/any-business.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class SelfView(FormView):
    template_name = 'main/self.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class ServiceView(FormView):
    template_name = 'main/service.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class PolicyView(FormView):
    template_name = 'main/policy.html'
    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class BlogView(ListView):
    model = Blog
    template_name = 'main/blog.html'
    context_object_name = 'articles'
    ordering = ['-created_at']

    form_class = ContactForm

    def form_valid(self, form):
        contact(self.request)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class ArticleView(DetailView):
    model = Blog
    template_name = 'main/article.html'


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            html = render_to_string(
                'mail/callback.html',
                {
                    'name': form.cleaned_data.get('name', ''),
                    'phone': form.cleaned_data.get('phone', ''),
                    'email': form.cleaned_data.get('email', ''),
                    'button': form.cleaned_data.get('button', ''),
                }
            )
            mail = send_mail('Заявка с сервиса Cash&IT', html, settings.EMAIL_SENDER,
                             settings.EMAIL_RECIPIENT, fail_silently=True, html_message=html)
            if mail:
                messages.success(request, 'Сообщение успешно отправлено')
                return redirect('test.html/')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Произошла ошибка, попробуйте еще раз')
    else:
        form = ContactForm()
    return render(request, 'include/_modal.html', {"form": form})
