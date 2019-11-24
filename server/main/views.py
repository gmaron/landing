from django.http import JsonResponse, HttpResponseBadRequest

from django.shortcuts import render
from .utils import check, send_email
from django.views.generic import View



class Index(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})

    def post(self, request, *args, **kwargs):

        if (request.POST['name'] is None) or (request.POST['email'] is None) or (request.POST['message'] is None):
            return HttpResponseBadRequest("Error During Error Processing")

        result = send_email(request.POST['name'], request.POST['email'], request.POST['message'])
        return JsonResponse({"status": result})

