from django.shortcuts import render

# Create your views here.

def index(request):
  context_dict = {'message': 'Hello World!'}
  return render(request, 'drawings/index.html', context_dict)