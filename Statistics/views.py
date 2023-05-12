from django.shortcuts import render, redirect
from .inputForm import KendallWValueForms
from django.forms.models import model_to_dict


# Create your views here.
def take_input(request, error=""):
    if request.method == 'POST':
        form = KendallWValueForms(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            print("Valid")
            request.session['set_1'] = form.cleaned_data['set_1']
            request.session['set_2'] = form.cleaned_data['set_2']
            if len(form.cleaned_data['set_1']) != len(form.cleaned_data['set_2']):
                return render(request, 'index.html', {'form': form, 'error': "The length of two sets must be equal."})
            return redirect('result')

        else:
            return render(request, 'index.html', {'form': form, 'error': error})
        print(request.POST)

    else:
        form = KendallWValueForms()
        context = {
            'form': form,
            'error': error
        }

        return render(request, 'index.html', context)

def display_result(request):
    # print(random)

    # print(form.errors)
    set_1 = str(request.session.get('set_1'))
    return render(request, 'result.html', {'result': set_1})