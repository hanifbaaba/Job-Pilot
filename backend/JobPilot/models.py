from django.db import models

class CreateJob(models.Model):
      job_title = models.CharField(max_length=100)
      description = models.TextField()
      salary = models.DecimalField(max_digits=10, decimal_places=2)
      company_name = models.CharField(max_length=100)
      location = models.CharField(max_length=100)
      category = models.CharField(max_length=100)
      EXPERIENCE_CHOICES = [
      ('junior', 'Junior'),
      ('mid', 'Mid'),
      ('senior', 'Senior'),
      ]
      experience = models.CharField(max_length=200, default='junior',blank=True, choices=EXPERIENCE_CHOICES)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      
      def __str__(self):
            return self.job_title
      
class ApplyJob(models.Model):
      job = models.ForeignKey(CreateJob,on_delete=models.CASCADE,related_name='applications')
      name = models.CharField(max_length=200)
      email = models.EmailField()
      reason_for_applying = models.TextField()
      country_of_residence = models.CharField(max_length=200)
      resume_upload = models.FileField(upload_to='CV/', blank=True, null=True)
      portfolio_link = models.URLField(max_length=355)
      preferred_salary =  models.DecimalField(max_digits=10, decimal_places=2)
