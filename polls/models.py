from django.db import models


class DecorationZone(models.Model):
    zone_name = models.CharField(max_length=100)
    zone_cost = models.IntegerField(default=25)

    def __str__(self):
        return self.zone_name


class Actions(models.Model):
    action_name = models.CharField(max_length=100)
    action_cost = models.IntegerField(default=25)

    def __str__(self):
        return self.action_name

# class Project(models.Model):
#     zones = models.ManyToManyField(DecorationZone)
#     scales = (
#         ('decor', 'Декорирование'),
#         ('decor_furniture', 'Декорирование + меблирование'),
#         ('decor_furniture_renovation', 'Декорирование + меблирование + косметический ремонт'),
#     )
#     scale = models.CharField(max_length=50, choices=scales)
#     durations = (
#         ('fastest', 'Как можно быстрее'),
#         ('fast', 'Быстро'),
#         ('normal', 'В обычном режиме'),
#     )
#     duration = models.CharField(max_length=50, choices=durations)
