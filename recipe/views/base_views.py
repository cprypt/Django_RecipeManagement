from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Recipe


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    recipe_list = Recipe.objects.order_by('-create_date')
    if kw:
        recipe_list = recipe_list.filter(
            Q(name__icontains=kw) |  # 이름 검색
            Q(category__icontains=kw) |  # 카테고리 검색
            Q(author__username__icontains=kw)  # 레시피 작성자 검색
        ).distinct()
    paginator = Paginator(recipe_list, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'recipe_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'recipe/recipe_list.html', context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipe/recipe_detail.html', context)