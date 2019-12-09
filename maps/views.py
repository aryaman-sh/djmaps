from django.shortcuts import render

# Create your views here.

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoiYXJ5YW1hbjQxNTIiLCJhIjoiY2szeTE5NHB5MWZvbDNtbzF1azV2aTAyNCJ9.VX1AzRhPnccvg-ul4h1V2Q'
    return render(request, 'default.html',
                  {'mapbox_access_token': mapbox_access_token})

