from django.shortcuts import render,redirect

def index(request):
    return render(request, 'eventsmodule/index.html')

def eventscategories(request):
    return render(request, 'eventsmodule/eventscategories.html')

def eventscategory(request,EventId):
    category1 = {'id':12345,'categoryname':'Wedding Event','pakagedetails':'...........'} 
    category2 = {'id':67899,'categoryname':'Birthday Event','pakagedetails':'...........'}
    category3 = {'id':12188,'categoryname':'Graduation Event','pakagedetails':'...........'} 

    targetcategory=None

    if category1['id'] == EventId: targetcategory=category1
    if category2['id']==EventId:targetcategory=category2
    if category3['id']==EventId:targetcategory=category3
    if targetcategory == None : return redirect('/events')
    
    context={'eventscategory':targetcategory}
    return render(request, 'eventsmodule/eventscategory.html',context)