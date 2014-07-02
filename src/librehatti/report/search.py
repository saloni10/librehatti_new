from django.shortcuts import *
from forms import *

"""
view to display "index.html" i.e. the search interface or form
"""
def search(request):
    client_form = ClientForm()
    order_form = OrderForm()
    add_constraints=  AddConstraints()
    temp = {'client_form':client_form,'order_form':order_form, 
    'add_constraints':add_constraints}
    return render(request, 'index.html',temp)
