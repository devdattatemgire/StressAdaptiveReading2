from django.db import models


class KnowledgeBase(models.Model):
    subject_id = models.CharField(max_length=255)  # varchar
    subject_name = models.CharField(max_length=255)  # varchar
    topic_name = models.CharField(max_length=255)  # varchar
    text = models.CharField(max_length=255)  # varchar
    level = models.CharField(max_length=255)  # varchar
    q1 = models.IntegerField()  # numeric
    q2 = models.IntegerField()  # numeric
    q3 = models.IntegerField()  # numeric
    q4 = models.IntegerField()  # numeric
    q5 = models.IntegerField()  # numeric
    a1 = models.IntegerField()  # numeric
    a2 = models.IntegerField()  # numeric
    a3 = models.IntegerField()  # numeric
    a4 = models.IntegerField()  # numeric
    a5 = models.IntegerField()  # numeric
    
    class Meta:
        db_table = 'custom_knowledge_base_table'  # Set your desired table name here
    def __str__(self):
        return self.subject_name  # You can choose any field as a readable representation


# Create your models here.
