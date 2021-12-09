from django.shortcuts import render
from basicapp import forms #==> from basicapp import forms, the directory above

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form_var = forms.FormName

    if request.method == 'POST':
        form_var = forms.FormName(request.POST)

        if form_var.is_valid():
            #DO SOMETHING
            print("VALIDATION SUCCESS")
            print("NAME: "+ form_var.cleaned_data['name'])
            print("EMAIL: "+ form_var.cleaned_data['email'])
            print("TEXT: "+ form_var.cleaned_data['text'])




    form_dict = {'form_key': form_var}
    return render(request, 'basicapp/form_page.html', context=form_dict)
