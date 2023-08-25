from django.db import models

# Create your models here.


class Province(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Municipality(models.Model):
    type = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Wardnumber(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Road(models.Model):
    name = models.CharField(max_length=100)
    roadnumber = models.CharField(max_length=1)
    wardnumber = models.ForeignKey(Wardnumber, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Chowk(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    road = models.ForeignKey(Road, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class HashedLocation(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    wardnumber = models.ForeignKey(Wardnumber, on_delete=models.CASCADE)
    road = models.ForeignKey(Road, on_delete=models.CASCADE)
    chowk = models.ForeignKey(Chowk, on_delete=models.CASCADE, null=True)
    locationnumber = models.CharField(max_length=100)
    locationoffset = models.CharField(max_length=100)
    locationType = models.CharField(max_length=100)
