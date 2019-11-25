from django.shortcuts import render

# import created form
from .forms import SignUp


def registerform(request):

    if request.method == 'POST':
        form = SignUp(request.POST)
        html = 'We haeve received this form again'

        if form.is_valid():
            html = html + "The Form is Valid"

    else:
        form = SignUp()
        html = 'Welcome for the First Time'

    context = {}
    context['form'] = form
    context['html'] = html

    return render(request, 'signup.html', context)
