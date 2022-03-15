from django.db import models
from django.utils import timezone

course_list = (
    ('1st PUC', "1st PUC"),
    ('2nd PUC', "2nd PUC"),
    ('BCA',"BCA"),
    ('BCOM',"BCOM"),
    ('B.Tech',"B.Tech"),
    ('BA', "BA"),
    ('BBA', "BBA"),
    ('B.Sc', "B.Sc"),
    ('BHM', "BHM"),
    ('MBBS', "MBBS"),
    ('B.E - Mechanical',"B.E - Mechanical"),
    ('B.E - Civil',"B.E - Civil"),
    ('B.E - Computer Science',"B.E - Computer Science"),
    ('B.E - EC',"B.E - EC"),
    ('MCA',"MCA"),
    ('MBA', "MBA"),
    ('MCOM',"MCOM"),
    ('MHM', "MHM"),
    ('MFA', "MFA"),
    ('M.Tech', "M.Tech"),
    ('M.Sc', "M.Sc"),
    ('MSW', "MSW"),
    ('PGDM', "PGDM"),
    ('PGDM(BA)', "PGDM(BA)"),
    ('PH.d', "PH.d"),
    ('Others',"Others"),
)

class Material(models.Model):
    semester = models.PositiveIntegerField(default=1)
    course = models.CharField(choices=course_list, max_length=40)
    subject = models.CharField(max_length=200)
    material = models.FileField(upload_to='media/')
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.course
