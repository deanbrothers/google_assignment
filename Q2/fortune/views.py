import json
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework import viewsets
from fortune.serializers import *
from fortune.models import *
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.response import Response
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


company_obj=Company.objects.get(id=1)

class HomeView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        fortune_obj = FortuneCookie.objects.order_by('?')
        print(fortune_obj)
        context['fortune_cookie'] = fortune_obj[0].fortune_option
        context['fortune_id'] = fortune_obj[0].id
        return context

class CompanyViewSet(APIView):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            company_id=request.GET['company_id']
        except:
            return JsonResponse({'msg': 'company id is missing'}, status=404)
        try:
            if company_id == 'all':
                company = Company.objects.filter(status=True)
            else:
                company = Company.objects.get(status=True, id=company_id)                
            company = CompanySerializer(company, context={'request': request})
            return Response(company.data, status=200)
        except:
            return JsonResponse({'msg': 'server error'}, status=500)
    def post(self, request, *args, **kwargs):
        company_id=request.POST.get('company_id')
        status=request.POST.get('status')
        name=request.POST.get('name')
        email=request.POST.get('email')
        gst_number=request.POST.get('gst')
        phone_number=request.POST.get('phone')
        try:
            company_obj=Company.objects.get(id=company_id)
            company_obj.name=name
            company_obj.email=email
            company_obj.gst_number=gst_number
            company_obj.phone_number=phone_number
            try:
                company_obj.save()
                company = Company.objects.get(status=True, id=company_id)
                company = CompanySerializer(company, context={'request': request})
                return Response(company.data, status=200)
            except:
                return JsonResponse({'msg': 'server error'}, status=500)
        except:
            return JsonResponse({'msg': 'company id is missing'}, status=404)



class FortuneViewSet(APIView):
    """
    API endpoint that allows fortune to be viewed or edited.
    """
    
    def get(self, request, *args, **kwargs):
        try:
            fortune_obj = FortuneCookie.objects.order_by('?')                
            fortune_obj = FortuneSerializer(fortune_obj, context={'request': request})
            return Response(fortune_obj.data, status=200)
        except:
            return JsonResponse({'msg': 'server error'}, status=500)
    
    def post(self, request, *args, **kwargs):
        company_id=request.POST.get('company_id')
        status=request.POST.get('status')
        fortune_option=request.POST.get('fortune_option')
        fortune_id=request.POST.get('fortune_id')
        # try:
        fortune_obj=FortuneCookie.objects.get(id=fortune_id)
        fortune_obj.fortune_option=fortune_option
        try:
            fortune_obj.save()
            return Response({'msg': 'fortune save successfully'}, status=200)
        except:
            return JsonResponse({'msg': 'server error'}, status=500)


class OrderViewSet(APIView):
    """
    API endpoint that allows order to be viewed or edited.
    """
    
    def post(self, request, *args, **kwargs):
        daily_checklist_data = request.data
        print(daily_checklist_data)
        return Response({'msg': 'Order placed successfully'}, status=200)
