from django.shortcuts import render, redirect
from .models import Notification

# Create your views here.
def view_notification(request, hash):
    notification = Notification.objects.get(for_user=request.user, hash=hash)
    notification.viewed = True
    notification.save()
    return redirect(notification.url_redirect)