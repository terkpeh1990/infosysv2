from django import forms
from .models import *
from django.forms.widgets import NumberInput
from company.models import Devision,Sub_Devision
from inventory.models import Brands
from datetime import date


class ClassificationForm(forms.ModelForm):
    name = forms.CharField(label=False)
    class Meta:
        model = Classification
        fields = ('name',)

class AccountingRecognitionForm(forms.ModelForm):
    name = forms.CharField(label=False)
    classification =forms.ModelChoiceField(
        queryset=Classification.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required = True
    )
    class Meta:
        model = AccountingRecognition
        fields = ('name','classification')

class GFSCategoryForm(forms.ModelForm):
    code = forms.CharField(label=False,required=True)
    name = forms.CharField(label=False)
    class Meta:
        model = GFSCategory
        fields = ('code','name',)


class SubCategoryForm(forms.ModelForm):
    name = forms.CharField(label=False)
    ipsascategory = forms.ModelChoiceField(
        queryset=IPSASCategory.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    class Meta:
        model = SubCategory
        fields = ('name','ipsascategory')

class IPSASCategoryForm(forms.ModelForm):
    name = forms.CharField(label=False)
    classification =forms.ModelChoiceField(
        queryset=Classification.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    gfscategory =forms.ModelChoiceField(
        queryset=GFSCategory.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    class Meta:
        model = IPSASCategory
        fields = ('name','classification','gfscategory')


class LocationForm(forms.ModelForm):
    code = forms.CharField(label=False)
    location = forms.CharField(label= False)
    class Meta:
        model = Location
        fields = ('code','location',)

class SourceOfFundingForm(forms.ModelForm):
    code = forms.CharField(label=False)
    funding = forms.CharField(label= False)
    class Meta:
        model = SourceOfFunding
        fields = ('code','funding',)

class MothodofAcquisitionForm(forms.ModelForm):
    name = forms.CharField(label=False)
    class Meta:
        model = MothodofAcquisition
        fields = ('name',)

class AssetsClassificationForm(forms.ModelForm):
    classification =forms.ModelChoiceField(
        queryset=Classification.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    class Meta:
        model = FixedAsset
        fields = ('classification',)


class LandForm(forms.ModelForm):
    condition = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    usage = (
        ('Public Domain', 'Public Domain'),
        ('Private Domain', 'Private Domain'),
    )
    status = (
        ('In Use', 'In Use'),
        ('Not in Use', 'Not in Use'),
        ('Retired', 'Retired'),
        ('Disposed', 'Disposed'),
    )
    disposal = (
        ('Sales', 'Sales'),
        ('Auction', 'Auction'),
        ('Donated', 'Donated'),
        ('Trade-in/Exchanged', 'Trade-in/Exchanged'),
        ('Transfer-out to Other Govt Entities', 'Transfer-out to Other Govt Entities'),
        ('Scrapped', 'Scrapped'),
    )
    classification = forms.ModelChoiceField(
        queryset=Classification.objects.filter(name='Land').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    description =forms.CharField(label=False,required=True)
    accountingrecognition = forms.ModelChoiceField(
        queryset=AccountingRecognition.objects.filter(classification__name='Land').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    amotization = forms.ChoiceField(label=False,choices=condition,required=True)
    usage =forms.ChoiceField(label=False,choices=usage,required=True)
    ipsascategory = forms.ModelChoiceField(
        queryset=IPSASCategory.objects.filter(classification__name='Land').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    size =forms.CharField(label=False,required=True)
    location =forms.ModelChoiceField(
        queryset=Location.objects.all().order_by('location'),
        label=False,
        empty_label="Select One",
        required=True
    )
    ghanapostgpsaddress=forms.CharField(label=False,required=True)
    titled = forms.ChoiceField(label=False,choices=condition,required=True)
    staffid = forms.CharField(label=False,required=True)
    costcenter = forms.ModelChoiceField(
        queryset=Devision.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    subcostcenter =forms.ModelChoiceField(
        queryset=Sub_Devision.objects.all(),
        label=False,
        empty_label="Select One",
        required=True
    )
   
    methodofacquisition =forms.ModelChoiceField(
        queryset=MothodofAcquisition.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    currentstatus = forms.ChoiceField(label=False,choices=status,required=True)
    investmentproperty =forms.ChoiceField(label=False,choices=condition,required=True)
    fundsource =forms.ModelChoiceField(
        queryset=SourceOfFunding.objects.all().order_by('funding'),
        label=False,
        empty_label="Select One",
        required=True
    )
    value = forms.FloatField(label=False,required=False,initial=0.0) 
    usefullife = forms.IntegerField(label=False,required=False)
    comments = forms.CharField(
    widget=forms.Textarea(attrs={'maxlength': 255}),
        label=False,required=True)

    class Meta:
        model = FixedAsset
        fields = ('classification','description','accountingrecognition','amotization','usage','ipsascategory','subcategory','size','location','ghanapostgpsaddress','titled','staffid','costcenter',
        'subcostcenter','staffid','methodofacquisition',
        'currentstatus','investmentproperty','fundsource','value','usefullife','comments')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        instance = kwargs.get("instance")
        super(LandForm,self).__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields['costcenter'].queryset = Devision.objects.filter(status = True)
            
        else:
            self.fields['costcenter'].queryset = Devision.objects.filter(tenant_id=self.request.user.devision.tenant_id.id,status = True)
       
        if instance:
            self.fields['subcostcenter'].queryset = Sub_Devision.objects.filter(devision=instance.costcenter)
            self.fields['subcategory'].queryset = SubCategory.objects.filter(ipsascategory=instance.ipsascategory)
        else:
            self.fields['subcostcenter'].queryset = Sub_Devision.objects.none()
            self.fields['subcategory'].queryset = SubCategory.objects.none()


        if 'costcenter' in self.data:
            try:
                devision = int(self.data.get('costcenter'))
                self.fields['subcostcenter'].queryset = Sub_Devision.objects.filter(
                    devision=devision)
            except (ValueError, TypeError):
                pass
        
        if 'ipsascategory' in self.data:
            try:
                ipsascategory = int(self.data.get('ipsascategory'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(
                    ipsascategory=ipsascategory)
            except (ValueError, TypeError):
                pass


class BuildingForm(forms.ModelForm):
    condition = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    usagetype = (
        ('Pool', 'Pool'),
        ('Assigned', 'Assigned'),
    )
    
    status = (
        ('In Use', 'In Use'),
        ('Not in Use', 'Not in Use'),
        ('Retired', 'Retired'),
        ('Disposed', 'Disposed'),
    )
    disposal = (
        ('Sales', 'Sales'),
        ('Auction', 'Auction'),
        ('Donated', 'Donated'),
        ('Trade-in/Exchanged', 'Trade-in/Exchanged'),
        ('Transfer-out to Other Govt Entities', 'Transfer-out to Other Govt Entities'),
        ('Scrapped', 'Scrapped'),
    )
    bcondition=(
        ('Good','Good'),
        ('Needs Repair/Renovation/Servicing','Needs Repair/Renovation/Servicing'),
        ('Irrepairable/Unserviceable','Irrepairable/Unserviceable'),
        ('Not Sighted','Not Sighted'),
    )
    classification = forms.ModelChoiceField(
        queryset=Classification.objects.filter(name='Buldings And Other Structures').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    description =forms.CharField(label=False,required=True)
    accountingrecognition = forms.ModelChoiceField(
        queryset=AccountingRecognition.objects.filter(classification__name='Buldings And Other Structures').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    depreciation = forms.ChoiceField(label=False,choices=condition,required=True)
    ipsascategory = forms.ModelChoiceField(
        queryset=IPSASCategory.objects.filter(classification__name='Buldings And Other Structures').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    quantity=forms.IntegerField(label=False,required=False)
    location =forms.ModelChoiceField(
        queryset=Location.objects.all().order_by('location'),
        label=False,
        empty_label="Select One",
        required=True
    )
    ghanapostgpsaddress=forms.CharField(label=False,required=True)
    dateplacedinservice=forms.DateField(widget=NumberInput(attrs={'type': 'date'}),label=False)
    staffid = forms.CharField(label=False,required=True)
    costcenter = forms.ModelChoiceField(
        queryset=Devision.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    subcostcenter =forms.ModelChoiceField(
        queryset=Sub_Devision.objects.all(),
        label=False,
        empty_label="Select One",
        required=True
    )
    usagetype= forms.ChoiceField(label=False,choices=usagetype,required=True)
    methodofacquisition =forms.ModelChoiceField(
        queryset=MothodofAcquisition.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    currentstatus = forms.ChoiceField(label=False,choices=status,required=True)
    conditions = forms.ChoiceField(label=False,choices=bcondition,required=True)
    investmentproperty =forms.ChoiceField(label=False,choices=condition,required=True)
    fundsource =forms.ModelChoiceField(
        queryset=SourceOfFunding.objects.all().order_by('funding'),
        label=False,
        empty_label="Select One",
        required=True
    )
    value = forms.FloatField(label=False,required=False,initial=0.0) 
    usefullife = forms.IntegerField(label=False,required=False)
    comments = forms.CharField(
    widget=forms.Textarea(attrs={'maxlength': 255}),
        label=False,required=True)

    class Meta:
        model = FixedAsset
        fields = ('classification','description','accountingrecognition','depreciation','ipsascategory','subcategory','quantity','location','ghanapostgpsaddress','dateplacedinservice','staffid','costcenter',
        'subcostcenter','usagetype','staffid','methodofacquisition',
        'currentstatus','conditions','investmentproperty','fundsource','value','usefullife','comments')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        instance = kwargs.get("instance")
        super(BuildingForm,self).__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields['costcenter'].queryset = Devision.objects.filter(status = True)
            
        else:
            self.fields['costcenter'].queryset = Devision.objects.filter(tenant_id=self.request.user.devision.tenant_id.id,status = True)
       
        if instance:
            self.fields['subcostcenter'].queryset = Sub_Devision.objects.filter(devision=instance.costcenter)
            self.fields['subcategory'].queryset = SubCategory.objects.filter(ipsascategory=instance.ipsascategory)
        else:
            self.fields['subcostcenter'].queryset = Sub_Devision.objects.none()
            self.fields['subcategory'].queryset = SubCategory.objects.none()


        if 'costcenter' in self.data:
            try:
                devision = int(self.data.get('costcenter'))
                self.fields['subcostcenter'].queryset = Sub_Devision.objects.filter(
                    devision=devision)
            except (ValueError, TypeError):
                pass
        
        if 'ipsascategory' in self.data:
            try:
                ipsascategory = int(self.data.get('ipsascategory'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(
                    ipsascategory=ipsascategory)
            except (ValueError, TypeError):
                pass

class TransportForm(forms.ModelForm):
    years = [(year, str(year)) for year in range(1700, date.today().year + 1)]
    condition = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    usagetype = (
        ('Pool', 'Pool'),
        ('Assigned', 'Assigned'),
    )
    
    status = (
        ('In Use', 'In Use'),
        ('Not in Use', 'Not in Use'),
        ('Retired', 'Retired'),
        ('Disposed', 'Disposed'),
    )
    disposal = (
        ('Sales', 'Sales'),
        ('Auction', 'Auction'),
        ('Donated', 'Donated'),
        ('Trade-in/Exchanged', 'Trade-in/Exchanged'),
        ('Transfer-out to Other Govt Entities', 'Transfer-out to Other Govt Entities'),
        ('Scrapped', 'Scrapped'),
    )
    bcondition=(
        ('Good','Good'),
        ('Needs Repair/Renovation/Servicing','Needs Repair/Renovation/Servicing'),
        ('Irrepairable/Unserviceable','Irrepairable/Unserviceable'),
        ('Not Sighted','Not Sighted'),
    )
    classification = forms.ModelChoiceField(
        queryset=Classification.objects.filter(name='Transport Equipments').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    description =forms.CharField(label=False,required=True)
    registrationnumber =forms.CharField(label=False,required=True)
    accountingrecognition = forms.ModelChoiceField(
        queryset=AccountingRecognition.objects.filter(classification__name='Transport Equipments').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    depreciation = forms.ChoiceField(label=False,choices=condition,required=True)
    ipsascategory = forms.ModelChoiceField(
        queryset=IPSASCategory.objects.filter(classification__name='Transport Equipments').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    quantity=forms.IntegerField(label=False,required=False)
    location =forms.ModelChoiceField(
        queryset=Location.objects.all().order_by('location'),
        label=False,
        empty_label="Select One",
        required=True
    )
    dateplacedinservice=forms.DateField(widget=NumberInput(attrs={'type': 'date'}),label=False)
    colour =forms.CharField(label=False,required=True)
    chassisno =forms.CharField(label=False,required=True)
    engineserialno =forms.CharField(label=False,required=True)
    manufacturer = forms.ModelChoiceField(
        queryset=Brands.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    model = forms.CharField(label=False,required=True)
    modelyear =forms.ChoiceField(choices=years, initial=date.today().year,label=False,required=True)
    costcenter = forms.ModelChoiceField(
        queryset=Devision.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    subcostcenter =forms.ModelChoiceField(
        queryset=Sub_Devision.objects.all(),
        label=False,
        empty_label="Select One",
        required=True
    )
    usagetype= forms.ChoiceField(label=False,choices=usagetype,required=True)
    staffid = forms.CharField(label=False,required=True)
    methodofacquisition =forms.ModelChoiceField(
        queryset=MothodofAcquisition.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    currentstatus = forms.ChoiceField(label=False,choices=status,required=True)
    conditions = forms.ChoiceField(label=False,choices=bcondition,required=True)
    investmentproperty =forms.ChoiceField(label=False,choices=condition,required=True)
    fundsource =forms.ModelChoiceField(
        queryset=SourceOfFunding.objects.all().order_by('funding'),
        label=False,
        empty_label="Select One",
        required=True
    )
    value = forms.FloatField(label=False,required=False,initial=0.0) 
    usefullife = forms.IntegerField(label=False,required=False)
    comments = forms.CharField(
    widget=forms.Textarea(attrs={'maxlength': 255}),
        label=False,required=True)

    class Meta:
        model = FixedAsset
        fields = ('classification','description','registrationnumber','accountingrecognition','depreciation','ipsascategory','subcategory','quantity','location','dateplacedinservice',
        'colour','chassisno','engineserialno','manufacturer','model','modelyear','costcenter','subcostcenter','usagetype','staffid','methodofacquisition',
        'currentstatus','conditions','investmentproperty','fundsource','value','usefullife','comments')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        instance = kwargs.get("instance")
        super(TransportForm,self).__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields['costcenter'].queryset = Devision.objects.filter(status = True)
            
        else:
            self.fields['costcenter'].queryset = Devision.objects.filter(tenant_id=self.request.user.devision.tenant_id.id,status = True)
       
        if instance:
            self.fields['subcostcenter'].queryset = Sub_Devision.objects.filter(devision=instance.costcenter)
            self.fields['subcategory'].queryset = SubCategory.objects.filter(ipsascategory=instance.ipsascategory)
        else:
            self.fields['subcostcenter'].queryset = Sub_Devision.objects.none()
            self.fields['subcategory'].queryset = SubCategory.objects.none()


        if 'costcenter' in self.data:
            try:
                devision = int(self.data.get('costcenter'))
                self.fields['subcostcenter'].queryset = Sub_Devision.objects.filter(
                    devision=devision)
            except (ValueError, TypeError):
                pass
        
        if 'ipsascategory' in self.data:
            try:
                ipsascategory = int(self.data.get('ipsascategory'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(
                    ipsascategory=ipsascategory)
            except (ValueError, TypeError):
                pass


class OutdoorForm(forms.ModelForm):
    years = [(year, str(year)) for year in range(1700, date.today().year + 1)]
    condition = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    usagetype = (
        ('Pool', 'Pool'),
        ('Assigned', 'Assigned'),
    )
    
    status = (
        ('In Use', 'In Use'),
        ('Not in Use', 'Not in Use'),
        ('Retired', 'Retired'),
        ('Disposed', 'Disposed'),
    )
    disposal = (
        ('Sales', 'Sales'),
        ('Auction', 'Auction'),
        ('Donated', 'Donated'),
        ('Trade-in/Exchanged', 'Trade-in/Exchanged'),
        ('Transfer-out to Other Govt Entities', 'Transfer-out to Other Govt Entities'),
        ('Scrapped', 'Scrapped'),
    )
    bcondition=(
        ('Good','Good'),
        ('Needs Repair/Renovation/Servicing','Needs Repair/Renovation/Servicing'),
        ('Irrepairable/Unserviceable','Irrepairable/Unserviceable'),
        ('Not Sighted','Not Sighted'),
    )
    classification = forms.ModelChoiceField(
        queryset=Classification.objects.filter(name='Outdoor Machinery And Equipments').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    description =forms.CharField(label=False,required=True)
    accountingrecognition = forms.ModelChoiceField(
        queryset=AccountingRecognition.objects.filter(classification__name='Outdoor Machinery And Equipments').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    depreciation = forms.ChoiceField(label=False,choices=condition,required=True)
    ipsascategory = forms.ModelChoiceField(
        queryset=IPSASCategory.objects.filter(classification__name='Outdoor Machinery And Equipments').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    quantity=forms.IntegerField(label=False,required=False)
    location =forms.ModelChoiceField(
        queryset=Location.objects.all().order_by('location'),
        label=False,
        empty_label="Select One",
        required=True
    )
    ghanapostgpsaddress = forms.CharField(label=False)
    dateplacedinservice=forms.DateField(widget=NumberInput(attrs={'type': 'date'}),label=False)
    chassisno =forms.CharField(label=False,required=True)
    engineserialno =forms.CharField(label=False)
    manufacturer = forms.ModelChoiceField(
        queryset=Brands.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
    )
    model = forms.CharField(label=False,required=True)
    modelyear =forms.ChoiceField(choices=years, initial=date.today().year,label=False)
    tagno = forms.CharField(label=False,required=True)
    costcenter = forms.ModelChoiceField(
        queryset=Devision.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    subcostcenter =forms.ModelChoiceField(
        queryset=Sub_Devision.objects.all(),
        label=False,
        empty_label="Select One",
        required=True
    )
    
    usagetype= forms.ChoiceField(label=False,choices=usagetype,required=True)
    staffid = forms.CharField(label=False,required=True)
    methodofacquisition =forms.ModelChoiceField(
        queryset=MothodofAcquisition.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    currentstatus = forms.ChoiceField(label=False,choices=status,required=True)
    conditions = forms.ChoiceField(label=False,choices=bcondition,required=True)
    investmentproperty =forms.ChoiceField(label=False,choices=condition,required=True)
    fundsource =forms.ModelChoiceField(
        queryset=SourceOfFunding.objects.all().order_by('funding'),
        label=False,
        empty_label="Select One",
        required=True
    )
    value = forms.FloatField(label=False,required=False,initial=0.0) 
    usefullife = forms.IntegerField(label=False,required=False)
    comments = forms.CharField(
    widget=forms.Textarea(attrs={'maxlength': 255}),
        label=False,required=True)

    class Meta:
        model = FixedAsset
        fields = ('classification','description','accountingrecognition','depreciation','ipsascategory','subcategory','quantity','location','ghanapostgpsaddress','dateplacedinservice',
        'chassisno','engineserialno','manufacturer','model','modelyear','tagno','costcenter','subcostcenter','usagetype','staffid','methodofacquisition',
        'currentstatus','conditions','investmentproperty','fundsource','value','usefullife','comments')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        instance = kwargs.get("instance")
        super(OutdoorForm,self).__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields['costcenter'].queryset = Devision.objects.filter(status = True)
            
        else:
            self.fields['costcenter'].queryset = Devision.objects.filter(tenant_id=self.request.user.devision.tenant_id.id,status = True)
       
        if instance:
            self.fields['subcostcenter'].queryset = Sub_Devision.objects.filter(devision=instance.costcenter)
            self.fields['subcategory'].queryset = SubCategory.objects.filter(ipsascategory=instance.ipsascategory)
        else:
            self.fields['subcostcenter'].queryset = Sub_Devision.objects.none()
            self.fields['subcategory'].queryset = SubCategory.objects.none()


        if 'costcenter' in self.data:
            try:
                devision = int(self.data.get('costcenter'))
                self.fields['subcostcenter'].queryset = Sub_Devision.objects.filter(
                    devision=devision)
            except (ValueError, TypeError):
                pass
        
        if 'ipsascategory' in self.data:
            try:
                ipsascategory = int(self.data.get('ipsascategory'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(
                    ipsascategory=ipsascategory)
            except (ValueError, TypeError):
                pass


class IndoorForm(forms.ModelForm):
    years = [(year, str(year)) for year in range(1700, date.today().year + 1)]
    condition = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    usagetype = (
        ('Pool', 'Pool'),
        ('Assigned', 'Assigned'),
    )
    
    status = (
        ('In Use', 'In Use'),
        ('Not in Use', 'Not in Use'),
        ('Retired', 'Retired'),
        ('Disposed', 'Disposed'),
    )
    disposal = (
        ('Sales', 'Sales'),
        ('Auction', 'Auction'),
        ('Donated', 'Donated'),
        ('Trade-in/Exchanged', 'Trade-in/Exchanged'),
        ('Transfer-out to Other Govt Entities', 'Transfer-out to Other Govt Entities'),
        ('Scrapped', 'Scrapped'),
    )
    bcondition=(
        ('Good','Good'),
        ('Needs Repair/Renovation/Servicing','Needs Repair/Renovation/Servicing'),
        ('Irrepairable/Unserviceable','Irrepairable/Unserviceable'),
        ('Not Sighted','Not Sighted'),
    )
    classification = forms.ModelChoiceField(
        queryset=Classification.objects.filter(name='Indoor').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    description =forms.CharField(label=False,required=True)
    accountingrecognition = forms.ModelChoiceField(
        queryset=AccountingRecognition.objects.filter(classification__name='Indoor').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    depreciation = forms.ChoiceField(label=False,choices=condition,required=True)
    ipsascategory = forms.ModelChoiceField(
        queryset=IPSASCategory.objects.filter(classification__name='Indoor').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    quantity=forms.IntegerField(label=False,required=False)
    location =forms.ModelChoiceField(
        queryset=Location.objects.all().order_by('location'),
        label=False,
        empty_label="Select One",
        required=True
    )
    
    dateplacedinservice=forms.DateField(widget=NumberInput(attrs={'type': 'date'}),label=False)
    chassisno =forms.CharField(label=False,required=True)
    manufacturer = forms.ModelChoiceField(
        queryset=Brands.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
    )
    
    tagno = forms.CharField(label=False,required=True)
    costcenter = forms.ModelChoiceField(
        queryset=Devision.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    subcostcenter =forms.ModelChoiceField(
        queryset=Sub_Devision.objects.all(),
        label=False,
        empty_label="Select One",
        required=True
    )
    
    usagetype= forms.ChoiceField(label=False,choices=usagetype,required=True)
    staffid = forms.CharField(label=False,required=True)
    methodofacquisition =forms.ModelChoiceField(
        queryset=MothodofAcquisition.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    currentstatus = forms.ChoiceField(label=False,choices=status,required=True)
    conditions = forms.ChoiceField(label=False,choices=bcondition,required=True)
    investmentproperty = forms.ChoiceField(label=False,choices=condition,required=True)
    fundsource =forms.ModelChoiceField(
        queryset=SourceOfFunding.objects.all().order_by('funding'),
        label=False,
        empty_label="Select One",
        required=True
    )
    value = forms.FloatField(label=False,required=False,initial=0.0) 
    usefullife = forms.IntegerField(label=False,required=False)
    comments = forms.CharField(
    widget=forms.Textarea(attrs={'maxlength': 255}),
        label=False,required=True)

    class Meta:
        model = FixedAsset
        fields = ('classification','description','accountingrecognition','depreciation','ipsascategory','subcategory','quantity','location','dateplacedinservice',
        'chassisno','manufacturer','tagno','costcenter','subcostcenter','usagetype','staffid','methodofacquisition',
        'currentstatus','conditions','investmentproperty','fundsource','value','usefullife','comments')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        instance = kwargs.get("instance")
        super(IndoorForm,self).__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields['costcenter'].queryset = Devision.objects.filter(status = True)
            
        else:
            self.fields['costcenter'].queryset = Devision.objects.filter(tenant_id=self.request.user.devision.tenant_id.id,status = True)
       
        if instance:
            self.fields['subcostcenter'].queryset = Sub_Devision.objects.filter(devision=instance.costcenter)
            self.fields['subcategory'].queryset = SubCategory.objects.filter(ipsascategory=instance.ipsascategory)
        else:
            self.fields['subcostcenter'].queryset = Sub_Devision.objects.none()
            self.fields['subcategory'].queryset = SubCategory.objects.none()


        if 'costcenter' in self.data:
            try:
                devision = int(self.data.get('costcenter'))
                self.fields['subcostcenter'].queryset = Sub_Devision.objects.filter(
                    devision=devision)
            except (ValueError, TypeError):
                pass
        
        if 'ipsascategory' in self.data:
            try:
                ipsascategory = int(self.data.get('ipsascategory'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(
                    ipsascategory=ipsascategory)
            except (ValueError, TypeError):
                pass


class WIPForm(forms.ModelForm):
    years = [(year, str(year)) for year in range(1700, date.today().year + 1)]
    accountingstatus = (
        ('In-progress','In-progress'),
        ('Completed','Completed'),
        ('Completed and Transferred','Completed and Transferred'),
       
    )
    condition = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    usagetype = (
        ('Pool', 'Pool'),
        ('Assigned', 'Assigned'),
    )
    
    status = (
        ('In Use', 'In Use'),
        ('Not in Use', 'Not in Use'),
        ('Retired', 'Retired'),
        ('Disposed', 'Disposed'),
        ('On-going', 'On-going'),
        ('Abandoned', 'Abandoned'),
        ('Suspended', 'Suspended'),
    )
    disposal = (
        ('Sales', 'Sales'),
        ('Auction', 'Auction'),
        ('Donated', 'Donated'),
        ('Trade-in/Exchanged', 'Trade-in/Exchanged'),
        ('Transfer-out to Other Govt Entities', 'Transfer-out to Other Govt Entities'),
        ('Scrapped', 'Scrapped'),
    )
    bcondition=(
        ('Good','Good'),
        ('Needs Repair/Renovation/Servicing','Needs Repair/Renovation/Servicing'),
        ('Irrepairable/Unserviceable','Irrepairable/Unserviceable'),
        ('Not Sighted','Not Sighted'),
    )
    classification = forms.ModelChoiceField(
        queryset=Classification.objects.filter(name='Wip Or Cip').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    description =forms.CharField(label=False,required=True)
    accountingrecognition = forms.ModelChoiceField(
        queryset=AccountingRecognition.objects.filter(classification__name='Wip Or Cip').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    depreciation = forms.ChoiceField(label=False,choices=condition,required=True)
    ipsascategory = forms.ModelChoiceField(
        queryset=IPSASCategory.objects.filter(classification__name='Wip Or Cip').order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    quantity=forms.IntegerField(label=False,required=False)
    location =forms.ModelChoiceField(
        queryset=Location.objects.all().order_by('location'),
        label=False,
        empty_label="Select One",
        required=True
    )
    ghanapostgpsaddress = forms.CharField(label=False)
    commencement_date=forms.DateField(widget=NumberInput(attrs={'type': 'date'}),label=False)
    expectedcompletion_date=forms.DateField(widget=NumberInput(attrs={'type': 'date'}),label=False)
    costcenter = forms.ModelChoiceField(
        queryset=Devision.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    subcostcenter =forms.ModelChoiceField(
        queryset=Sub_Devision.objects.all(),
        label=False,
        empty_label="Select One",
        required=True
    )
    accountingstatus = forms.ChoiceField(label=False,choices=accountingstatus,required=True)
    usagetype= forms.ChoiceField(label=False,choices=usagetype,required=True)
    staffid = forms.CharField(label=False,required=True)
    methodofacquisition =forms.ModelChoiceField(
        queryset=MothodofAcquisition.objects.all().order_by('name'),
        label=False,
        empty_label="Select One",
        required=True
    )
    currentstatus = forms.ChoiceField(label=False,choices=status,required=True)
    
    fundsource =forms.ModelChoiceField(
        queryset=SourceOfFunding.objects.all().order_by('funding'),
        label=False,
        empty_label="Select One",
        required=True
    )
    costbf = forms.FloatField(label=False,required=False,initial=0.0) 
    currentperiodcost = forms.FloatField(label=False,required=False,initial=0.0) 
    costcf = forms.FloatField(label=False,required=False,initial=0.0) 
    comments = forms.CharField(
    widget=forms.Textarea(attrs={'maxlength': 255}),
        label=False,required=True)

    class Meta:
        model = FixedAsset
        fields = ('classification','description','accountingrecognition','depreciation','ipsascategory','quantity','location','ghanapostgpsaddress','commencement_date',
        'expectedcompletion_date','costcenter','subcostcenter','accountingstatus','usagetype','staffid','methodofacquisition',
        'currentstatus','fundsource','costbf','currentperiodcost','costcf','comments')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        instance = kwargs.get("instance")
        super(WIPForm,self).__init__(*args, **kwargs)
        if self.request.user.is_superuser:
            self.fields['costcenter'].queryset = Devision.objects.filter(status = True)
            
        else:
            self.fields['costcenter'].queryset = Devision.objects.filter(tenant_id=self.request.user.devision.tenant_id.id,status = True)
       
        if instance:
            self.fields['subcostcenter'].queryset = Sub_Devision.objects.filter(devision=instance.costcenter)
            
        else:
            self.fields['subcostcenter'].queryset = Sub_Devision.objects.none()
            


        if 'costcenter' in self.data:
            try:
                devision = int(self.data.get('costcenter'))
                self.fields['subcostcenter'].queryset = Sub_Devision.objects.filter(
                    devision=devision)
            except (ValueError, TypeError):
                pass
        
        