from django.db import models

class Guest(models.Model):
    title = models.CharField(max_length=50);
    content = models.TextField();
    regdate = models.DateField(auto_now_add=True); #수정 불가

    class Meta:
        db_table = 'db_guest'

class Article(models.Model):
    id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=30);
    price = models.IntegerField();
    pub_date = models.DateField(auto_now=True); #날짜를 자동적으로 집어넣음
    class Meta:
        db_table = 'db_article'

class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    imgname = models.CharField(max_length=20, blank=True, null=True)
    regdate = models.DateField(auto_now=True)

    class Meta:
        db_table = 'db_item'

class Cust(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    pwd = models.CharField(max_length=10)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'db_cust'

class Cart(models.Model):
    custid = models.ForeignKey(Cust, on_delete=models.CASCADE, related_name='custid')
    itemid = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='itemid')
    num = models.IntegerField(blank=True, null=True)
    regdate = models.DateField(auto_now=True)

    class Meta:
        db_table = 'db_cart'
