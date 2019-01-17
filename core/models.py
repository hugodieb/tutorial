from django.db import models
from django.contrib.auth.models import User

class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser")
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Todo(models.Model):
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)

    def to_dict_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'done': self.done,
        }


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    hometown = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=100, unique=True)
    youtube_id = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title


class Tutorial(models.Model):
    title = models.CharField(max_length=100, unique=True)
    videos = models.ManyToManyField(Video)
    description = models.TextField(max_length=500, blank=True, null=True)
    similar = models.ManyToManyField('self', blank=True, null=True)

    def __str__(self):
        return self.title
