from django.contrib.auth.models import User

def is_correctusername(username):
    try:
        user=User.objects.get(username=username)
    except:
        user=None
    return user
