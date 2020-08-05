from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"BMI.html")
def getdata(request):
    h = request.GET['Height']
    w = request.GET['Weight']
    h= float(h)
    w = float(w)
    res = w/(h*h)
    return render (request, "BMIcal.html", {"Height": h, "Weight": w, "Result": res})
