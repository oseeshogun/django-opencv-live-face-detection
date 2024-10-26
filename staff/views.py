from django.shortcuts import render

from staff.models import Staff
from staff.training import train_faces
from django.http import StreamingHttpResponse
from .camera import VideoCamera, gen
from django.contrib.auth.decorators import login_required


def _get_staff_data():
    staff_members = Staff.objects.all()

    staff_data = []
    for member in staff_members:
        image_count = (
            member.staffface_set.count()
        )  # Compte le nombre d'images associées
        staff_data.append(
            {
                "name": member.name,
                "phone": member.phone,
                "email": member.email,
                "address": member.address,
                "image_count": image_count,
            }
        )
    return staff_data


# Create your views here.
def index(request):
    data = _get_staff_data()
    return render(request, "index.html", {"staff_data": data})

@login_required
def training_view(request):
    train_faces()
    data = _get_staff_data()
    return render(request, "index.html", {"staff_data": data, "trained": True})

def detection_view(request):
    data = _get_staff_data()
    return render(request, "index.html", {"staff_data": data, "detection": True})


def video_feed(request):
    return StreamingHttpResponse(
        gen(VideoCamera()), content_type="multipart/x-mixed-replace; boundary=frame"
    )
