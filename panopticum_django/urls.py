"""panopticum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import redirect

from rest_framework import routers
import rest_framework.authtoken.views

from panopticum import views
from panopticum import jira
from panopticum_django import settings

router = routers.DefaultRouter()
router.register(r'product_version', views.ProductVersionViewSet)
router.register(r'component', views.ComponentViewSet)
router.register(r'component_history', views.HistoryComponentVersionViewSet)
router.register(r'requirement', views.RequirementViewSet)
router.register(r'requirement_status', views.RequirementStatusEntryViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'requirement_set', views.RequirementSetViewSet)
router.register(r'component_version', views.ComponentVersionViewSet)
router.register(r'location_class', views.DeploymentLocationClassViewSet)
router.register(r'component_category', views.ComponentCategoryViewSet)
router.register(r'component_type', views.ComponentTypeViewSet)
router.register(r'component_data_privacy_class', views.ComponentDataPrivacyClassViewSet)
router.register(r'user', views.UserDetail)
router.register(r'token', views.Token)
router.register(r'issue', views.JiraIssueView)
router.register(r'techradar_quadrants', views.TechradarQuadrantViewSet)
router.register(r'techradar_rings', views.TechradarRingViewSet)
router.register(r'techradar_entries', views.TechradarEntryViewSet)

urlpatterns = [
    path('', lambda request: redirect('/dashboard/components.html', permanent=False)),  # Redirect root URL
    path('admin/', admin.site.urls),
    re_path('^component/', views.component, name='Component'),
    re_path('^dashboard/components.html', views.dashboard_components, name='Components'),
    re_path('^requirementset/', views.requirementset, name='team'),
    re_path('^dashboard/links.html', views.dashboard_components, name='Links'),
    re_path('^techradar/ring.html', views.techradar_ring, name='Tech Radar'),
    re_path('^techradar/table.html', views.techradar_table, name='Tech Radar'),
    re_path('^techradar/config.json', views.techradar_config),
    re_path(r'^api/jira_url/', views.JiraUrlView.as_view(), name='jira_url'),
    path('api/login/', rest_framework.authtoken.views.obtain_auth_token),
    path('api/login/', views.LoginAPIView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path('^api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += (path("admin/", include('loginas.urls')),)
