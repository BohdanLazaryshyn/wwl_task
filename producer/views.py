import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from producer.forms import OrderSearchForm, RegistrationForm
from producer.models import Order
from producer.telegrambot import send_message


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "orders.html"
    context_object_name = "orders"
    model = Order

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")

        context["search_form"] = OrderSearchForm(
            initial={"name": name}
        )
        context["orders"] = self.get_queryset()
        return context

    def get_queryset(self):
        queryset = Order.objects.filter(employee=self.request.user)
        form = OrderSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])

        return queryset


class OrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Order
    success_url = reverse_lazy("producer:orders")

    def get_success_url(self):
        message = f"Задача №{self.object.pk}-{self.object.task_id} під назвою {self.object.name} "\
            f"була опрацьована {self.object.employee.first_name} - {self.object.employee.position} "\
            f"у {datetime.datetime.now()}"
        send_message(message)
        messages.success(self.request, message)
        return super().get_success_url()


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = RegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form})
