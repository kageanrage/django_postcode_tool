from django.shortcuts import render, redirect, get_object_or_404
from .models import PostcodeList
from .forms import PostcodeListForm

# Create your views here.


def home_page(request):
    lists = PostcodeList.objects.all()
    return render(request, 'pc_tool/list_list.html', {'lists': lists})


def new_postcode_list(request):
    form = PostcodeListForm()
    return render(request, 'pc_tool/list_edit.html', {'form': form})


def new_postcode_list_2(request):
    if request.method == "POST":
        form = PostcodeListForm(request.POST)
        if form.is_valid():
            pc_list = form.save(commit=False)
            # pc_list.author = request.user
            pc_list.save()
            return redirect('home_page')
    else:
        form = PostcodeListForm()
    return render(request, 'blog/list_edit.html', {'form': form})


def list_detail(request, pk):
    list = get_object_or_404(PostcodeList, pk=pk)
    return render(request, 'pc_tool/list_detail.html', {'list': list})
