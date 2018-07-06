from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Item, order
from .forms import PayForm

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
    oorder = order.objects.create(user=request.user, item=item, name=item.name, amount=item.amount)
    return redirect('shop:order_pay', item_id, str(oorder.merchant_uid))


@login_required
def order_pay(request, item_id, merchant_uid):
    oorder = get_object_or_404(order, user=request.user,
                            merchant_uid=merchant_uid, status='ready')
    
    if request.method == 'POST':
        form = PayForm(request.POST, instance=oorder)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = PayForm(instance=oorder)

    return render(request, 'shop/pay_form.html', {
        'form': form,
    })
