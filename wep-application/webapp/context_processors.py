from django.utils import timezone

from webapp.forms import FeedbackForm, SubscriberForm
from webapp.models import Call, Contact, Advice, Guarantee, Content, Service


def getting_call_info(request):
    call = Call.objects.first()
    return locals()


def getting_feedback_form(request):
    form = FeedbackForm()

    if hasattr(request, 'resolver_match'):
        service_slug = request.resolver_match.kwargs.get('service_slug')
        
        if service_slug:
            form.fields['service_slug'].initial = service_slug

    return locals()


def getting_subscribe_form(request):
    subscribe_form = SubscriberForm()
    return locals()


def getting_contact_info(request):
    contacts = Contact.objects.all()[:3]
    time = timezone.now()
    return locals()


def getting_advice_info(request):
    advices = Advice.objects.all()[:6]
    return locals()


def getting_content_info(request):
    content = Content.objects.first()
    guarantees = Guarantee.objects.all()[:5]
    return locals()


def getting_service_info(request):
    services = Service.objects.all()
    return locals()
