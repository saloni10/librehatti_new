 # Create your views here.
from django.http import HttpResponse
from useraccounts.models import *
from helper import *
from forms import *
from django.shortcuts import *
from librehatti.catalog.models import *
from django.db.models import Sum

def bill(request):
    purchase_order = PurchaseOrder.objects.get(buyer_id_id=6)
    purchased_item = PurchasedItem.objects.filter(purchase_order_id=6).values(
    'item__name' ,'qty','item__price','price')	
    total = PurchasedItem.objects.filter(purchase_order_id=6).aggregate(Sum('price')).get('price__sum', 0.00)
    return render(request, 'bill.html', { 'STC_No' :'1','PAN_No' :'12', 'L_No': '123',
     'purchase_order':purchase_order, 'purchased_item' : purchased_item, 
     'total_cost': total  })



def index(request):
  client_form = ClientForm()
  order_form = OrderForm()
  
  add_constraints=  AddConstraints()
  temp = {'client_form':client_form,'order_form':order_form, 'add_constraints':add_constraints}
  return render(request, 'index.html',temp)



def display(request):
    
    title = 'Search'
    results=[]
    result_fields = []
    selected_fields_client = request.GET.getlist('client_fields')
    selected_fields_order = request.GET.getlist('order')
    selected_fields_constraints = request.GET.getlist('additional_constraints')
    avail_list_dict_client = {'name':'user__username', 'city':'address__city','phone':'telephone','joining date':'date_joined','company':'company'}
    avail_list_dict_order = {'name':'purchase_order__buyer_id__user__username','city':'purchase_order__buyer_id__address__city','quantity':'qty','unit price':'item__price',
		'item':'item__name','discount':'discount','debit':'purchase_order__is_debit','total price':'price'}
	
    avail_list = []
    avail_list2=[]
    #avail_list3=['is_debit']
    start_date = request.GET['start_date']
    end_date = request.GET['end_date']  
    if 'Client' in request.GET:
        result_fields.append(selected_fields_client)
        search_fields = []
        for value in selected_fields_client:
            search_value = avail_list_dict_client[value]
            search_fields.append(search_value)

        query_string = ''
        found_entries = None
        if ('search' in request.GET) and request.GET['search'].strip():
            query_string = request.GET['search']
            entry_query = get_query(query_string,search_fields)
            found_entries = Customer.objects.filter(entry_query)
            for entries in found_entries:
                temp = []
                if 'date' in selected_fields_constraints:
                    for value in search_fields:
                       obj = Customer.objects.filter(id=entries.id ,date_joined__range=(start_date,end_date) ).values(value)
                       for temp_result in obj:
                          temp.append(temp_result)
                else:                    
                    for value in search_fields:
                       obj = Customer.objects.filter(id=entries.id).values(value)
                       for temp_result in obj:
                          temp.append(temp_result)
                results.append(temp)
                    

    if 'Order' in request.GET:
        result_fields.append(selected_fields_order)
        search_fields = []
        for value in selected_fields_order:
            search_value = avail_list_dict_order[value]
            search_fields.append(search_value)
        query_string = ''
        found_entries = None
        if ('search' in request.GET) and request.GET['search'].strip():
            query_string = request.GET['search']
            entry_query = get_query(query_string,search_fields)
            found_entries = PurchasedItem.objects.filter(entry_query)
            for entries in found_entries:
                temp = []
                if 'debit' and 'date' in selected_fields_order:
                    for value in search_fields:
                        obj = PurchasedItem.objects.filter(id=entries.id,purchase_order__is_debit = 1,purchase_order__date_time__range=(start_date,end_date)).values(value)
                        for temp_result in obj:
                            temp.append(temp_result)
                elif 'date' and not 'debit' in selected_fields_order:
                    for value in search_fields:
                        obj = PurchasedItem.objects.filter(id=entries.id,purchase_order__date_time__range=(start_date,end_date)).values(value)
                        for temp_result in obj:
                            temp.append(temp_result)
                elif 'debit' and not 'date' in selected_fields_order:
                    for value in search_fields:
                        obj = PurchasedItem.objects.filter(id=entries.id,purchase_order__is_debit = 1).values(value)
                        for temp_result in obj:
                            temp.append(temp_result)  
                                                                           
                else:
                    for value in search_fields:
                        obj = PurchasedItem.objects.filter(id=entries.id).values(value)
                        for temp_result in obj:
                            temp.append(temp_result)
                results.append(temp)
                
               
         
    if 'search' in request.GET:
       title = request.GET['search']
    return render(request, 'display.html', {'results':results,'title': title,'result_fields':result_fields})



