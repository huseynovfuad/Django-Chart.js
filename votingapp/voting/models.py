from django.db import models

# Create your models here.



class Poll(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length = 100)
    option2 = models.CharField(max_length = 100)
    option3 = models.CharField(max_length = 100)
    option1_count = models.PositiveIntegerField(default=0)
    option2_count = models.PositiveIntegerField(default=0)
    option3_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Poll'
        verbose_name_plural = 'Poll'
        ordering = ['-id']
    
    def __str__(self):
        return "%s"%(self.question)