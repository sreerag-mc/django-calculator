from django.shortcuts import render
from django.http import HttpResponse

def calculator(request):
	if request.method == 'POST':
		result = request.POST.get('result', '')
		return render(request, 'index.html', {'result': result})

	return render(request, 'index.html')


def result(request):
	num1 = int(request.GET.get('number1'))
	num2 = int(request.GET.get('number2'))

	if request.GET.get('add') == "":
		ans = num1 + num2

	elif request.GET.get('subtract') == "":
		ans = num1 - num2

	elif request.GET.get('multiply') == "":
		ans = num1 * num2

	else:
		ans = num1 / num2

	return render(request, 'result.html', {'ans': ans})





