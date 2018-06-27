from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Goods


@login_required
def index(request):
    goods = get_list_or_404(Goods)
    return render(
        request,
        'index.html',
        {'goods': goods}
    )


@login_required
def detail(request, pk):
    goods_item = get_object_or_404(Goods, pk=pk)
    return render(
        request,
        'detail.html',
        {'goods_item': goods_item}
    )
