from django.db import models

class TaskList(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Task List: {self.name}"
    
    
class Item(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(null=True, blank=True, max_length=256)
    completion_date = models.DateTimeField(null=True, blank=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='items')
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Item: {self.title}"