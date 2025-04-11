from django.shortcuts import render, redirect
from rest_framework.permissions import AllowAny, IsAuthenticated

from .permissions import IsOwnerOrAdmin, IsAdmin

from .forms import RegistrationForm, LoginForm, EditProfileForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required



from rest_framework import viewsets, generics

from .models import CustomUser
from .serializers import CustomUserSerializer, RegisterSerializer, ProfileSerializer

def login_view(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:homepage')  # Перенаправление на главную страницу
            else:
                error = 'Неверное имя пользователя или пароль.'
        else:
            error = form.errors
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form, 'error': error})


def signup(request):
    error = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('main:homepage')
        else:
            error = form.errors
    else:
        form = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': form, "error": error})


@login_required
def logout_view(request):
    logout(request)
    return redirect('main:homepage')


from django.shortcuts import render, redirect
from .forms import EditProfileForm

@login_required
def profile(request):
    error = ''
    if request.method == 'POST':
        form = EditProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
        else:
            error = form.errors
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'main/profile.html', {'form': form, 'error': error})




class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_object(self):
        return self.request.user
