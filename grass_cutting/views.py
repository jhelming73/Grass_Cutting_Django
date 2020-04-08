from django.shortcuts import render, redirect, reverse
from .models import Lawnmower, Fertilizer
from .forms import LawnmowerForm
# Create your views here.

def lawnmower_list(request):
    lawnmowers = Lawnmower.objects.all()

    return render(request,'grass_cutting/lawnmower_list.html', {'lawnmowers': lawnmowers})

def lawnmower_detail(request, pk):
    lawnmower = Lawnmower.objects.get(id=pk)

    return render(request, 'grass_cutting/lawnmower_detail.html', {'lawnmower': lawnmower})

def lawnmower_create(request):
    if request.method == 'POST':
        form = LawnmowerForm(request.POST)
        if form.is_valid():
            lawnmower = form.save()
            return redirect('lawnmower_detail', pk=lawnmower.pk)
    else:
        form = LawnmowerForm()
    return render(request, 'grass_cutting/lawnmower_form.html', {'form': form})

def lawnmower_edit(request, pk):
    lawnmower = Lawnmower.objects.get(pk=pk)
    if request.method == "POST":
        form = LawnmowerForm(request.POST, instance=lawnmower)
        if form.is_valid():
            lawnmower = form.save()
            return redirect('lawnmower_detail', pk=lawnmower.pk)
    else:
        form = LawnmowerForm(instance=lawnmower)
    return render(request, 'grass_cutting/lawnmower_form.html', {'form': form})

def lawnmower_delete(request, pk):
    Lawnmower.objects.get(id=pk).delete()
    return redirect('lawnmower_list')

def fertilizer_list(request):
    fertilizers = Fertilizer.objects.all()
    return render(request, 'grass_cutting/fertilizer_list.html', {'fertilizers': fertilizers})