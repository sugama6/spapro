from django import forms
from django.core.exceptions import ValidationError
from app.models import *
import re

class AdminEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdminEditForm, self).__init__(*args, **kwargs)
        SEX_CHOICE = (
            (0, '男性'),
            (1, '女性'),
            (2, 'どちらでもない'),
        )
        AREA_CHOICE = (
            ('',''),('北海道','北海道'),('青森県','青森県'),('岩手県','岩手県'),('宮城県','宮城県'),('秋田県','秋田県'),('山形県','山形県'),('福島県','福島県'),('茨城県','茨城県'),\
            ('栃木県','栃木県'),('群馬県','群馬県'),('埼玉県','埼玉県'),('千葉県','千葉県'),('東京都','東京都'),('神奈川県','神奈川県'),('新潟県','新潟県'),('富山県','富山県'),\
            ('石川県','石川県'),('福井県','福井県'),('山梨県','山梨県'),('長野県','長野県'),('岐阜県','岐阜県'),('静岡県','静岡県'),('愛知県','愛知県'),('三重県','三重県'),\
            ('滋賀県','滋賀県'),('京都府','京都府'),('大阪府','大阪府'),('兵庫県','兵庫県'),('奈良県','奈良県'),('和歌山県','和歌山県'),('鳥取県','鳥取県'),('島根県','島根県'),\
            ('岡山県','岡山県'),('広島県','広島県'),('山口県','山口県'),('徳島県','徳島県'),('香川県','香川県'),('愛媛県','愛媛県'),('高知県','高知県'),('福岡県','福岡県'),\
            ('佐賀県','佐賀県'),('長崎県','長崎県'),('熊本県','熊本県'),('大分県','大分県'),('宮崎県','宮崎県'),('鹿児島県','鹿児島県'),('沖縄県','沖縄県'),
        )

        self.fields['mail_address'] = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
        self.fields['tel'] = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
        self.fields['postal_code'] = forms.CharField(max_length=7, widget=forms.TextInput(attrs={'class': 'p-postal-code form-control'}))
        # self.fields['sex'] = forms.ChoiceField(choices=SEX_CHOICE, widget=forms.Select(attrs={'class': 'form-control'}))
        self.fields['prefectures'] = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'class': 'p-region form-control', 'readonly': 'readonly'}))
        self.fields['municipalities'] = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'p-locality form-control', 'readony': 'readonly'}))
        self.fields['address'] = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'p-street-address form-control'}))
        self.fields['apartment_mansion'] = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'p-extended-address form-control'}))

    class Meta:
        model = Users
        fields = (
            'mail_address', 'tel', 'postal_code', 'prefectures', 'municipalities', 'address', 'apartment_mansion'
        )
    
    def clean_mail_address(self):
        mail_address = self.cleaned_data['mail_address']
        reg = re.search("[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$", mail_address)
        if reg == None:
            raise forms.ValidationError('正しいメールアドレスを入力してください')
        
        # admin_user_count = AdminUsers.objects.filter(mail_address=self.cleaned_data['mail_address']).count()
        # if admin_user_count != 0:
        #     raise forms.ValidationError('このメールアドレスは既に使用されています。')
        
        return mail_address

    def clean_postal_code(self):
        tel = self.cleaned_data['postal_code']
        digit = re.search('\d{7}', tel)
        if digit == None :
            raise forms.ValidationError('郵便番号は7桁で入力してください')
        num = re.search('[^0-9]+', tel)
        if num != None:
            raise forms.ValidationError('数字のみで入力してください')
        # if re.search('[-]+'):
        #     raise forms.ValidationError(u'電話番号は半角数字のみで入力してください')
        return tel

    def clean_tel(self):
        tel = self.cleaned_data['tel']
        # reg = re.search('\d{2,4}-?\d{3,4}-?\d{4}', tel)
        # if reg == None :
        #     raise forms.ValidationError('電話番号の入力に誤りがあります')
        if re.search('[^0-9]+', tel):
            raise forms.ValidationError('電話番号は半角数字のみで入力してください')
        return tel