from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Record

def home(request):
    return render(request, 'home.html')

def name(request):
    top_record = Record.objects.order_by('-score').first()
    if request.method == 'POST':
        player_name = request.POST.get('name')
        request.session['player_name'] = player_name
        return redirect('game')
    return render(request, 'name.html', {'top_record': top_record})

def game(request):
    return render(request, 'game.html')

def save_score(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        score = request.POST.get('score')
        new_record = Record(name=name, score=score)
        new_record.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)

def gameover(request):
    top_records = Record.objects.order_by('-score')[:3]
    
   
    return render(request, 'gameover.html', {'top_records': top_records})