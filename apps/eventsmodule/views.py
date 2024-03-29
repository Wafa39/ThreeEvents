from django.shortcuts import render,redirect
from .models import Events


def index(request):
    return render(request, 'eventsmodule/index.html')

def eventscategories(request):
    events = Events.objects.filter(price__lte = 100).order_by('-price')
    print(str(len(Events)))
    return render(request, 'eventsmodule/eventscategories.html', {'events': events})

def filtterevents(request):
   
   if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isprice = request.POST.get('option2')
        selected = request.POST.get('selectedgenre')
        event = Events.objects.filter(categoryname__icontains='n')
        event2 = event.filter(price__lte = 100)
        print(f"selected thing = {selected}")

        # now filter
        eventscategorie = _getEvents()
        neweventscategorie = []
        for item in eventscategorie:
            contained = False
            if isTitle and string in item['categoryname'].lower(): contained = True
            if not contained and isprice and string in item['price'].lower():contained = True
            if contained: neweventscategorie.append(item)

        return render(request, 'eventsmodule/eventscategories.html', {'eventscategorie':neweventscategorie})
   
   return render(request, 'eventsmodule/search.html',{})

def eventscategory(request,EventId):
    category1 = {'id':12345,'categoryname':'Wedding n Event','pakagedetails':'...........','price':'500'} 
    category2 = {'id':67899,'categoryname':'Birthday Event','pakagedetails':'...........','price':'300'}
    category3 = {'id':12188,'categoryname':'Graduation n Event','pakagedetails':'...........','price':'300'} 

    targetcategory=None

    if category1['id'] == EventId: targetcategory=category1
    if category2['id']==EventId:targetcategory=category2
    if category3['id']==EventId:targetcategory=category3
    if targetcategory == None : return redirect('/events')
    
    context={'eventscategory':targetcategory}
    return render(request, 'eventsmodule/eventscategory.html',context)

def _getEvents():
    eventscategorie =[]
    category1 = {'id':12345,'categoryname':'Wedding n Event','pakagedetails':'...........','price':'500'} 
    eventscategorie.append(category1)
    category2 = {'id':67899,'categoryname':'Birthday Event','pakagedetails':'...........','price':'300'}
    eventscategorie.append(category2)
    category3 = {'id':12188,'categoryname':'Graduation n Event','pakagedetails':'...........','price':'300'} 
    eventscategorie.append(category3)
    return eventscategorie