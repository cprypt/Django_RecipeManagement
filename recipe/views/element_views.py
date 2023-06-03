from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url

from ..forms import ElementForm
from ..models import Recipe, Element

@login_required(login_url='common:login')
def element_create(request, recipe_id):
    """
    recipe 재료 등록
    """
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == "POST":
        form = ElementForm(request.POST)
        if form.is_valid():
            element = form.save(commit=False)
            element.recipe = recipe
            element.save()
            return redirect('{}#detail_{}'.format(resolve_url('recipe:detail', recipe_id=recipe.id), element.id))
    else:
        form = ElementForm()
    context = {'recipe': recipe, 'form': form}
    return render(request, 'recipe/recipe_detail.html', context)


@login_required(login_url='common:login')
def element_delete(request, element_id):
    element = get_object_or_404(Element, pk=element_id)
    if request.user != element.recipe.author:
        messages.error(request, '삭제 권한이 없습니다')
    else:
        element.delete()
    return redirect('recipe:detail', recipe_id=element.recipe.id)