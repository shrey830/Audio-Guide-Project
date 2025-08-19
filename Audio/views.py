from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.models import User
from .models import register_view,login_view  # Import your custom model
from django.contrib.auth.hashers import make_password 
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
import random2
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def index(request):
    
    return render(request,'index.html')


def header(request):
    return render(request,'header.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contact.html')

def tour(request):
    return render(request,'tour.html')

from django.shortcuts import render
from django.contrib import messages
from .models import Rating
from django.db.models import Avg, Count
def tourdetail1(request):
    ratings = Rating.objects.filter(place="adalaj-stepwell")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="adalaj-stepwell")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail1.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })

def tourdetail2(request):
    ratings = Rating.objects.filter(place="rani-ki-vav")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="rani-ki-vav")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail2.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })

def tourdetail3(request):
    ratings = Rating.objects.filter(place="vintage-car-museum")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="vintage-car-museum")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail3.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })
   

def tourdetail4(request):
    ratings = Rating.objects.filter(place="sabarmati-aashram")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="sabarmati-aashram")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail4.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })
    

def tourdetail5(request):
    ratings = Rating.objects.filter(place="hutheesing-jain-temple")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="hutheesing-jain-temple")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail5.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })
    

def tourdetail6(request):
    ratings = Rating.objects.filter(place="jama-masjid")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="jama-masjid")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail6.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })

def tourdetail7(request):
    ratings = Rating.objects.filter(place="jhulta-minar")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="jhulta-minar")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail7.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })

def tourdetail8(request):
    ratings = Rating.objects.filter(place="kankaria-lake")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="kankaria-lake")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail8.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })

def tourdetail9(request):
    ratings = Rating.objects.filter(place="lal-darvaja")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="lal-darvaja")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail9.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })

def tourdetail10(request):
    ratings = Rating.objects.filter(place="sabarmati-riverfront")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="sabarmati-riverfront")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail10.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })


def Audio1(request):

    return render(request,'Audio1.html')

def home(request):
    return render(request,'home.html')


def otp(request):
    return render(request,'otp_verification.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        message=request.POST.get("message")
        formData = contact_us(name=name, email=email, phone=phone, message=message)          
        formData.save() 
        return redirect("contact") 
    return render(request,'contact.html')



from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages  # Import messages framework

def register_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('cpass')

        # Check if passwords match
        if pass1 != pass2:
            return HttpResponse("Your Password and Confirm Password are not the same")

        # Check if username already exists
        if User.objects.filter(username=name).exists():
            return HttpResponse("Username already taken. Please choose another one.")

        # Check if email already exists (optional but recommended)
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email is already in use. Try another one.")

        # Create and save user
        user = User.objects.create_user(username=name, email=email, password=pass1)
        user.save()

        return redirect('login')  # Redirect to login page after successful registration

    return render(request, 'register.html')



def user_login(request):  # Renamed from 'login' to 'user_login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user using Django's built-in authentication
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in using Django's login function
            auth_login(request, user)  # Use the renamed 'auth_login' function
            return redirect('index')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request,'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')


def audio_player(request):
    audio_files = Audio.objects.all()
    return render(request, 'audio_page.html', {'audio_files': audio_files})

def ahmedabad(request):
    cities = City.objects.all()
    return render(request, 'ahmedabad.html', {'cities': cities})
    

import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

# def send_otp(request):
#     if request.method == "POST":
#         entered_otp = request.POST.get("otp")
#         stored_otp = request.session.get("otp")

#         if entered_otp and stored_otp and entered_otp == str(stored_otp):
#             messages.success(request, "OTP verified successfully!")
#             return redirect("login")  # Redirect to success page
#         else:
#             messages.error(request, "Invalid OTP. Please try again.")

#     # Generate OTP
#     otp = random.randint(100000, 999999)
#     request.session["otp"] = otp  # Store OTP in session

#     # Send OTP via email (Update with your email settings)
#     # send_mail(
#     #     "Your OTP Code",
#     #     f"Your OTP code is {otp}",
#     #     "your_email@example.com",
#     #     ["user_email@example.com"],
#     #     fail_silently=False,
#     # )

#     return render(request, "otp_verification.html", {"otp": otp})  # Pass OTP to template
def send_otp(request):
    return render(request,"otp_verification.html")



def bookguide_page(request, guide_name, guide_place):
    if request.method == 'POST':
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        member = request.POST.get('member')  # Get the missing field
        price = request.POST.get('charges')  

        formData = Booking(date=date, 
                           start_time=start_time,
                           end_time=end_time,
                           member=member,  
                           price=price)
        formData.save()
        return redirect("send_otp")

    return render(request, "bookguide.html", {"guide_name": guide_name, "guide_place": guide_place})



def profile_page(request): 
    bookings = Booking.objects.filter()  # Fetch all bookings for the logged-in user

    context = {
        "bookings": bookings  # Pass the entire queryset to the template
    }
    return render(request, "profilepage.html", context)

