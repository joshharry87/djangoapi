from django.db import models
import datetime

# Create your models here.
class SomeObject(models.Model):
    a_number = models.IntegerField()
    a_word = models.CharField(
        max_length=50, 
        null=True
        )
    a_bool = models.BooleanField(
        default=False
        )
    
    @property
    def some_function(self):
        '''
            Just making stuff to get refamiliarised with django.
        '''
        return str(self.a_number) + ' - ' + self.a_word 
    

class Booking(models.Model):
    def get_date():
        return datetime.date.today()
    
    id = models.BigAutoField(primary_key=True)
    
    title = models.CharField(
        max_length=100
    )
    entry_details = models.CharField(
        max_length=500,
        null=True
    )
    entry_date = models.DateField(
        auto_created=True,
        default=get_date()
    )
    completed = models.BooleanField(
        default=False
    )
    

class BookingNote(models.Model):
    booking = models.ForeignKey(
        Booking, 
        on_delete=models.CASCADE
        )
    
    update_details = models.CharField(
        max_length=500
        )

