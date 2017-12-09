from django.shortcuts import render

def Apresentacao(request):
	return render (request, 'index.html')
