# -*- coding: UTF-8 -*-
from django import forms
from web.models import Diary, Money

# 日誌表單
class DiaryForm(forms.ModelForm):
        class Meta:
                model = Diary
                fields = ['memo']
          
# 帳本表單
class MoneyForm(forms.ModelForm):
        RELEVANCE_CHOICES = (
                (1, "飲食"),
                (2, "衣服"),
                (3, "交通"),
                (4, "教育"),
                (5, "娛樂"),
                (6, "其它"),
        )
        kind = forms.ChoiceField(choices = RELEVANCE_CHOICES, required=True)

        class Meta:
                model = Money
                fields = ['item', 'kind', 'price']

        def __init__(self, *args, **kwargs):
                super(MoneyForm, self).__init__(*args, **kwargs)
                self.fields['item'].label = "項目"
                self.fields['kind'].label = "類別"
                self.fields['price'].label = "費用"
                
# 使用者登入表單
class LoginForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)

        def __init__(self, *args, **kwargs):
                super(LoginForm, self).__init__(*args, **kwargs)
                self.fields['username'].label = "帳號"
                self.fields['password'].label = "密碼"