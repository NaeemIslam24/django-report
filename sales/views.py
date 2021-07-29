from django.shortcuts import render
from . models import *
from . forms import SaleSearchForm
# Create your views here.


def home_view(request):

    template = 'sale/home.html'
    form = SaleSearchForm(request.POST or None)
    if request.method == 'POST':

        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        print(date_from)

        qs = Sale.objects.filter(created__date=date_from)
        obj = Sale.objects.get(id=2)

        print('This is a test', qs)
        print('This is a test2', obj)

    context = {
        'search_form': form,
    }
    return render(request, context=context, template_name=template)


def sale_list_view(request):

    template = 'sale/main.html'

    qs = Sale.objects.all()
    context = {
        'object_list': qs
    }
    return render(request, context=context, template_name=template)


def sale_detail_view(request, pk):

    template = 'sale/detail.html'
    qs = Sale.objects.get(pk=pk)
    context = {
        'object': qs
    }
    return render(request, context=context, template_name=template)
