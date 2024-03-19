# from msilib.schema import Error
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *
from authentication.forms import UploadFileForm
from django.contrib.auth.decorators import login_required, permission_required
from .upload_thread import *
import pandas as pd
from tablib import Dataset
from django.core.files.storage import FileSystemStorage
from appsystem.models import *
import os

@login_required(login_url='authentication:login')
@permission_required('fixedassets.custom_view_fixedassets')
def assets(request):
    app_model = Companymodule.objects.filter(tenant_id = request.user.devision.tenant_id.id)
    asset_list = FixedAsset.objects.all()
    template = 'fixedassets/assets/asset.html'
    context = {
        'asset_list': asset_list,
        'heading': 'List of Assets',
        'pageview': 'Assets',
        'app_model':app_model
    }
    return render(request,template,context)
    
@login_required(login_url='authentication:login')
@permission_required('fixedassets.custom_create_fixedassets')
def add_selectclassification(request):
    
    app_model = Companymodule.objects.filter(tenant_id = request.user.devision.tenant_id.id)
    if request.method == 'POST':
        form = AssetsClassificationForm(request.POST)
        if form.is_valid():
            classification = form.cleaned_data['classification']
            assetclassification = Classification.objects.get(name=classification)
            formclassification =assetclassification.name
            # messages.info(request,'Classification Selected')
            return redirect('fixedassets:new-asset', formclassification)
    else:
        form = AssetsClassificationForm()

    template = 'fixedassets/assets/classificationform.html'
    context = {
        'form':form,
        'heading': 'New Asset',
        'pageview': 'List of Assets',
        'app_model':app_model
    }
    return render(request,template,context)

@login_required(login_url='authentication:login')
@permission_required('fixedassets.custom_create_fixedassets')
def add_assets(request,formclassification):
    
    app_model = Companymodule.objects.filter(tenant_id = request.user.devision.tenant_id.id)
    if request.method == 'POST':
        if formclassification == 'Land':
            form = LandForm(request.POST,request=request)
        elif formclassification == 'Buldings And Other Structures':
            form = BuildingForm(request.POST,request=request)
        elif formclassification == 'Transport Equipments':
            form = TransportForm(request.POST,request=request)
        elif formclassification == 'Outdoor Machinery And Equipments':
            form = OutdoorForm(request.POST,request=request)
        elif formclassification == 'Indoor':
            form = IndoorForm(request.POST,request=request)
        else:
            form = WIPForm(request.POST,request=request)
        if form.is_valid():
            form.save()
            messages.info(request,'Asset Saved')
            return redirect('fixedassets:asset-list')
            
    else:
        if formclassification == 'Land':
            form = LandForm(request=request)
        elif formclassification == 'Buldings And Other Structures':
            form = BuildingForm(request=request)
        elif formclassification == 'Transport Equipments':
            form = TransportForm(request=request)
        elif formclassification == 'Outdoor Machinery And Equipments':
            form = OutdoorForm(request=request)
        elif formclassification == 'Indoor':
            form = IndoorForm(request=request)
        else:
            form = WIPForm(request=request)
    if formclassification == 'Land':
        template = 'fixedassets/assets/create-land.html'
    elif formclassification == 'Buldings And Other Structures':
        template = 'fixedassets/assets/create-building.html'
    elif formclassification == 'Transport Equipments':
        template = 'fixedassets/assets/create-transport.html'
    elif formclassification == 'Outdoor Machinery And Equipments':
        template = 'fixedassets/assets/create-outdoor.html'
    elif formclassification == 'Indoor':
        template = 'fixedassets/assets/create-indoor.html'
    else:
        template = 'fixedassets/assets/create-wip.html'
    context = {
        'form':form,
        'heading': 'New Asset',
        'pageview': 'List of Assets',
        'app_model':app_model,
       
    }
    return render(request,template,context)


@login_required(login_url='authentication:login')
def load_subcategory(request):
    ipsascategory = request.GET.get('ipsascategory')
    subcategory = SubCategory.objects.filter(ipsascategory=ipsascategory).order_by('name')
    return render(request, 'authentication/district_dropdown_list.html', {'district': subcategory})


@login_required(login_url='authentication:login')
@permission_required('fixedassets.custom_create_fixedassets')
def edit_assets(request,asset_id):
    
    app_model = Companymodule.objects.filter(tenant_id = request.user.devision.tenant_id.id)
    asset = FixedAsset.objects.get(id=asset_id)
    formclassification = asset.classification.name
    if request.method == 'POST':
        if formclassification == 'Land':
            form = LandForm(request.POST,request=request,instance=asset)
        elif formclassification == 'Buldings And Other Structures':
            form = BuildingForm(request.POST,request=request,instance=asset)
        elif formclassification == 'Transport Equipments':
            form = TransportForm(request.POST,request=request,instance=asset)
        elif formclassification == 'Outdoor Machinery And Equipments':
            form = OutdoorForm(request.POST,request=request,instance=asset)
        else:
            form = WIPForm(request.POST,request=request,instance=asset)
        if form.is_valid():
            form.save()
            messages.info(request,'Asset Saved')
            return redirect('fixedassets:asset-list')
            
    else:
        if formclassification == 'Land':
            form = LandForm(request=request,instance=asset)
        elif formclassification == 'Buldings And Other Structures':
            form = BuildingForm(request=request,instance=asset)
        elif formclassification == 'Transport Equipments':
            form = TransportForm(request=request,instance=asset)
        elif formclassification == 'Outdoor Machinery And Equipments':
            form = OutdoorForm(request=request,instance=asset)
        else:
            form = WIPForm(request=request,instance=asset)
    if formclassification == 'Land':
        template = 'fixedassets/assets/create-land.html'
    elif formclassification == 'Buldings And Other Structures':
        template = 'fixedassets/assets/create-building.html'
    elif formclassification == 'Transport Equipments':
        template = 'fixedassets/assets/create-transport.html'
    elif formclassification == 'Outdoor Machinery And Equipments':
        template = 'fixedassets/assets/create-outdoor.html'
    else:
        template = 'fixedassets/assets/create-wip.html'
    context = {
        'form':form,
        'heading': 'Update',
        'pageview': 'List of Assets',
        'app_model':app_model,
        'asset':asset
       
    }
    return render(request,template,context)

def delete_asset(request,asset_id):
    asset = FixedAsset.objects.get(id=asset_id)
    asset.delete()
    messages.error(request,'Asset Deleted')
    return redirect('fixedassets:asset-list')
