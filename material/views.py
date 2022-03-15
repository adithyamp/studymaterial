from re import M
from django.shortcuts import redirect, render, get_object_or_404
from . forms import MaterialForm
from . models import Material
from . filters import MaterialFilter
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages

def index(request):
    material_list = Material.objects.all().order_by('-date')

    myfilter = MaterialFilter(request.GET, queryset=material_list)
    material_list = myfilter.qs

    search_query = request.GET.get('m')
    if search_query:
        material_list = material_list.filter(
            Q(course__icontains=search_query) |
            Q(subject__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    paginator = Paginator(material_list, 25)
    page_number = request.GET.get('page')
    material_list = paginator.get_page(page_number)

    context = {
        'material_list': material_list,
        'myfilter': myfilter,
    }

    return render(request, 'index.html', context)


def material_form(request):
    mform = MaterialForm()
    if request.method == 'POST':
        mform = MaterialForm(request.POST, request.FILES)

        if mform.is_valid():
            obj = Material.objects.create(
                semester = mform.cleaned_data["semester"],
                course = mform.cleaned_data["course"],
                subject = mform.cleaned_data["subject"],
                material = mform.cleaned_data["material"],
                description = mform.cleaned_data["description"],
            )
            obj.save()
            messages.info(request, "Your material has been successfully uploaded !")
            
            return redirect('material:index')
        else:
            mform = MaterialForm()
    
    return render(request, 'material_form.html', {'mform': mform})


def material_detail(request, id):
    material = Material.objects.get(id=id)

    context = {
        'material':material,
    }

    return render(request, 'index.html', context)