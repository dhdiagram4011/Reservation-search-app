from django import forms
from .models import skyuser


class registrationForm(forms.ModelForm):
    class Meta:
        model = skyuser
        fields = ('koreanLastname', 'koreanFirstname', 'englishLastname','englishFirstname','birthday','email','password','address','detailAddress','phoneNumber','companyName','department','position','fixedlineTelephone')

    koreanLastname = forms.CharField(label='한국(성)')
    koreanFirstname = forms.CharField(label='한국(이름)')
    englishLastname = forms.CharField(label='영문(이름)')
    englishFirstname = forms.DateField(label='영문(성)')
    birthday = forms.DateField(label='생년월일')
    email = forms.EmailField(label="이메일")
    password = forms.CharField(label="패스워드", widget=forms.PasswordInput())
    address = forms.CharField(label="기본주소")
    detailAddress = forms.CharField(label="상세주소")
    phoneNumber = forms.CharField(label="핸드폰번호")
    companyName = forms.CharField(label="회사명")
    department = forms.CharField(label="부서명")
    position = forms.CharField(label="직급")
    fixedlineTelephone = forms.CharField(label="유선전화번호")


class loginForm(forms.ModelForm):
    class Meta:
        model = skyuser
        fields = ('email', 'password')

    email = forms.EmailField(label="이메일", help_text="가입시 입력하신 이메일을 입력하여 주세요")
    password = forms.CharField(label="패스워드", help_text="가입시 입력하신 패스워드를 입력하여 주세요", widget=forms.PasswordInput())



