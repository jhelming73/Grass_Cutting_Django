from django.shortcuts import render, redirect, reverse
from .models import Lawnmower, Fertilizer
from .forms import LawnmowerForm, FertilizerForm
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

def fertilizer_detail(request, pk):
    fertilizer = Fertilizer.objects.get(id=pk)

    return render(request, 'grass_cutting/fertilizer_detail.html', {'fertilizer': fertilizer})

def fertilizer_create(request):
    if request.method == 'POST':
        form = FertilizerForm(request.POST)
        if form.is_valid():
            fertilizer = form.save()
            return redirect('fertilizer_detail', pk=fertilizer.pk)
    else:
        form = FertilizerForm()
    return render(request, 'grass_cutting/fertilizer_form.html', {'form': form})

def fertilizer_edit(request, pk):
    fertilizer = Fertilizer.objects.get(pk=pk)
    if request.method == "POST":
        form = FertilizerForm(request.POST, instance=fertilizer)
        if form.is_valid():
            fertilizer = form.save()
            return redirect('fertilizer_detail', pk=fertilizer.pk)
    else:
        form = FertilizerForm(instance=fertilizer)
    return render(request, 'grass_cutting/fertilizer_form.html', {'form': form})

def fertilizer_delete(request, pk):
    Fertilizer.objects.get(id=pk).delete()
    return redirect('fertilizer_list')