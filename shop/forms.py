from django import forms
from .models import order
import json
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_text
from django.template.loader import render_to_string
from django import forms
from .models import order
from .mixins import IamportBaseForm


class PayForm(IamportBaseForm):
    template_name = 'shop/_iamport.html'
    params_names = ['merchant_uid', 'name', 'amount']
    imp_fn_name = 'request_pay'
        
    class Meta:
        model = order
        fields = ['imp_uid']
        widgets = {
            'imp_uid': forms.HiddenInput,
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model= order
        fields = ('name', 'amount')
        widgets = {
            'name': forms.TextInput(attrs={'readonly':'readonly'}),
            'amount': forms.TextInput(attrs={'readonly':'readonly'})
        }
"""
class PayForm(forms.ModelForm):
    class Meta:
        model =order
        fields = ('imp_uid',)

    def as_iamport(self):
        #본 Form의 Hidden 필드 위젯
        hidden_fields = mark_safe(''.join(smart_text(field) for field in self.hidden_fields()))
        # IMP.request_pay의 인자로 넘길 인자 목록
        fields = {
            'merchant_uid': str(self.instance.merchant_uid),
            'name': self.instance.name,
            'amount': self.instance.amount,
        }
        return hidden_fields + render_to_string('shop/_iamport.html', {
            'json_fields': mark_safe(json.dumps(fields, ensure_ascii=False)),
            'iamport_shop_id': settings.IAMPORT_SHOP_ID,  # FIXME: 각자의 상점 아이디로 변경 가능
        })


    def save(self):
        oorder = super().save(commit=False)
        oorder.status = 'paid'  # FIXME: 아임포트 API를 통한 확인 후에 변경을 해야만 합니다.
        oorder.update()
        oorder.save()
        return oorder

"""