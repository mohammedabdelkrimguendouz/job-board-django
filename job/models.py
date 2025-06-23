from django.db import models


JobTYpe = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    #location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15,choices=JobTYpe, default='Full Time')
    published_on = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.IntegerField(default=1)    
    category = models.ForeignKey(to='Category',on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name