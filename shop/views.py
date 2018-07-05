from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import OrderForm

class ItemListView(ListView):
    model = Item
    queryset = Item.objects.filter(is_public=True)

    def get_queryset(self):
        self.q = self.request.GET.get('q','')
        qs = super().get_queryset()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.q
        return context
index = ItemListView.as_view(model=Item, queryset=Item.objects.filter(is_public=True))


@login_required
def order_new(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    initial = {'name': item.name, 'amount': item.amount}
    if request.method == 'POST':
        form = OrderForm(request.POST, initial=initial)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.item = item
            order.save()
            return redirect('accounts:profile')
    else:
        form = OrderForm(initial=initial)
        
    return render(request, 'shop/order_form.html',{
        'form': form,
        'iamport_shop_id': 'iamport',  # FIXME: 가맹점 식별코드
    })
