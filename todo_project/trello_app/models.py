from django.db import models
from django.utils import timezone

# Create your models here.


#Requirements
    # -Tasks 
    #     -Content 
    #     -creation date
    #     -deadline
    #     - TaskList  

    #     -status
    #     -completed_on    
    #
    #  -TaskList
            # -name
# Tables
#     * Task Tables
#     id | content | creation_table | deadline | task_list_id | completed_on 
#     * Task List
#         (like all task related to college in one)
#         id | Name | created_at



class TaskList(models.Model):
    def __str__ (self):
        return self.name
    name = models.TextField(max_length=50)
    # created_at = models.DateTimeField(default = timezone.now)
    created_at = models.DateTimeField(default = timezone.localtime)
    

    
class Task(models.Model):
    def __str__(self):
        return f"{self.content}-{self.task_list}"
    content = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)
    # created_at = models.DateTimeField(default= timezone.localtime())
    deadline = models.DateTimeField(blank=True , null= True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('P','PENDING'),
        ('C','COMPLETE'),
        ('IP','IN_PROGRESS'),
        ('D','DROPPED')
    )
    status = models.CharField(choices=STATUS_CHOICES,default=STATUS_CHOICES[2],max_length=2)
    