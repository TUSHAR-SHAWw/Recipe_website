from faker import Faker
from .models import *
import random
from django.db.models import Sum
fake =Faker()

def create_marks(n):
    try:
        students=Student.objects.all()
        subjects=Subject.objects.all()
        # departments=Department.objects.all()
        for student in students:
            for subject in subjects:
                a=StudentMarks.objects.create(
                    student=student,
                    marks=random.randint(0,100),
                    subject=subject
                )
                a.save()
    except Exception as e:
            print(e)

def seed_db(n=100)->None:
    try:
        for i in range(0,n):
            departments_obj= Department.objects.all()
            random_index=random.randint(0,len(departments_obj)-1)
            department=departments_obj[random_index]

            student_id=f"STU-{random.randint(111,999)}"
            student_name=fake.name()
            student_email=fake.email()
            student_age=random.randint(18,30)
            student_address=fake.address()

            stu_id=Student_id.objects.create(student_id=student_id)

            student_obj=Student.objects.create(
                department=department,
                student_id=stu_id,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address
                
            )
            student_obj.save()
    except Exception as e:
        print(e)

def generate_ranks():

    ranks=Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')
    i=1
    for rank in ranks:
        i=i+1
        Report_card.objects.create(
            student=rank,
            rank=i,
            date_of_creation="04/12/2023"
        )