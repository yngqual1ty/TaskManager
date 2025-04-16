from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import IsOwnerOrAdmin

from .models import Task
from .forms import CreateTaskForm, EditTaskForm

from django.views.generic import ListView
from django.db.models import Q



from rest_framework import generics
from .serializers import TaskSerializer
import django_filters
from rest_framework.filters import OrderingFilter

@login_required
def tasks(request):
    task_list = Task.objects.filter(user=request.user)
    if request.user.is_authenticated:
        return render(request, 'main/tasks.html', {'tasks': task_list})
    else:
        return redirect('users:login')


def homepage(request):
    return render(request, 'main/homepage.html')

@login_required
def create_task(request):
    error = ''
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user_id = request.user.id
            task.save()
            return redirect('main:tasks')
        else:
            error = 'Неверно заполнен дедлайн'
    form = CreateTaskForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/create_task.html', context)


@login_required
def edit_task(request, task_id):
    error = ''
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('main:tasks')
        else:
            error = 'Неверно заполнен дедлайн'
    form = EditTaskForm(instance=task)
    context = {'form': form, 'task': task, 'error': error}
    return render(request, 'main/edit_task.html', context)


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        return JsonResponse({"success": True})

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)


@login_required
def view_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return render(request, 'main/view_task.html', {'task': task})


@login_required
def toggle_task_completion(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.is_completed = not task.is_completed  # Переключаем состояние
        task.save()
        return JsonResponse({"success": True, "is_completed": task.is_completed})

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)




class SearchResults(ListView):
    model = Task
    template_name = 'main/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Task.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(priority__icontains=query), user=self.request.user
        )
        return object_list



class TaskFilter(django_filters.FilterSet):
    title = django_filters.filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = django_filters.filters.CharFilter(field_name='description', lookup_expr='icontains')
    deadline = django_filters.filters.DateTimeFilter(field_name='deadline', lookup_expr='lte')
    priority = django_filters.filters.CharFilter(field_name='priority', lookup_expr='icontains')
    is_completed = django_filters.filters.BooleanFilter(field_name='is_completed')

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority', 'is_completed']


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, OrderingFilter)
    filterset_class = TaskFilter

    ordering_fields = ('title', 'description', 'deadline', 'priority', 'is_completed')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)