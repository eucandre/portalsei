from django.shortcuts import render

def Apresentacao(request):
	return render (request, 'apps/index.html')
