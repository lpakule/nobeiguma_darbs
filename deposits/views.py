

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, View, FormView, DetailView


from deposits.models import Deposit
from deposits.forms import DepositNewForm
from deposits.deposit_class import DepositClass


class DepositList(ListView):
    model = Deposit
    template_name = 'deposit_list.html'

class DepositGet(DetailView):

        model = Deposit

        template_name = 'deposit_get.html'


class DepositNew(FormView):
    form_class = DepositNewForm

    template_name = 'deposit_new.html'
#    success_url = '/'
    def form_valid(self, form):
        form.save()
        item = form.save()
        self.pk = item.pk

        response = super().form_valid(form=form )

        return response
#
    def get_success_url(self):

        return reverse('deposit-new', kwargs={'pk': self.pk})

class DepositListNew(View):
    model = Deposit
    template_name = 'deposit_added'

