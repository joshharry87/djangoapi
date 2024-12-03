from django.shortcuts import render
from .models import (
    BookingNote, Booking
)
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.decorators.http import require_http_methods
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view #swagger interface decorator


# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.


class BookingNoteView(generic.DetailView):
    model = BookingNote
    
    

def get_booking(request, booking_id):
    # booking = get_object_or_404(Booking, pk=booking_id)
    
    try:
       booking = Booking.objects.get(pk=booking_id)
    except Booking.DoesNotExist:
        raise Http404("No Booking")
    
    return render(
        request, 
        "bookings/booking.html", 
        {
            'booking' : booking
            }
        )
    
    
@require_http_methods(['POST'])
def create_booking(request):
    
    serial = BookingSerializer(data=request.data)
    
    if serial.is_valid():
        serial.save()
        return Response(status=status.HTTP_201_CREATED)
    
    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)



    
@require_http_methods(['POST'])
def create_booking_note(request):
    
    serial = BookingNoteSerializer(data=request.data)
    
    if serial.is_valid():
        serial.save()
        return Response(status=status.HTTP_201_CREATED)
    
    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


@require_http_methods(['POST'])
def update_booking_details(request, booking_id):

    try:
        booking = Booking.objects.get(pk=booking_id)
        booking.entry_details = request.data.entry_details
        booking.save()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@require_http_methods(['POST'])
def update_booking_note_details(request, booking_note_id):
    try:
        booking = BookingNote.objects.get(pk=booking_note_id)
        booking.update_details = request.data.update_details
        booking.save()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@require_http_methods(['PUT'])
def delete_booking_note_details(request, booking_note_id):
    try:
        booking = BookingNote.objects.get(pk=booking_note_id)
        booking.delete()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@require_http_methods(['PUT'])
def delete_booking_details(request, booking_id):

    try:
        booking = Booking.objects.get(pk=booking_id)
        booking.delete()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    