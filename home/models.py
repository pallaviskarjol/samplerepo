from django.db import models
# Create your models here.
class Student(models.Model):
    name = models.CharField('Stdent Name',null=True, max_length=30)
    Branch = models.ForeignKey('Department',on_delete=models.SET_NULL,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.name

class details(models.Model):
	USN = models.CharField('U S N',null=False,max_length=30,unique=True)
	name = models.ForeignKey('Student',on_delete=models.SET_NULL,null=True)
	sem = models.IntegerField('Semester',null=False)
	dob = models.DateField('Date of Birth',null=False)
	cgpa = models.FloatField('CGPA',null=False)
	profile = models.ImageField('profile',upload_to='images/',null=True)

	def __str__(self):
		return self.USN

class link(models.Model):
	st_name = models.ForeignKey('Student',on_delete=models.SET_NULL,null=True)
	reg_no = models.ForeignKey('details',on_delete=models.SET_NULL,null=True)

class Department(models.Model):
	dept = (('CSE','Computer Science'),('ISE','Information Science'))
	department = models.CharField('Name',choices= dept,max_length=30,null=True)
	HOD = models.CharField('Head Of Dept',null=True,max_length=30)

	def __str__(self):
		return self.department;

class Employee(models.Model):
	firstname = models.CharField('firstname',null=False,max_length=20)
	lastname = models.CharField('lastname',null=True,max_length=20,default='')
	department = models.ForeignKey('Department',on_delete=models.SET_NULL,null=True)

	def __str__(self):
		return self.firstname+self.lastname;

class Section(models.Model):
	Section_name = models.CharField('Sect_name',null=False,max_length=10)
	Advisor = models.OneToOneField('Employee',on_delete=models.SET_NULL,null=True)
	students = models.ManyToManyField('Student',null=False)

	def __str__(self):
		return self.Section_name;

