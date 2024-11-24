from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if not request.user.is_authenticated:
            login_url = reverse('login')
            signup_url = reverse('signup')
            
            if not (request.path == login_url or request.path == signup_url):
                return HttpResponseRedirect(login_url)
        return response
