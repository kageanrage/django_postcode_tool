from django.shortcuts import render, redirect, get_object_or_404
from .models import PostcodeList
from .forms import PostcodeListForm

# Create your views here.


def home_page(request):
    lists = PostcodeList.objects.all()
    return render(request, 'pc_tool/list_list.html', {'lists': lists})


def new_postcode_list(request):
    if request.method == "POST":  # if the user hits the save button
        form = PostcodeListForm(request.POST)  # take the data, put it in a Form instance and call it form
        if form.is_valid():  # if it's valid
            list = form.save(commit=False)  # don't commit the save yet
            list.csv = list.convert_to_csv()  # update the csv attribute of the instance
            list.save()   # ... and then save it
            return redirect(list_edit, pk=list.pk)  # then send user to the list_edit view
    else:  # assuming user hasn't hit 'save' button yet, what do we want them to see?
        form = PostcodeListForm()  # create a blank form
    return render(request, 'pc_tool/list_edit.html', {'form': form})  # show the blank form through the list_edit template


def list_detail(request, pk):
    list = get_object_or_404(PostcodeList, pk=pk)
    return render(request, 'pc_tool/list_detail.html', {'list': list})


def list_edit(request, pk):
    list = get_object_or_404(PostcodeList, pk=pk)  # establish which instance we're referring to here
    if request.method == "POST":  # if the user has hit the 'save' button
        form = PostcodeListForm(request.POST, instance=list)  # take the data, ensure it's still associated with this instance, shove it in a Form and name it 'form'
        if form.is_valid():  # if it's valid
            list = form.save(commit=False)  # don't commit the save yet
            list.csv = list.convert_to_csv()  # update the csv attribute of the instance
            list.save()  # ... and then save it
            # return redirect(list_detail, pk=list.pk)  # previously we redirected to the list_detail view
            return redirect(list_edit, pk=list.pk)  # now we want to continue to show the edit screen so that 'CSV' is easily copy/paste-able
    else:  # assuming user hasn't hit 'save' button yet, what do we want them to see?
        form = PostcodeListForm(instance=list)  # show them a form, populated with the instance data
    return render(request, 'pc_tool/list_edit.html', {'form': form})  # display this via the list_edit template


def list_remove(request, pk):
    list = get_object_or_404(PostcodeList, pk=pk)
    list.delete()
    return redirect(home_page)


def about(request):
    return render(request, 'pc_tool/about.html', {})