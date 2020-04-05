from django import forms
from .models import flightNumber, flightAircraft, flightSection, seatClass, price, emailTicket
import datetime


class reservationForm(forms.ModelForm):

    class Meta:
        model = flightSection
        fields = "__all__"


    STARTINGPOINT = (
        ('김포', '김포'),
        ('제주', '제주'),
        ('부산', '부산'),
        ('울산', '울산'),
        ('대구', '대구'),
        ('청주', '청주'),
    )


    ARRIVAL = (
        ('김포', '김포'),
        ('제주', '제주'),
        ('부산', '부산'),
        ('울산', '울산'),
        ('대구', '대구'),
        ('청주', '청주'),
    )


    RANKING = (
        ('프레스티지석', '프레스티지석'),
        ('일반석', '일반석'),
    )


    starting_point = forms.ChoiceField(label='출발지', choices=STARTINGPOINT)
    arrival = forms.ChoiceField(label='도착지', choices=ARRIVAL)
    ranking = forms.ChoiceField(label='좌석등급', choices=RANKING)
    daytogo = forms.DateField(label='가는날', input_formats=['%m-%d-%Y', ])
    comingDay = forms.DateField(label='오는날', input_formats=['%m-%d-%Y', ])




