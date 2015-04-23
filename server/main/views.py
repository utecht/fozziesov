# Create your views here.
from django.shortcuts import redirect, HttpResponse

def test(request):
    user = request.user
    
    print("User here:")
    print(repr(user))
    print(user.character_id)
    return HttpResponse("user? {}".format(request.user))

