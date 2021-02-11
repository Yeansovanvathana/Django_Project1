from django.shortcuts import render
def form(request):

    return render(request,"form.html")
# Create your views here.
def output(request):
    name = request.GET['name']
    reg = request.GET['regno']
    dep = request.GET['dep']
    phone = request.GET['phone']
    print(name)
    return render(request,"output.html",{'name':name,'regno':reg,'dep':dep,'phone':phone})
