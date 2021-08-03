from django.db import models

class Author(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    Name = models.CharField(max_length=20, verbose_name='作者名称')
    Gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    Bron_Date = models.CharField(max_length=20, verbose_name='出生日期')

    class Meta:
        db_table = 'tb_author'
        verbose_name = '作者表'

class Book(models.Model):
    BookName = models.CharField(max_length=20, verbose_name='书籍名字')
    Author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='所属作者')
    Publish_Date = models.CharField(max_length=20, verbose_name='发表日期')
    Country = models.CharField(max_length=20, verbose_name='所属国家')

    class Meta:
        db_table = 'tb_book'
        verbose_name = '图书表'