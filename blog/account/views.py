from django.shortcuts import render, get_object_or_404
from blog_auth.models import CustomUser

# Create your views here.
def account_view(request, username):
    user = get_object_or_404(CustomUser.objects.all(), username=username)
    return render(request, 'account/account.html', {'user': user})