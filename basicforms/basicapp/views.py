from django.shortcuts import render
from basicapp import forms #==> from . import forms, the directory above

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form_variable = forms.FormName

    if request.method == 'POST':
        form_variable = forms.FormName(request.POST)

        if form_variable.is_valid():
            #DO SOMETHING in console
            print("VALIDATION SUCCESS")
            print("NAME: "+ form_variable.cleaned_data['name'])
            print("EMAIL: "+ form_variable.cleaned_data['email'])
            print("TEXT: "+ form_variable.cleaned_data['text'])

    form_dict = {'form_key': form_variable}
    return render(request, 'basicapp/form_page.html', context=form_dict)
