from django.shortcuts import render

from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy

# Create your views here.



@login_required(login_url=reverse_lazy('login'))
def main_dashboard(request):
	return render(request, 'dashboard.html')