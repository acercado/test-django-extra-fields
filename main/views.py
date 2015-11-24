from django.shortcuts import render
from . models import Contest
from . forms import Contest_Form_Addendum

# @login_required
def index(request):
    mode = ''
    if request.method == 'POST':
        form = Contest_Form_Addendum(request.POST)
        if form.is_valid():
            contest = form.save(commit=False)
            contest.author = request.user
            contest.save()
            mode = 'saved'
    else:
        form = Contest_Form_Addendum()
    return render(request , 'main/base.html', {'form': form, 'mode': mode})