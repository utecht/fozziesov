import json

from django.shortcuts import redirect, HttpResponse, render, Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import *

@login_required
def test(request, stratop_id):
    user = request.user
    userinfo = request.session['userinfo']

    alliance = Alliance.objects.get(alliance_id=userinfo['allianceid'])
    op = Stratop.objects.get(id=stratop_id)
    
    battles = []
    for b in Battle.objects.filter(stratop=op):
        battle = {'sysname': b.system.name,
                  'structname': b.structure.name,
                  'nodes': [{'name': node.system.name,
                             'control': node.control}
                            for node in ControlNode.objects.filter(battle=b)]}

        battles.append(battle)

    corpstatus = []
    for cs in AllianceState.objects.filter(stratop=op):
        corpstatus.append({'name': cs.alliance.name,
                           'num': cs.number})
    eventstatus = []
    for es in Event.objects.filter(stratop=op):
        eventstatus.append({'text': es.text,
                            'time': str(es.time)})

    systems = []
    for sys in System.objects.filter(constellation=op.constellation):
        systems.append({'name': sys.name,
                        'corps': [{'name': sas.alliance.name,
                                   'num': sas.number}
                                  for sas in SystemAllianceState.objects.filter(stratop=op, system=sys)],
                        'events': [{'time': str(se.time),
                                    'text': se.text}
                                   for se in SystemEvent.objects.filter(stratop=op, system=sys)]})
                   
    r = {'battles': battles,
         'status': {'corps': corpstatus,
                    'events': eventstatus},
         'systems': systems}
    
    return HttpResponse(json.dumps(r))

@login_required
@csrf_exempt
def stratop_state(request, stratop_id):
    if request.method == "POST":
        return test(request, stratop_id)

    op = Stratop.objects.get(pk=stratop_id)
    # if request.session['userinfo']['allianceid'] != op.good_guys.alliance_id:
    #     raise Http404
    d = { 'stratop': op }
    return render(request, 'stratop.html', d)

