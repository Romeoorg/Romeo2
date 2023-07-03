from django.db import models
import uuid


# Create your models here.
class my_table(models.Model):

    tittle = models.CharField(max_length=2000)
    description = models.TextField(null=True,blank= True)
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link=models.CharField(max_length=2000,null=True,blank=True)
    tags=models.ManyToManyField('Tag',blank=True)
    vote_total=models.IntegerField(default=0,null=True,blank=True)
    value_ratio=models.IntegerField(default=0,null=True,blank=True)
    create =  models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self): #this is for the tables created in the adminstration to have a meaning
        return self.tittle

#the child model(review table),1 to many relationship

class Review(models.Model):

    my_table=models.ForeignKey(my_table,on_delete=models.CASCADE)

    body=models.TextField(null=True,blank=True)
    value=models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.value
    
    #child model(tag table),many to may relationship
class Tag(models.Model):

    name=models.CharField(max_length=200)
    create =  models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.name

