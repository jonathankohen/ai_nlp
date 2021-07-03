from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("regex", views.regex, name="regex"),
    path("lemma", views.lemma, name="lemma"),
    path("pos", views.pos, name="pos"),
    path("ner", views.ner, name="ner"),
]

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
