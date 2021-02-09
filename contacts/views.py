from django.shortcuts import render


def contact(request):
    context = {
        'title': 'Contacts'
    }
    if request.method == 'POST':
        pass
    else:
        return render(request, "contacts/add.html", context)
