from django.shortcuts import render

def name(request):
    return render(request,'name.html')
def result(request):
    dict1=request.GET
    res=dict1['names']
    return render(request,'output.html',{'output':res})