from django.shortcuts import render,redirect
from .models import Events


def index(request):
    return render(request, 'eventsmodule/index.html')

def eventscategories(request):
    return render(request, 'eventsmodule/eventscategories.html', {'eventscategorie': _getEvents()})


def filtterevents(request):
   
   if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        istype = request.POST.get('option2')
        isprice = request.POST.get('option3')
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
    category1 = {'id':12345,'categoryname':'Wedding Event','pakagetype':'Diamond','pakagedetails':'...........','price':'500'} 
    category2 = {'id':67899,'categoryname':'Wedding Event','pakagetype':'Platinum','pakagedetails':'...........','price':'300'}
    category3 = {'id':12188,'categoryname':'Wedding Event','pakagetype':'Gold','pakagedetails':'...........','price':'200'} 
    category4 = {'id':12354,'categoryname':'Wedding Event','pakagetype':'Silver','pakagedetails':'...........','price':'100'} 
    category5 = {'id':67859,'categoryname':'Birthday Event','pakagetype':'Diamond','pakagedetails':'...........','price':'500'}
    category6 = {'id':12588,'categoryname':'Birthday Event','pakagetype':'Platinum','pakagedetails':'...........','price':'300'} 
    category7 = {'id':12335,'categoryname':'Birthday Event','pakagetype':'Gold','pakagedetails':'...........','price':'200'} 
    category8 = {'id':63399,'categoryname':'Birthday Event','pakagetype':'Silver','pakagedetails':'...........','price':'100'}
    category9 = {'id':12938,'categoryname':'Graduation Event','pakagetype':'Diamond','pakagedetails':'...........','price':'500'} 
    category10 = {'id':12385,'categoryname':'Graduation Event','pakagetype':'Platinum','pakagedetails':'...........','price':'300'} 
    category11 = {'id':67239,'categoryname':'Graduation Event','pakagetype':'Gold','pakagedetails':'...........','price':'200'}
    category12 = {'id':12328,'categoryname':'Graduation Event','pakagetype':'Silver','pakagedetails':'...........','price':'100'} 
    targetcategory=None

    if category1['id'] == EventId: targetcategory=category1
    if category2['id']==EventId:targetcategory=category2
    if category3['id']==EventId:targetcategory=category3
    if category4['id'] == EventId: targetcategory=category4
    if category5['id']==EventId:targetcategory=category5
    if category6['id']==EventId:targetcategory=category6
    if category7['id'] == EventId: targetcategory=category7
    if category8['id']==EventId:targetcategory=category8
    if category9['id']==EventId:targetcategory=category9
    if category10['id'] == EventId: targetcategory=category10
    if category11['id']==EventId:targetcategory=category11
    if category12['id']==EventId:targetcategory=category12
    if targetcategory == None : return redirect('/events')
    
    context={'eventscategory':targetcategory}
    return render(request, 'eventsmodule/eventscategory.html',context)

def _getEvents():
    eventscategorie =[]
    category1 = {'id':12345,'categoryname':'Wedding Event','pakagetype':'Diamond','pakagedetails':'banners,centerpieces,candles,backdrops,table runners,flower arrangements,balloons,table setting,tables','price':'500'} 
    eventscategorie.append(category1)
    category2 = {'id':67899,'categoryname':'Wedding Event','pakagetype':'Platinum','pakagedetails':'banners,centerpieces,candles,backdrops,table runners,flower arrangements,balloons','price':'300'}
    eventscategorie.append(category2)
    category3 = {'id':12188,'categoryname':'Wedding Event','pakagetype':'Gold','pakagedetails':'banners,centerpieces,candles,backdrops,flower arrangements,balloons','price':'200'} 
    eventscategorie.append(category3)
    category4 = {'id':12354,'categoryname':'Wedding Event','pakagetype':'Silver','pakagedetails':'banners,centerpieces,candles,backdrops,flower arrangements','price':'100'} 
    eventscategorie.append(category4)
    category5 = {'id':67859,'categoryname':'Birthday Event','pakagetype':'Diamond','pakagedetails':'banners,centerpieces,candles,backdrops,table runners,flower arrangements,balloons,table setting,tables','price':'500'}
    eventscategorie.append(category5)
    category6 = {'id':12588,'categoryname':'Birthday Event','pakagetype':'Platinum','pakagedetails':'banners,centerpieces,candles,backdrops,table runners,flower arrangements,balloons','price':'300'} 
    eventscategorie.append(category6)
    category7 = {'id':12335,'categoryname':'Birthday Event','pakagetype':'Gold','pakagedetails':'banners,centerpieces,candles,backdrops,flower arrangementsm,balloons','price':'200'} 
    eventscategorie.append(category7)
    category8 = {'id':63399,'categoryname':'Birthday Event','pakagetype':'Silver','pakagedetails':'banners,centerpieces,candles,backdrops,flower arrangements','price':'100'}
    eventscategorie.append(category8)
    category9 = {'id':12938,'categoryname':'Graduation Event','pakagetype':'Diamond','pakagedetails':'banners,centerpieces,candles,backdrops,table runners,flower arrangements,balloons,table setting,tables','price':'500'} 
    eventscategorie.append(category9)
    category10 = {'id':12385,'categoryname':'Graduation Event','pakagetype':'Platinum','pakagedetails':'banners,centerpieces,candles,backdrops,table runners,flower arrangements,balloons','price':'300'} 
    eventscategorie.append(category10)
    category11 = {'id':67239,'categoryname':'Graduation Event','pakagetype':'Gold','pakagedetails':'banners,centerpieces,candles,backdrops,flower arrangements,balloons','price':'200'}
    eventscategorie.append(category11)
    category12 = {'id':12328,'categoryname':'Graduation Event','pakagetype':'Silver','pakagedetails':'banners,centerpieces,candles,backdrops,flower arrangements','price':'100'} 
    eventscategorie.append(category12)
    
    return eventscategorie