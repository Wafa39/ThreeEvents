from django.shortcuts import render,redirect

def index(request):
    return render(request, 'eventsmodule/index.html')

def eventscategories(request):
    return render(request, 'eventsmodule/eventscategories.html',{'eventscategories':_getEvents})

def filtterevents(request):
   
   if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isprice = request.POST.get('option2')
        # now filter
        eventscategorie = _getEvents()
        neweventscategorie = []
        for item in eventscategorie:
            contained = False
            if isTitle and string in item['categoryname'].lower(): contained = True
            if not contained and isprice and string in item['pakagedetails'].lower():contained = True
            if contained: neweventscategorie.append(item)

        return render(request, 'eventsmodule/eventscategories.html', {'eventscategorie':neweventscategorie})
   
   return render(request, 'eventsmodule/search.html',{})

def eventscategory(request,EventId):
    category1 = {'id':12345,'categoryname':'Wedding n Event','pakagedetails':'...........'} 
    category2 = {'id':67899,'categoryname':'Birthday Event','pakagedetails':'...........'}
    category3 = {'id':12188,'categoryname':'Graduation n Event','pakagedetails':'...........'} 

    targetcategory=None

    if category1['id'] == EventId: targetcategory=category1
    if category2['id']==EventId:targetcategory=category2
    if category3['id']==EventId:targetcategory=category3
    if targetcategory == None : return redirect('/events')
    
    context={'eventscategory':targetcategory}
    return render(request, 'eventsmodule/eventscategory.html',context)

def _getEvents():
    eventscategorie =[]
    category1 = {'id':12345,'categoryname':'Wedding Event','pakagedetails':'...........'} 
    eventscategorie.append(category1)
    category2 = {'id':67899,'categoryname':'Birthday Event','pakagedetails':'...........'}
    eventscategorie.append(category2)
    category3 = {'id':12188,'categoryname':'Graduation Event','pakagedetails':'...........'} 
    eventscategorie.append(category3)
    return eventscategorie