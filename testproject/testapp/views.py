# from django.shortcuts import render
from django.shortcuts import render
import requests
import json
from django.contrib.gis.geoip2 import GeoIP2



def geo (request):
    # ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    url = 'http://ip-api.com/json/'
    response1 = requests.get(url)
    geodata1 = response1.json()
    ip = geodata1['query']
    sip = str(ip)
    print(sip)


    BASE_URL = 'http://api.ipstack.com/'
    ENDPOINT =  sip
    url = BASE_URL + ENDPOINT
    header = {'access_key': 'fca3c19a9f568d8ab244845af90e661c'}

    response =  requests.get(url,header)
    geodata = response.json()

    return render(request,'testapp/demo.html',{'city': geodata['city'],'ip': geodata['ip'],'country_name': geodata['country_name']})






# from django.shortcuts import render
# import requests
#
# def home(request):
#     is_cached = ('geodata' in request.session)
#
#     if not is_cached:
#         ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
#         response = requests.get('http://freegeoip.net/json/%s' % ip_address)
#         request.session['geodata'] = response.json()
#
#     geodata = request.session['geodata']
#
#     return render(request, 'core/home.html', {
#         'ip': geodata['ip'],
#         'country': geodata['country_name'],
#         'latitude': geodata['latitude'],
#         'longitude': geodata['longitude'],
#         'api_key': 'AIzaSyC1UpCQp9zHokhNOBK07AvZTiO09icwD8I',  # Don't do this! This is just an example. Secure your keys properly.
