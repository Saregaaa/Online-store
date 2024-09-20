from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'info/contact.html')


def terms(request):
    return render(request, 'info/terms.html')


def faq(request):
    return render(request, 'info/faq.html')