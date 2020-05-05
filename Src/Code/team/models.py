from django.db import models
from user.models import User
from course.models import Course


class Leader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bonus = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class Team(models.Model):
    name = models.CharField(max_length=64, unique=False)
    leader = models.IntegerField(default=0)
    member = models.ManyToManyField(User)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Vote(models.Model):
    # team = models.OneToOneField(Team, on_delete=models.CASCADE, unique=False)
    # member = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)

    team = models.IntegerField(default=0)
    member = models.IntegerField(default=0)
    vote_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

