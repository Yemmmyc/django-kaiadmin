from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),  # Updated to use 'index' instead of 'home'
    path('avatars/', views.avatars, name='avatars'),
    path('button/', views.buttons, name='buttons'),
    path('charts/', views.charts, name='charts'),
    path('datatables/', views.datatables, name='datatables'),
    path('font_awesome_icons/', views.font_awesome_icons, name='font_awesome_icons'),
    path('forms/', views.forms, name='forms'),
    path('googlemaps/', views.googlemaps, name='googlemaps'),
    path('gridsystem/', views.gridsystem, name='gridsystem'),
    path('icon_menu/', views.icon_menu, name='icon_menu'),
    path('index/', views.index, name='index'),
    path('jsvectormap/', views.jsvectormap, name='jsvectormap'),
    path('notifications/', views.notifications, name='notifications'),
    path('panels/', views.panels, name='panels'),
    path('sidebar_style_2/', views.sidebar_style_2_view, name='sidebar_style_2'),
    path('simple_line_icons/', views.simple_line_icons, name='simple_line_icons'),
    path('sparkline/', views.sparkline, name='sparkline'),
    path('starter_template/', views.starter_template, name='starter_template'),
    path('sweetalert/', views.sweetalert, name='sweetalert'),
    path('typography/', views.typography, name='typography'),
    path('widgets/', views.widgets, name='widgets'),
    path('demo1/index/', views.index, name='demo1_index'),
    path('tables/', views.tables_view, name='tables'), 
    path('tables/datatables/', views.datatables_view, name='datatables'),
    path('maps/googlemaps/', views.google_maps, name='googlemaps'),
    path('maps/jsvectormap/', views.jsvectormap_view, name='jsvectormap'),
    path('charts/charts/', views.charts_view, name='charts'),
    path('charts/sparkline/', views.sparkline, name='sparkline'), 
    path('documentation/index/', views.documentation_index, name='documentation'),
    path('profile/', views.profile_view, name='profile'),






]
