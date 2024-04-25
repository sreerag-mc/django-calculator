from django.shortcuts import render

def calculator(request):
    return render(request, 'index.html')

def submit_query(request):
    q = request.GET.get('query', '')
    try:
        ans = eval(q)
        context = {
            "q": q,
            "ans": ans,
            "error": False
        }
    except Exception as e:
        context = {
            "error_message": str(e),
            "error": True,
        }
    return render(request, 'index.html', context=context)







