from django.shortcuts import render
from .models import CropRecommendation


def dashboard(request):
    user_profile = request.user.userprofile
    crop_recommendations = CropRecommendation.objects.filter(locality=user_profile.locality)
    return render(request, 'dashboard/dashboard.html', {'crop_recommendations': crop_recommendations,'disaster_alerts': disaster_alerts,})


def recommend_crops(locality, soil_type):
    # Logic to recommend crops based on locality and soil type
    recommendations = Crop.objects.filter(locality=locality, soil_type=soil_type)
    return recommendations
