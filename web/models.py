# -*- coding: UTF-8 -*-
from django.db import models

# 日誌
class Diary(models.Model):
        memo = models.TextField()
        time = models.DateTimeField(auto_now_add=True)
        def __unicode__(self):
                return self.memo


# 月份
class Month(models.Model):
        date = models.IntegerField(default=0)
        
        def __unicode__(self):
                return str(self.date)

# 帳目
class Money(models.Model):
        item = models.CharField(max_length=30)
        kind = models.IntegerField(default=0)
        price = models.IntegerField(default=0)
        time = models.DateTimeField(auto_now_add=True)

        def __unicode__(self):
                return self.item