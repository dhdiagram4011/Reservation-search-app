from django import forms
from .models import flightNumber, flightAircraft, flightSection, seatClass, price, emailTicket


class reservationForm(forms.ModelForm):

    class Meta:
        model = flightSection
        fields = "__all__"


    STARTINGPOINT = (
        ('GMP', '김포'),
        ('CJU', '제주'),
        ('PUS', '부산'),
        ('ULS', '울산'),
        ('DGU', '대구'),
        ('CHJ', '청주'),
    )


    ARRIVAL = (
        ('GMP', '김포'),
        ('CJU', '제주'),
        ('PUS', '부산'),
        ('ULS', '울산'),
        ('DGU', '대구'),
        ('CHJ', '청주'),
    )


    RANKING = (
        ('PRES', '프레스티지석'),
        ('GEN', '일반석'),
    )


    starting_point = forms.ChoiceField(label='출발지', choices=STARTINGPOINT)
    arrival = forms.ChoiceField(label='도착지', choices=ARRIVAL)
    ranking = forms.ChoiceField(label='좌석등급', choices=RANKING)
    daytogo = forms.DateField(label='가는날')
    comingDay = forms.DateField(label='오는날')




