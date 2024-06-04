from django.utils import timezone
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import redirect

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Check if the user is authenticated
        if request.user.is_authenticated:
            last_activity_str = request.session.get('last_activity')
            if last_activity_str:
                last_activity = timezone.datetime.fromisoformat(last_activity_str)
                elapsed_time = timezone.now() - last_activity
                if elapsed_time.total_seconds() > settings.SESSION_EXPIRE_SECONDS:
                    logout(request)
                    return redirect('base:login')  # Redirect to login page or any other page

        # Update last activity time in session
        request.session['last_activity'] = timezone.now().isoformat() 

        return response