from django.shortcuts import render

# Index view
def index(request):
	return render(request, 'index.html', {
		'project_name': 'django_5',
		'app_name': 'web',
	})
