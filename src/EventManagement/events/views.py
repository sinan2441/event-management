from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.timezone import now

from events.forms import EventForm
from events.models import Event


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EventForm()
    return render(request, 'AddEvent.html', {'form': form})


def list_events(request):
    events = Event.objects.filter(date__gte=now()).order_by('date')
    return render(request, 'list.html', {'events': events})


def edit_event(request,pk):
    instance_edit = Event.objects.get(pk=pk)
    form = EventForm(request.POST or None, instance=instance_edit)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, 'AddEvent.html', {'form': form})


def delete_event(request,pk):
    instance = Event.objects.get(pk=pk)
    instance.delete()
    form = Event.objects.filter(date__gte=now()).order_by('date')
    return render(request, 'list.html', {'events': form})


def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list')
    else:
        form = AuthenticationForm()
    return render(request, 'sign_in.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('signin')
