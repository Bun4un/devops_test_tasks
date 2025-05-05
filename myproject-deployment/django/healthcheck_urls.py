from django.http import JsonResponse
from django.urls import path
import subprocess

def healthcheck(request):
    # Check nginx status
    nginx_status = subprocess.run(['systemctl', 'is-active', '--quiet', 'nginx'], stdout=subprocess.PIPE)
    nginx_status = 'running' if nginx_status.returncode == 0 else 'not running'
    
    # Check Django status
    try:
        # Simple database query to verify Django is working
        from django.db import connections
        connections['default'].cursor()
        django_status = 'running'
    except Exception as e:
        django_status = 'not running'
    
    # Check PostgreSQL status
    try:
        # Simple database query to verify PostgreSQL is working
        from django.db import connections
        connections['default'].cursor()
        postgresql_status = 'running'
    except Exception as e:
        postgresql_status = 'not running'
    
    # Return JSON response
    return JsonResponse({
        'status': 'OK',
        'components': {
            'nginx': nginx_status,
            'django': django_status,
            'postgresql': postgresql_status
        }
    })

urlpatterns = [
    path('healthcheck/', healthcheck, name='healthcheck'),
]