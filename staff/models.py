from django.db import models


# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    position = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

def staff_directory_path(instance, filename):
    # Create a directory for each staff member using their name
    return f'images/{instance.staff.name}/{filename}'

class StaffFace(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=staff_directory_path)

    def __str__(self) -> str:
        return f'{self.staff} - {self.image}'
    


