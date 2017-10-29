from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from . import forms
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

# Create your views here.
#from django
from . import models
"""
def add_comments(request):
    if 'application/x-www-form-urlencoded' in request.META['CONTENT_TYPE']:
        print 'hi'
        data = json.loads(request.body)
        comment = data.get('comment', None)
        id = data.get('id', None)
        title = data.get('title', None)

        post = Post.objects.get(id = id)
        com = Comment()
        com. comments = comment
        com.title = post
        com.save()

"""
#def adata():

#    d = {}
    #received_json_data = json.loads(request.body.decode("utf-8"))


def doc_date(request):
    form = forms.docd()
    return render(request,'health/date.html',{'form':form})

class basicView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        return HttpResponse("CLLL")

class PatientListView(ListView):
    model = models.Patient
    query = model.objects.all()
    context_object_name = 'stuff'

    template_name = "health/patient_list.html"
    def get(self,request,*args,**kwargs):
        stuff = self.get_queryset()
        """if request.GET.get(model.name):
            q = request.GET.get(model.name)
            stuff = stuff.filter(user__icontains=q)"""
        return render(request, self.template_name, {'stuff': stuff})

    def post(self, request, *args, **kwargs):
        """
        write script here

        """
        print(request.POST.get('initial_date'))
        stuff = self.get_queryset()

        return render(request, self.template_name,{'stuff':stuff})

    """def f(self,**kk):
        #if self.method == 'POST':
        context = super(PatientListView, self).f(**kk)
            #form = forms.docd(request.POST)
        print(context)
        if form.is_valid():
            print("YUP!!")
            print(form.cleaned_data['initial_date'])
            print(form.cleaned_data['final_date'])"""

class SensorListView(ListView):
    model = models.Sensor

class PatientDetailView(DetailView):
    context_object_name = 'patient_details'
    model = models.Patient
    template_name = 'health/patient_detail.html'

class SensorDetailView(DetailView):
    context_object_name = 'sensor_details'
    model = models.Sensor
    template_name = 'health/sensor_detail.html'

"""class PatientCreateView(CreateView):
    fields = ("name","age","location")
    model = models.Patient

class SensorCreateView(CreateView):
    fields = ("name","patient")
    model = models.Sensor"""
