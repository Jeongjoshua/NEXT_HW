from django.shortcuts import render, redirect
from .models import Record
import time

# Create your views here.
def home(request):
    return render(request,'home.html')

def name(request):
     # 현재 1등 기록 가져오기
    top_record = Record.objects.order_by('-score').first()
    if request.method == 'POST':
        player_name = request.POST.get('name')
        request.session['player_name'] = player_name
        request.session['start_time'] = time.time()
        return redirect('game')
    return render(request, 'name.html', {'top_record': top_record})

def game(request):
    return render(request,'game.html')

def gameover(request):
    return render(request, 'gameover.html')