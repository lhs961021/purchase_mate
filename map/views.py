from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
import folium
import geocoder
# Create your views here.

def map(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/map/')
    else:
        form = SearchForm()
    address = request.user.profile.address
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('잘못된 주소입니다! 새로고침을 눌러 다시 검색해주세요!')

    # Map Object 만들기
    m = folium.Map(location=[lat, lng], zoom_start=20)

    folium.Marker([lat, lng], tooltip='Click for more', 
                    popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm' : m,
        'form' : form, 
    }
    return render(request, "map/map.html", context)
