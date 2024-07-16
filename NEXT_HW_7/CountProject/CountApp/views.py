from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text=request.POST['text']
    total_len=len(text) 
    total_len2 = len(text.replace(" ", ""))
    return render(request, 'result.html',{'total_len': total_len,'total_len2': total_len2, 'text': text},)

