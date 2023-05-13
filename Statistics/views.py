from django.shortcuts import render, redirect
from .inputForm import KendallWValueForms
from rpy2.robjects.packages import STAP
from rpy2.robjects.packages import importr
from django.forms.models import model_to_dict

def getKendallW(set_1, set_2):
    base = importr('base')
    c = base.c
    inputIntArr = []
    for i in set_1.split(','):
        inputIntArr.append(int(i))
    with open('/home/syednouman1618/PycharmProjects/W-Stats-Calculator/Statistics/stats.r', 'r') as f:
        string = f.read()
    myfunc = STAP(string, "stats")
    print(myfunc.KendallW(c(inputIntArr), c(1,2,3)))
    return myfunc.KendallW(c(inputIntArr), c(1,2,3))


# Create your views here.
def take_input(request, error=""):
    if request.method == 'POST':
        form = KendallWValueForms(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            print("Valid")
            request.session['result'] = str(getKendallW(form.cleaned_data['set_1'], form.cleaned_data['set_2']))
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
    result = str(request.session.get('result'))
    return render(request, 'result.html', {'result': result})