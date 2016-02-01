from django.shortcuts import render#, get_object_or_404
from django.utils import timezone
from .models import counter_data, counter

def counter_data_list(request):
    #objects.filter(reg_date__lte=timezone.now())
    data = counter_data.objects.order_by('-reg_date')
    return render(request, 'bills/counter_data_list.html', {'data': data})

def counter_data_by(request, pk):
    #data = get_object_or_404(counter, pk=pk)
    cdata = counter.objects.get(pk=pk)
    fdata = counter_data.objects.filter(counter_id=pk).order_by('-reg_date')
    data = {'cdata': cdata, 'fdata': fdata}
    return render(request, 'bills/counter_detail.html', {'data': data})
