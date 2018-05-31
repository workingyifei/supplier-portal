from django.shortcuts import render
from django.views import generic
from .models import Audit

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'audits/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Audit.objects.order_by('-pub_date')[:5]
