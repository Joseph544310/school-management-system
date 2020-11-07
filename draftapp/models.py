from django.db import models


class Student(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    # Student_ID = models.IntegerField(default=0, unique=True)
    SEX = [
        ("M", "Male"),
        ("F", "Female")
    ]
    Sex = models.CharField(max_length=1, choices=SEX,  default= 'Male')
    GRADE = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12)
    ]
    Grade = models.IntegerField(choices=GRADE, default=1)
    Nationality=models.CharField(max_length=20, default='Lebanese')
    Born_in= models.IntegerField( default=1970)                              #used to be int
    Father = models.CharField(max_length=20, default='unknown')
    Mother = models.CharField(max_length=20, default='unknown')
    City = models.CharField(max_length=20, default='unknown')
    Address = models.CharField(max_length=20, default='address')
    Building = models.CharField(max_length=20, default='unknown')
    Floor = models.CharField(max_length=20, default='unknown')
    Fixed=models.IntegerField( default=0)                                   #used to be int
    Mobile=models.IntegerField( default=0)                                  #used to be int
    HEALTH = [
        ("H","Healthy"),
        ("NH","Sickboi")
    ]
    Medical_state = models.CharField(max_length=3,  choices=HEALTH ,  default= 'Healthy' )
    Bloodtype = [
        ('A', 'A+'),
        ('A', 'A-'),
        ('B', 'B+'),
        ('B', 'B-'),
        ('AB', 'AB+'),
        ('AB', 'AB-'),
        ('O', 'O+'),
        ('O', 'O-')
    ]
    Student_Bloodtype = models.CharField(max_length=3, choices=Bloodtype,  default= 'A+')
    MorF=[
        ("M","Mother"),
        ("F","Father")
    ]
    Guardian = models.CharField(max_length=1, choices=MorF, default= 'Mother')
    Guardian_Phone=models.IntegerField( default=0)                       #used to be int
    Guardian_Level_of_Education = models.CharField(max_length=20, default='unknown')
    Guardian_City = models.CharField(max_length=20, default='unknown')
    Guardian_Address = models.CharField(max_length=20, default='unknown')
    Guardian_Building = models.CharField(max_length=20, default='unknown')
    Guardian_Bloodtype= models.CharField(max_length=3, choices=Bloodtype,  default= 'A+')

    def __str__(self):
        temp=str(self.Student_ID)
        return self.First_Name + '-' + self.Last_Name + '-' + temp


class Teacher(models.Model):
    First_Name= models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    # Teacher_ID= models.IntegerField(primary_key=True)
    Teaches = [

        ("E","English"),
        ("E","Arabic"),
        ("E","Math"),
        ("E","Physics"),
        ("E","Biology"),
        ("E","Chemistry"),
        ("E","History"),
        ("E","Geography"),
        ("E","Civics"),
        ("E","Religion"),
        ("E","PE")
    ]
    Subject= models.CharField(max_length=1, choices=Teaches)

    SEX = [
        ("M", "Male"),
        ("F", "Female")
    ]
    Sex = models.CharField(max_length=1, choices=SEX)
    Nationality=models.CharField(max_length=20)
    Born_in= models.IntegerField( default=1970)                                 #used to be int
    City = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    Building = models.CharField(max_length=20)
    Floor = models.CharField(max_length=20)
    Fixed=models.IntegerField(default=0)                                                              #used to be int
    Mobile=models.IntegerField(default=0)                                                               #used to be int
    Bloodtype = [
        ('A', 'A+'),
        ('A', 'A-'),
        ('B', 'B+'),
        ('B', 'B-'),
        ('AB', 'AB+'),
        ('AB', 'AB-'),
        ('O', 'O+'),
        ('O', 'O-')
    ]
    Bloodtype = models.CharField(max_length=3, choices=Bloodtype)

    def __str__(self):
        return self.First_Name + '-' + self.Last_Name

