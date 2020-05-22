from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    re_path(r'^celery-progress/', include('celery_progress.urls')),  # the endpoint is configurabl
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('progress', hello.views.progress_view, name="progress_view"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
