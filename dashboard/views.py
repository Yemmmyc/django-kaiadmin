from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'dashboard/home.html')

def avatars(request):
    return render(request, 'avatars.html')

def buttons(request):
    return render(request, 'buttons.html')

def charts(request):
    return render(request, 'charts.html')

def datatables(request):
    return render(request, 'datatables.html')

def font_awesome_icons(request):
    return render(request, 'font_awesome_icons.html')

def forms(request):
    return render(request, 'forms.html')

def googlemaps(request):
    return render(request, 'googlemaps.html')

def gridsystem(request):
    return render(request, 'gridsystem.html')

def icon_menu(request):
     return render(request, 'icon_menu.html')

def index(request):
    return render(request, 'index.html')

def jsvectormap(request):
    return render(request, 'jsvectormap.html')

def notifications(request):
    return render(request, 'notifications.html')

def panels(request):
    return render(request, 'panels.html')

def sidebar_style_2_view(request):
    return render(request, 'sidebar_style_2.html')

def simple_line_icons(request):
    return render(request, 'simple_line_icons.html')

def sparkline(request):
    return render(request, 'charts/sparkline.html')

def starter_template(request):
    return render(request, 'starter_template.html')

def sweetalert(request):
    return render(request, 'sweetalert.html')

def typography(request):
    return render(request, 'typography.html')

def widgets(request):
    return render(request, 'widgets.html')

def tables_view(request):
    return render(request, 'tables.html')

def datatables_view(request):
    return render(request, 'datatables.html')

def google_maps(request):
    return render(request, 'maps/googlemaps.html')

def jsvectormap_view(request):
    return render(request, 'maps/jsvectormap.html')

def charts_view(request):
    return render(request, 'charts/charts.html')

def sparkline_chart(request):
    return render(request, 'charts/sparkline.html')

def documentation_index(request):
    return render(request, 'documentation/index.html')

def profile_view(request):
    return render(request, 'profile.html')




