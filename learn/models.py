from django.db import models
from django.core.urlresolvers import reverse
from accounts.models import User
from ckeditor.fields import RichTextField

def in_upload_path(instance, filename):
    """ Function to return upload path for test case input file"""
    return "/".join(["testcases", str(instance.lesson.id)]) + ".in"


def out_upload_path(instance, filename):
    """ Function to return upload path for test case output file"""
    return "/".join(["testcases", str(instance.lesson.id)]) + ".out"

class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return '/learn/category?category-id=' + str(self.id)

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # 课程所属分类
    course_name = models.CharField(max_length=255, unique=True)
    brief = models.TextField()
    overview = RichTextField()
    release_date = models.DateTimeField(auto_now_add=True)
    course_auth = models.CharField(max_length=255, default='admin')

    class Meta:
        ordering = ['course_name']

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return '/learn/course?course-id=' + str(self.id)
    
    def total_lesson(self):
        return self.lesson_set.all().count()

class Lesson(models.Model): 
    LANGUAGE_IN_LESSON_CHOICES = (
        ('Python', 'Python'),
        ('C', 'C'),
        ('C++', 'C++'),
        ('Java', 'Java')
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=255)
    lesson_num = models.IntegerField()
    learn = RichTextField()
    instructions = RichTextField()
    hint = RichTextField()
    language = models.CharField(max_length=32, choices=LANGUAGE_IN_LESSON_CHOICES, default='C')
    time_limit = models.CharField(max_length=16) # 解题代码时间限制
    memory_limit = models.CharField(max_length=16) # 解题代码内存限制
    precode = models.TextField(blank=True) # 代码编辑区预设代码

    class Meta:
        index_together = ['course', 'lesson_num']

    def __str__(self):
        return str(self.course.course_name + ' ' + self.lesson_name)

    def get_absolute_url(self):
        return '/learn/lesson?lesson-id=' + str(self.id)

class Testcase(models.Model):
    lesson = models.ForeignKey(Lesson)
    inputfile = models.FileField(upload_to=in_upload_path)
    outputfile = models.FileField(upload_to=out_upload_path)

class Submission(models.Model):
    lesson = models.ForeignKey(Lesson)
    submission_time = models.DateTimeField(auto_now_add=True)
    submitter = models.ForeignKey('accounts.User')
    code = models.TextField()
    status = models.CharField(max_length=8, default='') # 判题结果
    result = models.TextField(default='') # 代码执行后的标准输出和标准错误

class HaveLearned(models.Model):
    user = models.ForeignKey('accounts.User')
    lesson = models.ForeignKey(Lesson)

class TriedCourse(models.Model):
    user = models.ForeignKey('accounts.User')
    course = models.ForeignKey(Course)

