from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin

from thumbnail.things.models import Thing

admin.autodiscover()


class ExtraContextTemplateView(TemplateView):
    extra_context = None

    def get_context_data(self, *args, **kwargs):
        context = super(ExtraContextTemplateView, self).get_context_data(*args, **kwargs)
        if self.extra_context:
            context.update(self.extra_context)
        return context


urlpatterns = patterns('',
    url(r"^$",
        ExtraContextTemplateView.as_view(
            template_name="thumbnail.html",
            extra_context={
                "thing": Thing.objects.all()[0],
            }), name="thumbnail"),

    url(r'^admin/', include(admin.site.urls)),
)
