from rest_framework import serializers
from .models import BookingNote, Booking

class BookingNoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BookingNote
        fields = (
            'pk',
            'booking',
            'update_details'
        )
        
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'pk',
            'title',
            'entry_details',
            'entry_date',
            'completed',
        )