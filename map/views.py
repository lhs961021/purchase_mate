from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
from posts.models import Post
import folium
import geocoder
import math
# Create your views here.

def map(request,id):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/map/')
    else:
        form = SearchForm()
    #내 개인정보 주소
    address = request.user.profile.address
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    #게시물에 올린 픽업 장소 주소
    spot = get_object_or_404(Post, pk=id)
    spot = spot.spot
    spot_location = geocoder.osm(spot)
    spot_lat = spot_location.lat
    spot_lng = spot_location.lng
    
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('잘못된 주소입니다! 새로고침을 눌러 다시 검색해주세요!')

    # Map Object 만들기
    m = folium.Map(location=[lat, lng], zoom_start=15)

    folium.Marker([lat, lng], tooltip='Click for more', 
                    popup=country).add_to(m)
    folium.Marker([spot_lat, spot_lng], tooltip='Click for more', 
                    popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    

    radius = 6371  # km
 
    dlat = math.radians(spot_lat-lat)
    dlon = math.radians(spot_lng-lng)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat)) \
        * math.cos(math.radians(spot_lat)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    context = {
        'm' : m,
        'form' : form,
        "d": d, 
    }

    return render(request, "map/map.html", context)

