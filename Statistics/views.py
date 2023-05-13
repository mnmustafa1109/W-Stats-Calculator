from django.shortcuts import render, redirect
from .inputForm import KendallWValueForms
from rpy2.robjects.packages import STAP
from rpy2.robjects.packages import importr
from .settings import r_file_path

def getKendallW(set_1, set_2):
    base = importr('base')
    c = base.c
    inputIntArr = []
    inputIntArr2 = []
    for i in set_1.split(','):
        inputIntArr.append(int(i))
    for i in set_2.split(','):
        inputIntArr2.append(int(i))
    with open(r_file_path, 'r') as f:
        string = f.read()
    myfunc = STAP(string, "stats")
    print(myfunc.KendallW(c(inputIntArr), c(inputIntArr2)))
    return myfunc.KendallW(c(inputIntArr), c(inputIntArr2))


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
    result = str(request.session.get('result'))
    return render(request, 'result.html', {'result': result})