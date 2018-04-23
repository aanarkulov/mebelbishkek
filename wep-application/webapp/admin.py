import threading
from django.contrib import admin
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from webapp.forms import NewsForm
from webapp.models import Call, Feedback, Quality, Icon, LeftBar, Review, Contact, ProductionFeature, Employee, News, \
    Subscriber, \
    AboutUs, Content, Guarantee, OurTeam, SocialLink, Coordinate, Advice, Service, OrderOfMaster


class CallAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'icon')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message')


class OrderOfMasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')


class QualityAdmin(admin.ModelAdmin):
    list_display = ('id', 'quality')


class IconAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'icon')


class LeftBarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'icon')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'company', 'text', 'image')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class AdviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'slug', 'date')
    prepopulated_fields = {"slug": ("title",)}


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'price', 'term', 'slug')
    prepopulated_fields = {"slug": ("title",)}


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'image')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
    form = NewsForm

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        send_to_subscribers = form.cleaned_data['send_to_subscribers']

        subscribers = Subscriber.objects.all()
        email_of_subscribers = []
        for i in subscribers:
            email_of_subscribers.append(i.email)

        if send_to_subscribers:
            context = {
                "title": obj.title,
                "description": obj.description,
            }

            content = render_to_string('send_mail/send_news_to_subscribers.html', context)
            mail = EmailMessage(_('Новости'), content, to=email_of_subscribers)
            mail.content_subtype = 'html'
            mail.send()


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')


class GuaranteeAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'description')


class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'icon')


class CoordinateAdmin(admin.ModelAdmin):
    list_display = ('address', 'position')


admin.site.register(Call, CallAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(OrderOfMaster, OrderOfMasterAdmin)
admin.site.register(Quality, QualityAdmin)
admin.site.register(Icon, IconAdmin)
admin.site.register(LeftBar, LeftBarAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Advice, AdviceAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ProductionFeature)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Subscriber)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Guarantee, GuaranteeAdmin)
admin.site.register(OurTeam, OurTeamAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
admin.site.register(Coordinate, CoordinateAdmin)
