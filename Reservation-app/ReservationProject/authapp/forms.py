from django import forms
from .models import joinMembership


class registrationForm(forms.ModelForm):

    class Meta:
        model = joinMembership
        fields = "__all__"


    koreanLastname = forms.CharField(label='한국(성)')
    koreanFristname = forms.CharField(label='한국(이름)')
    englishLastname = forms.CharField(label='영문(이름)')
    englishFirstname = forms.DateField(label='영문(성)')
    birthday = forms.DateField(label='생년월일')
    email = forms.EmailField(label="이메일")
    address = forms.CharField(label="기본주소")
    detailAddress = forms.CharField(label="상세주소")
    phoneNumber = forms.CharField(label="핸드폰번호")
    companyName = forms.CharField(label="회사명")
    deaprtment = forms.CharField(label="부서명")
    position = forms.CharField(label="직급")
    fixedlineTelephone = forms.CharField(label="유선전화번호")


class loginForm(forms.ModelForm):

    class Meta:
        model = joinMembership
        fields = "__all__"

