 # Create your views here.
from django.http import HttpResponse
from useraccounts.models import *
from helper import *
from forms import *
from django.shortcuts import render
from librehatti.catalog.models import *
import datetime
from django.db.models import Sum

def bill(request):
    
    purchased_item = PurchasedItem.objects.get(pk=1)
    purchase_order = PurchaseOrder.objects.get(pk=2)
    purchaseditem= PurchasedItem.objects.values('item','price','qty')
    per_price = purchased_item.item.price
    total=PurchasedItem.objects.filter(id=1).aggregate(Sum('price'))
    date= datetime.datetime.now()
    bill_date=purchase_order.date_time      
    delivery_address=purchase_order.delivery_address
    organisation=purchase_order.organisation
    buyer_id=purchase_order.buyer_id
    
    return render(request, 'bill.html', { 'STC_No':'1', 'PAN_No' :'12',
    'date': date, 'delivery_address' : delivery_address, 
    'Organisation' : organisation,'buyer_id' : buyer_id, 'L_No.': '123',
    'bill_date': bill_date,'purchaseditem' : purchaseditem,'per_price': per_price, 'total_cost': total, 'p': purchased_item })




def index(request):
  client_form = ClientForm()
  order_form = OrderForm()
  order_type=OrderType()
  temp = {'client_form':client_form,'order_form':order_form,'order_type':order_type}
  return render(request, 'index.html',temp)


def display(request):
    title = 'Search'
    results=[]
    s=[]
    avail_list = ['user__username', 'address__city','telephone','date_joined','company']
    avail_list2=['qty','item__price','item__category','item__name','discount','purchase_order__is_debit']
    #avail_list3=['is_debit']
    if 'Client' in request.GET:
        if 'client_fields' in request.GET:
           info = request.GET.getlist('client_fields')
           for i in avail_list:
              if i in info:
                r = Customer.objects.values(i)
                results.append(r)
                query_string = ''
                found_entries = None
                if ('q' in request.GET) and request.GET['q'].strip():
                  query_string = request.GET['q']
                  entry_query = get_query(query_string,info)
                  found_entries = Customer.objects.filter(entry_query)
                  for i in found_entries:
                    al=i._meta.get_all_field_names()
                    for j in al:  
                      if j in info:
                        o = Customer.objects.values(j)
                        s.append(o)


                    

    if 'Order' in request.GET:        
       if 'order' in request.GET:
           order = request.GET.getlist('order')
           for j in avail_list2:
              if j and 'is_debit' in order:
                s = PurchasedItem.objects.filter(purchase_order__is_debit=True).values(j)
                results.append(s)
              else:  
                s = PurchasedItem.objects.filter(purchase_order__is_debit=False).values(j)
                results.append(s)
         
    if 'q' in request.GET:
       title = request.GET['q']
 
    return render(request, 'display.html', {'results':results,'title': title,'found_entries':found_entries ,'info':info,'al':al})

