# Create your views here.
from django.shortcuts import redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import *

def test(request):
    user = request.user
    
    print("User here:")
    print(repr(user))
    print(user.character_id)
    return HttpResponse("user? {}".format(request.user))

@login_required
def stratop_state(request, stratop_id):
    op = Stratop.objects.get(pk=stratop_id)

    return HttpResponse(op.good_guys.name)

