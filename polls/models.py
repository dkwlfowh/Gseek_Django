from django.db import models


class SqlText(models.Model):
    date = models.DateTimeField(primary_key=True)
    gseek_id = models.CharField(max_length=20)
    user = models.CharField(max_length=20, blank=True, null=True)
    host = models.CharField(max_length=100, blank=True, null=True)
    state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sql_text'
        unique_together = (('date', 'gseek_id'),)

    def __str__(self):
        return self.state


class State(models.Model):
    date = models.DateTimeField(primary_key=True)
    thread = models.CharField(max_length=20)
    user = models.CharField(max_length=20, blank=True, null=True)
    host = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)
    avg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'
        unique_together = (('date', 'thread'),)
    def __str__(self):
        return self.state