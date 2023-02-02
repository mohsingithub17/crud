from django.db import models
class Emp(models.Model):
    ename=models.CharField(max_length=20)
    sal=models.IntegerField()
    address=models.CharField(max_length=20)
    img=models.ImageField(upload_to='pics')
    def __str__(self) -> str:
        return self.ename
