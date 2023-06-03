from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import RecipeForm
from ..models import Recipe


@login_required(login_url='common:login')
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # author 속성에 로그인 계정 저장
            recipe.create_date = timezone.now()
            recipe.save()
            return redirect('recipe:index')
    else:
        form = RecipeForm()
    context = {'form': form}
    return render(request, 'recipe/recipe_form.html', context)


@login_required(login_url='common:login')
def recipe_modify(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user != recipe.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('recipe:detail', recipe_id=recipe.id)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.modify_date = timezone.now()  # 수정일시 저장
            recipe.save()
            return redirect('recipe:detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    context = {'form': form}
    return render(request, 'recipe/recipe_form.html', context)


@login_required(login_url='common:login')
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.user != recipe.author:
        messages.error(request, '삭제 권한이 없습니다')
        return redirect('recipe:detail', recipe_id=recipe.id)
    recipe.delete()
    return redirect('recipe:index')