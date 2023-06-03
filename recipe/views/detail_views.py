from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import DetailForm
from ..models import Recipe, Detail


@login_required(login_url='common:login')
def detail_create(request, recipe_id):
    """
    recipe 상세 정보 등록
    """
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == "POST":
        form = DetailForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.author = request.user  # author 속성에 로그인 계정 저장
            detail.create_date = timezone.now()
            detail.recipe = recipe
            detail.save()
            return redirect('{}#detail_{}'.format(resolve_url('recipe:detail', recipe_id=recipe.id), detail.id))
    else:
        form = DetailForm()
    context = {'recipe': recipe, 'form': form}
    return render(request, 'recipe/recipe_detail.html', context)


@login_required(login_url='common:login')
def detail_modify(request, detail_id):
    detail = get_object_or_404(Detail, pk=detail_id)
    if request.user != detail.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('recipe:detail', recipe_id=detail.recipe.id)
    if request.method == "POST":
        form = DetailForm(request.POST, instance=detail)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.modify_date = timezone.now()
            detail.save()
            return redirect('{}#detail_{}'.format(resolve_url('recipe:detail', recipe_id=detail.recipe.id), detail.id))
    else:
        form = DetailForm(instance=detail)
    context = {'detail': detail, 'form': form}
    return render(request, 'recipe/detail_form.html', context)


@login_required(login_url='common:login')
def detail_delete(request, detail_id):
    detail = get_object_or_404(Detail, pk=detail_id)
    if request.user != detail.author:
        messages.error(request, '삭제 권한이 없습니다')
    else:
        detail.delete()
    return redirect('recipe:detail', recipe_id=detail.recipe.id)