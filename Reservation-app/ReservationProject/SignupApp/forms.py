from django import forms
from .models import MyUser


class registrationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username','email','password','koreanLastname', 'koreanFirstname', 'englishLastname','englishFirstname','address','detailAddress','phoneNumber']
        #fields = "__all__"

    username = forms.CharField(label="로그인아이디")
    email = forms.EmailField(label="이메일")
    password = forms.CharField(label="패스워드", widget=forms.PasswordInput())
    koreanLastname = forms.CharField(label='한국(성)')
    koreanFirstname = forms.CharField(label='한국(이름)')
    englishLastname = forms.CharField(label='영문(이름)')
    englishFirstname = forms.DateField(label='영문(성)')
    address = forms.CharField(label="기본주소")
    detailAddress = forms.CharField(label="상세주소")
    phoneNumber = forms.CharField(label="핸드폰번호")


class loginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']
        #fields = "__all__"

    username = forms.CharField(label="아이디", help_text="가입시 입력하신 아이디를 입력하여 주세요")
    password = forms.CharField(label="패스워드", help_text="가입시 입력하신 패스워드를 입력하여 주세요", widget=forms.PasswordInput())