from django.db import models

# Create your models here.
# Q_1,Q_2,Q_3,Q_4,Q_5,Q_6,Q_7,Q_8,Q_9,Q_10,Q_11,Q_12

class contents(models.Model):
    contents_name = models.CharField( max_length=50)
    contents_href = models.CharField( max_length=100)
    contents_type = models.CharField( max_length=50)
    cluster_label = models.CharField(max_length=50, null=True, blank = True)

    def __str__(self):
        return self.contents_name

class survey(models.Model):
    USER_ID = models.CharField(max_length=50)
    Q_1 = models.IntegerField()
    Q_2 = models.IntegerField()
    Q_3 = models.IntegerField()
    Q_4 = models.IntegerField()
    Q_5 = models.IntegerField()
    Q_6 = models.IntegerField()
    Q_7 = models.IntegerField()
    Q_8 = models.IntegerField()
    Q_9 = models.IntegerField()
    Q_10 = models.IntegerField()
    Q_11 = models.IntegerField()
    Q_12 =models.IntegerField()

    def __str__(self):
        return self.USER_ID
