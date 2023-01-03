from django.contrib.auth import user_logged_in
from django.dispatch.dispatcher import receiver
from django.contrib.sessions.models import Session
from . models import UserSession

@receiver(user_logged_in)
def remove_other_sessions(sender, user, request, **kwargs):
    Session.objects.filter(usersession__user=user).delete()
    request.session.save()
    UserSession.objects.get_or_create(
        user=user,
        session_id=request.session.session_key
    )