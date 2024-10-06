from django.shortcuts import render

from info.models import Contact, FAQ

# Create your views here.
def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    title = request.POST.get('title')
    comment = request.POST.get('comment')

    if name and email and title and comment:
        Contact.objects.create(
            name=name,
            email=email,
            title=title,
            comment=comment
        )

        return render(request, 'info/contact.html', {'success_message': 'Ваше повідомлення успішно надіслано.'})
    else:
        error_message = "Усі поля обов'язкові для заповнення."
        return render(request, 'info/contact.html', {'error_message': error_message})


def terms(request):
    return render(request, 'info/terms.html')


def faq(request):
    FAQs = FAQ.objects.all()

    context = {
        'FAQs': FAQs
    }

    return render(request, 'info/faq.html', context)