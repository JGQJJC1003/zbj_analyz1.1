# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    user_name = models.CharField(max_length=32, blank=True, null=True)
    user_case = models.CharField(max_length=256, blank=True, null=True)
    price = models.CharField(max_length=16, blank=True, null=True)
    comment_time = models.CharField(max_length=16, blank=True, null=True)
    impression = models.CharField(max_length=256, blank=True, null=True)
    company_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=32, blank=True, null=True)
    user_case = models.CharField(max_length=256, blank=True, null=True)
    price = models.CharField(max_length=16, blank=True, null=True)
    company_id = models.CharField(max_length=32, blank=True, null=True)
    comment_time = models.CharField(max_length=16, blank=True, null=True)
    impression = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class Company(models.Model):
    cid = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=256)
    company_address = models.CharField(max_length=128, blank=True, null=True)
    company_level = models.CharField(max_length=16, blank=True, null=True)
    company_icon = models.CharField(max_length=256, blank=True, null=True)
    company_link = models.CharField(max_length=256, blank=True, null=True)
    company_type = models.CharField(max_length=8, blank=True, null=True)
    company_deposit = models.CharField(max_length=128, blank=True, null=True)
    serviced_employer = models.CharField(max_length=16, blank=True, null=True)
    head_turn = models.CharField(max_length=16, blank=True, null=True)
    good_rate = models.CharField(max_length=16, blank=True, null=True)
    impression_tips = models.CharField(max_length=256, blank=True, null=True)
    company_income = models.CharField(max_length=128, blank=True, null=True)
    item_title = models.CharField(max_length=16, blank=True, null=True)
    link_name = models.CharField(max_length=16, blank=True, null=True)
    company_id = models.CharField(max_length=16, blank=True, null=True)
    ability_number1 = models.CharField(max_length=8, blank=True, null=True)
    ability_number2 = models.CharField(max_length=8, blank=True, null=True)
    ability_number3 = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=128)
    user_password = models.CharField(max_length=128, blank=True, null=True)
    user_email = models.CharField(max_length=128, blank=True, null=True)
    user_phone = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Work(models.Model):
    case_id = models.AutoField(primary_key=True)
    case_name = models.CharField(max_length=255, blank=True, null=True)
    case_img = models.CharField(max_length=255, blank=True, null=True)
    case_link = models.CharField(max_length=255, blank=True, null=True)
    case_price = models.CharField(max_length=32, blank=True, null=True)
    company_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work'


class Works(models.Model):
    case_id = models.AutoField(primary_key=True)
    case_name = models.CharField(max_length=255, blank=True, null=True)
    case_img = models.CharField(max_length=255, blank=True, null=True)
    case_link = models.CharField(max_length=255, blank=True, null=True)
    case_price = models.CharField(max_length=32, blank=True, null=True)
    company_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'works'
