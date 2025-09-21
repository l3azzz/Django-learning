from django.shortcuts import render

def index(request):
	return render(request, 'index.html', {
		'project_name': 'wibbitz',
		'app_name': 'web'
	})
