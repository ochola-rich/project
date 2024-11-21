from django.shortcuts import render
from . import gemeni
import markdown2
# Create your views here.
def ai(request):
    suggestions = markdown2.markdown(gemeni.response.text)
    context = {'suggestions': suggestions}
    return render(request, 'home.html', context)