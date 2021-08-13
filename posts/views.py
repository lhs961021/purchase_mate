from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Post
from users.models import Profile
from django.utils import timezone
from .forms import SpotForm
import folium
import geocoder
from .models import Search
from .forms import SearchForm
from django.contrib.auth.models import User
import math
from operator import itemgetter

# Create your views here.


def map(request, id):
    # if request.method == 'POST':
    #     form = SearchForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/map/') #검색부분 필요할수도 있으니까 일단 주석
    # else:

    form = SearchForm()
    if request.user.is_authenticated:  # 로그인 한 경우
        # 내 개인정보 주소
        address = request.user.profile.address
        location = geocoder.osm(address)
        lat = location.lat
        lng = location.lng
    else:
        lat = 0
        lng = 0

    # 게시물에 올린 픽업 장소 주소
    spot = get_object_or_404(Post, pk=id)
    spot = spot.spot
    spot_location = geocoder.osm(spot)
    spot_lat = spot_location.lat
    spot_lng = spot_location.lng

    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse("잘못된 주소입니다! 새로고침을 눌러 다시 검색해주세요!")

    # Map Object 만들기
    m = folium.Map(location=[lat, lng], zoom_start=15)

    folium.Marker([lat, lng], tooltip="Click for more", popup=country).add_to(m)
    folium.Marker([spot_lat, spot_lng], tooltip="Click for more", popup=country).add_to(
        m
    )
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
        "m": m,
        "form": form,
         "d": d,
    }

    return render(request, "map/map.html", context)


# Create your views here.
def showmain(request):
    posts = Post.objects.all()
    return render(request, "purchase_mate/index.html", {"posts": posts})


def shop(request):
    return render(request, "posts/shop.html")


def shop_detail(request):
    return render(request, "posts/shop_detail.html")


# 카테고리 부분
def food(request):
    post = Post.objects.filter(category="식자재")
    return render(request, "category/food.html", {"post": post})


def daily_necessity(request):
    post = Post.objects.filter(category="생필품")
    return render(request, "category/daily_necessity.html", {"post": post})


def ott(request):
    post = Post.objects.filter(category="OTT 서비스")
    return render(request, "category/ott.html", {"post": post})


def etc(request):
    post = Post.objects.filter(category="기타")
    return render(request, "category/etc.html", {"post": post})


# 정렬 부분
def all_postlist(request):
    if request.user.is_authenticated:
        post = Post.objects.all()
        postd=[]
        
        for i in post:
            lt=[]
            address = request.user.profile.address
            location = geocoder.osm(address)
            lat = location.lat
            lng = location.lng
        
            #게시물에 올린 픽업 장소 주소
            spot = i.spot
            spot_location = geocoder.osm(spot)
            spot_lat = spot_location.lat
            spot_lng = spot_location.lng
            
            radius = 6371  # km
            dlat = math.radians(spot_lat-lat)
            dlon = math.radians(spot_lng-lng)
            a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat)) \
                * math.cos(math.radians(spot_lat)) * math.sin(dlon/2) * math.sin(dlon/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = radius * c
            lt.append(i)
            lt.append(d)
            postd.append(lt)
            
            
        # return HttpResponse("hi")
        # for j in postd:
        #     print(j)
        return render(request, "sort/all_postlist.html", {"post": postd})
    else:
        return redirect("account_login")


def recent_postlist(request):
    post = Post.objects.order_by("-pub_date")
    return render(request, "sort/recent_postlist.html", {"post": post})


def deadline_postlist(request):

    post = Post.objects.order_by("deadline")
    return render(request, "sort/deadline_postlist.html", {"post": post})


def distance_postlist(request):

    if request.user.is_authenticated:
        post = Post.objects.all()
        dislt=[]
        for i in post:
            lt=[]
            address = request.user.profile.address
            location = geocoder.osm(address)
            lat = location.lat
            lng = location.lng
        
            #게시물에 올린 픽업 장소 주소
            spot = i.spot
            spot_location = geocoder.osm(spot)
            spot_lat = spot_location.lat
            spot_lng = spot_location.lng
            
            radius = 6371  # km
            dlat = math.radians(spot_lat-lat)
            dlon = math.radians(spot_lng-lng)
            a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat)) \
                * math.cos(math.radians(spot_lat)) * math.sin(dlon/2) * math.sin(dlon/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = radius * c
            lt.append(i)
            lt.append(d)
            dislt.append(lt)

            
       
        dislt.sort(key=itemgetter(1))
        
        return render(request, "sort/distance_postlist.html", {"post": dislt})
    else:
        return redirect("account_login")

def price_postlist(request):
    post = list(Post.objects.all())
    post.sort(key=lambda x: x.price / x.people)
    return render(request, "sort/price_postlist.html", {"post": post})


# CRUD 부분
def makepost(request):
    return render(request, "makepost.html")


def detail(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=id)

        post_writer=Profile.objects.get(user=post.writer)

        address = request.user.profile.address
        location = geocoder.osm(address)
        lat = location.lat
        lng = location.lng
    
        #게시물에 올린 픽업 장소 주소
        spot = post.spot
        spot_location = geocoder.osm(spot)
        spot_lat = spot_location.lat
        spot_lng = spot_location.lng
        
        radius = 6371  # km
        dlat = math.radians(spot_lat-lat)
        dlon = math.radians(spot_lng-lng)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat)) \
            * math.cos(math.radians(spot_lat)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c

    
    
        return render(request,'detail.html',{'post':post,'post_writer':post_writer,'d':d})
    else:
        return redirect("account_login")

def create(request):
    makepost_post = Post()
    makepost_post.title = request.POST['title']
    makepost_post.writer=request.user
    makepost_post.pub_date=timezone.now()
    makepost_post.deadline=request.POST['deadline']
    makepost_post.quantity=request.POST['quantity']
    makepost_post.price=request.POST['price']
    makepost_post.people=request.POST['people']
    makepost_post.category=request.POST['category']
    makepost_post.image=request.FILES.get('image')
    makepost_post.chat=request.POST['chat']
    makepost_post.spot=request.POST['spot']
    makepost_post.price_per_person=int(makepost_post.price)/int(makepost_post.people)
    
    # address = request.user.profile.address
    # location = geocoder.osm(address)
    # lat = location.lat
    # lng = location.lng
   
    # #게시물에 올린 픽업 장소 주소
    # spot = makepost_post.spot
    # spot_location = geocoder.osm(spot)
    # spot_lat = spot_location.lat
    # spot_lng = spot_location.lng
    
    # radius = 6371  # km
    # dlat = math.radians(spot_lat-lat)
    # dlon = math.radians(spot_lng-lng)
    # a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat)) \
    #     * math.cos(math.radians(spot_lat)) * math.sin(dlon/2) * math.sin(dlon/2)
    # c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    # d = radius * c

    # # makepost_post.distance=d
    makepost_post.save()

    
    return redirect ('posts:detail',makepost_post.id)


def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, "edit.html", {"post": edit_post})


def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST["title"]
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    if request.POST['deadline']:
        update_post.deadline=request.POST['deadline']
    update_post.quantity=request.POST['quantity']
    update_post.price=request.POST['price']
    update_post.people=request.POST['people']
    update_post.category=request.POST['category']
    if request.FILES.get('image'):
        update_post.image=request.FILES.get('image')
    update_post.chat=request.POST['chat']
    update_post.spot=request.POST['spot']
    update_post.price_per_person=int(update_post.price)/int(update_post.people)

    # address = request.user.profile.address
    # location = geocoder.osm(address)
    # lat = location.lat
    # lng = location.lng
   
    # #게시물에 올린 픽업 장소 주소
    # spot = update_post.spot
    # spot_location = geocoder.osm(spot)
    # spot_lat = spot_location.lat
    # spot_lng = spot_location.lng
    
    # radius = 6371  # km
    # dlat = math.radians(spot_lat-lat)
    # dlon = math.radians(spot_lng-lng)
    # a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat)) \
    #     * math.cos(math.radians(spot_lat)) * math.sin(dlon/2) * math.sin(dlon/2)
    # c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    # d = radius * c

    # update_post.distance=d
   
    update_post.save()
    return redirect("posts:detail", update_post.id)


def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect("posts:all_postlist")


def result(request):
    query = request.GET["query"]
    if query:
        posts = Post.objects.filter(title__contains=query)
    else:
        posts = Post.objects.all()
    return render(request, "result.html", {"posts": posts})
