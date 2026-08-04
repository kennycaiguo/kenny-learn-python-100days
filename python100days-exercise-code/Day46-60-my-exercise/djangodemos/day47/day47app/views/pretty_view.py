from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render

from day47app.models import PrettyNumber

class PrettyNumForm(forms.ModelForm):
    class Meta:
        model = PrettyNumber
        fields = '__all__'
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs={"class":"form-control","placeholder":field.label}

def pretty_list(req):
    pretty_nums = PrettyNumber.objects.all().order_by("-id")
    return render(req,'pretty_list.html',{"pretty_nums":pretty_nums})

def pretty_add(req):
    # get method
    if req.method == 'GET':
        form = PrettyNumForm()
        return render(req,"pretty_add.html",{"form":form})
    # post method
    form = PrettyNumForm(data=req.POST)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")
    return  render(req,"pretty_add.html",{"form":form})