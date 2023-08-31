from django.shortcuts import render

# Create your views here.
def task_view(request):
    dynamic_data = "This is dynamic data!"
    context = {'dynamic_data': dynamic_data}
    return render(request, 'task.html', context)
  