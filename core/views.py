from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date

from .filters import SearchFilter
from . forms import ItemForm, AddImageForm
from . models import Item
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def make_property_reference():
    last_ref = Item.objects.all().order_by('id').last()
    if not last_ref:
         return 'IOM/1/'+ date.today().strftime('%y')
    if last_ref.propertyReference.split('/')[2] != date.today().strftime('%y'):
        return 'IOM/1/' + date.today().strftime('%y')
    else:
        ref_no = last_ref.propertyReference
        ref_int = int(ref_no.split('/')[1])
        new_ref_int = ref_int + 1
        new_ref_no = 'IOM/' + str(new_ref_int) + '/' + date.today().strftime('%y')
        return new_ref_no


class Index(LoginRequiredMixin,View):
    login_url = '/accounts/login/'
    #redirect_field_name = 'redirect_to'
    template_name = 'core/index.html'
    def get(self, request):
        queryset = Item.objects.filter(user=request.user).order_by('-createdDate')[:10]
        context = {
            'items':queryset,"request":request
        }
        return render(request, self.template_name, context)

#def product_detail_view(request, id):
#    obj = get_object_or_404(Product, id=id)
#    context = {
#        "object": obj
#    }
#    return render(request, "products/product_detail.html", context)

class AddImageView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    template_name = 'core/addImage.html'
    def get(self, request, pk):
        form = AddImageForm
        context = {"form":form}
        return render(request, self.template_name, context)
    def post(self, request, pk):
        form = AddImageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.item = get_object_or_404(Item, pk=pk)
            instance.save()
            return HttpResponseRedirect(reverse('index'))

        context = {"form":form}
        return render(request, self.template_name, context)

class Add(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    template_name = 'core/add.html'
    def get(self, request):
        form = ItemForm()
        context = {"form":form}
        return render(request, self.template_name, context)
    def post(self, request):
        form = ItemForm(request.POST or None, request.FILES or None)#request files...used for imagefield so may need to be removed
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.propertyReference = make_property_reference()
            instance.save()
            return HttpResponseRedirect(reverse('index'))

        context = {"form":form}
        return render(request, self.template_name, context)

class Search(View):
    template_name='core/search.html'
    def get(self, request):
        search_filter = SearchFilter()
        context = {'search_filter':search_filter}
        return render(request, self.template_name, context)

    def post(self, request):
        item_list = Item.objects.all()
        search_filter = SearchFilter(request.POST, queryset=item_list)
        context = {'search_filter':search_filter}
        return render(request, 'core/results.html', context)

class ItemDetailView(DetailView):
    template_name = 'core/detail.html'
    model = Item


