from django.shortcuts import render, redirect
from .inputForm import KendallWValueForms
from django.forms.models import model_to_dict


# Create your views here.
def take_input(request, error=None):
    if request.method == 'POST':
        form = KendallWValueForms(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            print("Valid")
            request.session['set_1'] = form['set_1'].value()
            request.session['set_2'] = form['set_2'].value()
        else:
            #print the errors
            request.session['formerrors'] = form.errors
            print("Errors: ")

        print(request.POST)

        return redirect('result' )
    else:
        form = KendallWValueForms()
        context = {
            'form': form,
            'error': error
        }

        return render(request, 'index.html', context)

def display_result(request):
    # print(random)
    formerros = request.session.get('formerrors')
    if (formerros):
        return take_input(request, formerros)
    # print(form.errors)
    set_1 = str(request.session.get('set_1'))
    return render(request, 'result.html', {'result': set_1, 'formerr': formerros})