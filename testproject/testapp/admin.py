from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions




class APIKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        api_key = request.GET.get('api_key')
        if not api_key:
            return None
        try:
            user = get_api_key(api_key)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No user for API KEY')
        return (user, None)