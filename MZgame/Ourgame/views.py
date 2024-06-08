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
    player_name = request.session.get('player_name')
    my_record = Record.objects.filter(name=player_name).order_by('-id').first()  # 마지막 기록 가져오기
    top_records = Record.objects.order_by('-score')[:3]  # 상위 3개의 기록
    player_rank = list(Record.objects.order_by('-score')).index(my_record) + 1  # 플레이어 순위 계산

    context = {
        'player_name': player_name,
        'my_record': my_record,
        'top_records': top_records,
        'player_rank': player_rank,
    }
    return render(request, 'gameover.html', context)