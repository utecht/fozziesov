# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.views import login as django_login
from django.views.generic import TemplateView
from django.conf import settings

import pycrest


def login(request):
    return django_login(request, template_name='login.html')


def logout(request):
    django_logout(request)
    return redirect('/')


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_authed_crest_context(self):
        """fetch some market data from authenticated CREST"""

        # here we rudely fumble some of PyCrest's private parts
        # since we already completed the authentication process via python-social-auth
        authed_crest = pycrest.eve.AuthedConnection(
            res=self.request.user._get_crest_tokens(),
            endpoint=pycrest.EVE()._authed_endpoint,
            oauth_endpoint=pycrest.EVE()._oauth_endpoint,
            client_id=settings.SOCIAL_AUTH_EVEONLINE_KEY,
            api_key=settings.SOCIAL_AUTH_EVEONLINE_SECRET
        )
        authed_crest()
        print(authed_crest.whoami())
        character_id = authed_crest.whoami()['CharacterID']
        corp = ''
        alliance = ''

        return {
            'corp':corp,
            'alliance':alliance
        }

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['authed_crest'] = self.get_authed_crest_context()
        return context
