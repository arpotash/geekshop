from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserEditForm, ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import CategoryProduct, Product


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'Пользоветель / редактирование'
    if request.method == 'POST':
        edit_form = ShopUserRegisterForm(request.POST, request.FILES)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_read'))
    else:
        edit_form = ShopUserRegisterForm()

    content = {'title': title, 'update_form': edit_form}
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'Пользователь / удаление'
    curr_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        curr_user.is_active = False
        curr_user.save()
        return HttpResponseRedirect(reverse('admin:user_read'))

    content = {'title': title, 'delete_user': curr_user}
    return render(request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'Пользоветель / редактирование'
    curr_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=curr_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[curr_user.pk]))
    else:
        edit_form = ShopUserEditForm(instance=curr_user)

    content = {'title': title, 'update_form': edit_form}
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def render_admin_page(request):
    return render(request, 'adminapp/base.html')


@user_passes_test(lambda u: u.is_superuser)
def user_read(request):
    title = 'Пользователи'
    user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        'title': title,
        'user_list': user_list
    }

    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request):
    title = 'Продукт / создание'
    if request.method == 'POST':
        product_form_create = ProductEditForm(request.POST, request.FILES)
        if product_form_create.is_valid():
            product_form_create.save()
            return HttpResponseRedirect(reverse('admin:product_read'))
    else:
        product_form_create = ProductEditForm()
    content = {'title': title, 'product_form_create': product_form_create}
    return render(request, 'adminapp/product_create.html', content)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = 'Продукт / удаление'
    delete_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        delete_product.is_active = False
        delete_product.save()
        return HttpResponseRedirect(reverse('admin:products_read'))


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'Продукт / редактирование'
    updating_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product_form_update = ProductEditForm(request.POST, request.FILES, instance=updating_product)
        if product_form_update.is_valid():
            product_form_update.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[updating_product.pk]))
    else:
        product_form_update = ProductEditForm(instance=updating_product)
    content = {'title': title, 'product_form_create': product_form_update}
    return render(request, 'adminapp/product_create.html', content)


@user_passes_test(lambda u: u.is_superuser)
def products_read(request):
    title = 'Товары'
    product_list = Product.objects.all().order_by('category')

    content = {
        'title': title,
        'product_list': product_list
    }

    return render(request, 'adminapp/products_read.html', content)


def product_in_category_read(request, pk):
    title = 'Продукты в категории'
    current_category = get_object_or_404(CategoryProduct, pk=pk)
    products_in_category = Product.objects.filter(category=current_category)
    content = {'title': title, 'products_in_category': products_in_category, 'current_category': current_category}

    return render(request, 'adminapp/product_in_category.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'Категории'
    if request.method == 'POST':
        new_category = ProductCategoryEditForm(request.POST)
        if new_category.is_valid():
            new_category.save()
            return HttpResponseRedirect(reverse('admin:category_read'))
    else:
        new_category = ProductCategoryEditForm()
    content = {'title': title, 'new_category': new_category}

    return render(request, 'adminapp/category_create.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'Категория / удаление'
    delete_category = get_object_or_404(CategoryProduct, pk=pk)
    if request.method == 'POST':
        delete_category.is_active = False
        delete_category.save()
        return HttpResponseRedirect(reverse('admin:category_read'))
    content = {'title': title, 'delete_category': delete_category}
    return render(request, 'adminapp/category_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'Категории / редактирование'
    update_category = get_object_or_404(CategoryProduct, pk=pk)
    if request.method == 'POST':
        update_form = ProductCategoryEditForm(request.POST, instance=update_category)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('admin:category_update', args=[update_category.pk]))
    else:
        update_form = ProductCategoryEditForm(instance=update_category)

    content = {'title': title, 'new_category': update_form}
    return render(request, 'adminapp/category_create.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_read(request):
    title = 'Категории'
    category_list = CategoryProduct.objects.all()

    content = {
        'title': title,
        'category_list': category_list
    }

    return render(request, 'adminapp/categories.html', content)
