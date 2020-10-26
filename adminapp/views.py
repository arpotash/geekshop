from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserEditForm, ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import CategoryProduct, Product


class TemplateAdminPage(TemplateView):
    template_name = 'adminapp/base.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    paginate_by = 3

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    form_class = ShopUserRegisterForm
    success_url = reverse_lazy('admin:user_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    form_class = ShopUserEditForm
    success_url = reverse_lazy('admin:user_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin:user_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product_create.html'
    success_url = reverse_lazy('admin:products_read')
    form_class = ProductEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('admin:products_read')
    template_name = 'adminapp/product_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукт / удаление'
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/product_create.html'
    success_url = reverse_lazy('admin:products_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукты / редактирование'
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products_read.html'
    paginate_by = 5

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Product.objects.all().order_by('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продукты'
        return context


class ProductInCategoryListView(ListView):
    model = Product
    template_name = 'adminapp/product_in_category.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs
        category = get_object_or_404(CategoryProduct, pk=self.kwargs['pk'])
        context['category_name'] = category
        context['title'] = 'Продукты категории'
        return context

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['pk'])


class ProductCategoryCreateView(CreateView):
    model = CategoryProduct
    template_name = 'adminapp/category_create.html'
    success_url = reverse_lazy('adminapp:category_read')
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProductCategoryDeleteView(DeleteView):
    model = CategoryProduct
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin:category_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductCategoryListView(ListView):
    model = CategoryProduct
    template_name = 'adminapp/categories.html'
    paginate_by = 4

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProductCategoryUpdateView(UpdateView):
    model = CategoryProduct
    template_name = 'adminapp/category_create.html'
    success_url = reverse_lazy('admin:category_read')
    form_class = ProductCategoryEditForm
