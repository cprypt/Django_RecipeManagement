from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url

from ..forms import CookingForm
from ..models import Recipe, Cooking

@login_required(login_url='common:login')
def cooking_create(request, recipe_id):
    """
    recipe 재료 등록
    """
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == "POST":
        form = CookingForm(request.POST)
        if form.is_valid():
            cooking = form.save(commit=False)
            cooking.recipe = recipe
            cooking.save()
            return redirect('{}#detail_{}'.format(resolve_url('recipe:detail', recipe_id=recipe.id), cooking.id))
    else:
        form = CookingForm()
    context = {'recipe': recipe, 'form': form}
    return render(request, 'recipe/recipe_detail.html', context)


@login_required(login_url='common:login')
def cooking_delete(request, element_id):
    cooking = get_object_or_404(Cooking, pk=element_id)
    if request.user != cooking.recipe.author:
        messages.error(request, '삭제 권한이 없습니다')
    else:
        cooking.delete()
    return redirect('recipe:detail', recipe_id=cooking.recipe.id)