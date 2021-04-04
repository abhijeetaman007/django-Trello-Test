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
    name = models.TextField(max_length=50)
    created_at = models.DateTimeField(default = timezone.now)
    
class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default= timezone.now)
    deadline = models.DateTimeField(blank=True , null= True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
