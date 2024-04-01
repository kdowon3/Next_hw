from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    only_text = len(text.replace(' ', ''))
    word_count = len(text.split())  
    return render(request, 'result.html', {
        'text': text,
        'total_len': total_len,
        'only_text': only_text,
        'word_count': word_count, 
    })