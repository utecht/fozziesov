# Create your views here.
from django.shortcuts import redirect, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import *

@login_required
def test(request):
    user = request.user
    userinfo = request.session['userinfo']

    alliance = Alliance.objects.get(alliance_id=userinfo['allianceid'])
    ops = Stratop.objects.filter(good_guys=alliance)
    
    html = "user? {}<br/>".format(request.user)
    html += "alliance_id: {}<br/>".format(userinfo['allianceid'])
    html += "Alliance: {}<br/>".format(alliance.name)
    for o in ops:
        html += "Op: {}<br/>".format(o.constellation.name)

    return HttpResponse(html)

@login_required
def stratop_state(request, stratop_id):
    op = Stratop.objects.get(pk=stratop_id)

    return HttpResponse(op.good_guys.name)

