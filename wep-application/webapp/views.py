import threading
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from django.views.generic import TemplateView, DetailView, FormView, ListView
from webapp.forms import MasterForm, FeedbackForm, SubscriberForm
from webapp.models import Quality, Icon, LeftBar, Review, Service, AboutUs, ProductionFeature, Employee, OurTeam, \
    Coordinate, SocialLink, Advice
from works.models import Catalog, Work
from django.core.mail import EmailMessage


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['qualities'] = Quality.objects.all()[:3]
        context['icons'] = Icon.objects.all()[:3]
        context['left_bars'] = LeftBar.objects.all()[:5]
        context['catalogs'] = Catalog.objects.all()[:15]
        context['reviews'] = Review.objects.all()[:10]
        context['master_form'] = MasterForm()
        context['works'] = Work.objects.all()[:6]
        return context


class ServiceView(TemplateView):
    template_name = 'services.html'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service.html'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, slug=self.kwargs.get('service_slug'))


class AboutUsView(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['about_us'] = AboutUs.objects.first()
        context['production_features'] = ProductionFeature.objects.all()[:5]
        context['our_team'] = OurTeam.objects.first()
        context['employees'] = Employee.objects.all()[:15]
        context['reviews'] = Review.objects.all()[:10]
        return context


class ContactView(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['coordinate'] = Coordinate.objects.first()
        context['social_links'] = SocialLink.objects.all()[:5]
        return context


class AdviceView(ListView):
    template_name = 'advices.html'

    def get_queryset(self):
        return Advice.objects.order_by("-date")[:20]


class AdviceDetailView(DetailView):
    model = Advice
    template_name = 'advice.html'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, slug=self.kwargs.get('slug'))


class FeedbackFormView(FormView):
    form_class = FeedbackForm

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def form_valid(self, form):
        feedback = form.save(commit=False)
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']
        feedback.save()
        thread = threading.Thread(target=self.send_email_feedback, args=(name, phone, message))
        thread.start()
        return super(FeedbackFormView, self).form_valid(form)

    @staticmethod
    def send_email_feedback(name, phone, message):
        context = {
            "name": name,
            "phone": phone,
            "message": message,
        }

        content = render_to_string('send_mail/feedback.html', context)
        mail = EmailMessage(_('Обратаная связь'), content, to=[settings.EMAIL_DEFAULT])
        mail.content_subtype = 'html'
        mail.send()


class OrderOfService(FormView):
    form_class = FeedbackForm

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def form_valid(self, form):
        feedback = form.save(commit=False)
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']
        service_slug = form.cleaned_data['service_slug']
        if service_slug:
            feedback.service = Service.objects.get(slug=service_slug)
        feedback.save()
        thread = threading.Thread(target=self.send_email_service, args=(name, phone, message, service_slug))
        thread.start()
        return super(OrderOfService, self).form_valid(form)

    @staticmethod
    def send_email_service(name, phone, message, service_slug):
        context = {
            "name": name,
            "phone": phone,
            "message": message,
            "service": Service.objects.get(slug=service_slug)
        }

        content = render_to_string('send_mail/order_of_service.html', context)
        mail = EmailMessage(_('Заказ услуги'), content, to=[settings.EMAIL_DEFAULT])
        mail.content_subtype = 'html'
        mail.send()


class OrderOfMaster(FormView):
    form_class = MasterForm

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def form_valid(self, form):
        master = form.save(commit=False)
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        master.save()
        thread = threading.Thread(target=self.send_email_service, args=(name, phone))
        thread.start()
        return super(OrderOfMaster, self).form_valid(form)

    @staticmethod
    def send_email_service(name, phone):
        context = {
            "name": name,
            "phone": phone,
        }

        content = render_to_string('send_mail/order_of_master.html', context)
        mail = EmailMessage(_('Вызов замерщика'), content, to=[settings.EMAIL_DEFAULT])
        mail.content_subtype = 'html'
        mail.send()


class SubscriberFormView(FormView):
    form_class = SubscriberForm

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def form_valid(self, form):
        subscriber = form.save(commit=False)
        subscriber.save()
        return super(SubscriberFormView, self).form_valid(form)
