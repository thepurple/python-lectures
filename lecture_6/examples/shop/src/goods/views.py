from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Goods


def index(request):
    goods = get_list_or_404(Goods)
    return render(
        request,
        'index.html',
        {'goods': goods}
    )


def detail(request, pk):
    goods_item = get_object_or_404(Goods, pk=pk)
    return render(
        request,
        'detail.html',
        {'goods_item': goods_item}
    )
