# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=50, verbose_name="课程名称及任课老师")
    course_time = models.CharField(max_length=50, verbose_name="开课时间")
    course_index = models.CharField(max_length=50, verbose_name="上课时间")
    SUBJECT_CHOICES = (
        ('IT', '信息科学与技术学院'),
        ('EE', '电气工程学院'),
        ('CE', '土木工程学院'),
        ('MA', '数学学院'),
        ('ME', '机械工程学院'),
        ('PH', '物理学院'),
        ('HS', '人文学院'),
    )
    course_subject = models.CharField(max_length=2, choices=SUBJECT_CHOICES, verbose_name="开课学院")
    course_description = models.TextField(max_length=200, verbose_name="课程简介")
    course_consume = models.IntegerField(verbose_name="周学时")
    course_choose = models.ManyToManyField(User, blank=True)

    def __unicode__(self):
        return self.course_name

    class Meta:
        ordering = ['id']
        verbose_name = "课程"
        verbose_name_plural = "西南交大选课系统"



class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'course_subject']
