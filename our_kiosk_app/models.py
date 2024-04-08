from django.db import models

class Variety(models.Model):
    # 패스오더 앱 -> 최대 10자(공백포함)
    name = models.CharField(max_length=15)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Beverage(models.Model):
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    # 패스오더 앱 -> 최대 18자(공백포함)
    name = models.CharField(max_length=25)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name