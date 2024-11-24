from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, get_user_model
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import UserPassesTestMixin
from .forms import CustomUserCreationForm, UserUpdateForm
from django.contrib.auth.views import LogoutView

User = get_user_model()

class UserCreateAndLoginView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "account/signup.html"
    success_url = reverse_lazy("tasks:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        raw_pw = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=raw_pw)
        if user is not None:
            login(self.request, user)
        else:
            form.add_error(None, "Error en la autenticación.")
        return response

class OnlyYouMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class UserDetail(OnlyYouMixin, DetailView):
    model = User
    template_name = 'account/detail_user.html'

class UserUpdate(OnlyYouMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'account/edit_user.html'

    def get_success_url(self):
        return reverse_lazy('detail_user', kwargs={'pk': self.kwargs['pk']})

class PasswordChange(PasswordChangeView):
    template_name = 'account/change_password.html'
    def get_success_url(self):
        return reverse_lazy('detail_user', kwargs={'pk': self.request.user.pk})

class UserDelete(OnlyYouMixin, DeleteView):
    model = User
    template_name = 'account/delete_user.html'
    success_url = reverse_lazy('login')

class UserLogout(LogoutView):
    next_page = reverse_lazy('login')
