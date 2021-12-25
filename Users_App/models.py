from django.db import models

from django.contrib.auth.models import User # for the purpose of accessing ForeignKey from auth_user tbl

# Create your models here.

class ward_manager(models.Model):
    login_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    w_id=models.AutoField(primary_key=True) # id is automatically genertating
    ward_number=models.IntegerField()
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    phone=models.IntegerField()
    pincode=models.IntegerField()
    email=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    taluk=models.CharField(max_length=50)



class election_setter(models.Model):
    ward_id=models.ForeignKey(ward_manager,on_delete=models.CASCADE,null=True)
    e_id=models.AutoField(primary_key=True)
    datetime=models.DateTimeField(auto_now=True, auto_now_add=False)
    election_name=models.CharField(max_length=50)
    year=models.IntegerField()
    status=models.CharField(max_length=50)


# class booth_member(models.Model):
#     login_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
# 	  ward_id=models.ForeignKey(ward_manager,on_delete=models.CASCADE,null=True)

#     b_id=models.AutoField(primary_key=True)
#     memb_name=models.CharField(max_length=100)
#     email=models.CharField(max_length=100)
#   created_datetime=models.DateTimeField(auto_now=True, auto_now_add=True)

# class voter_data(models.Model):
#     booth_id=models.ForeignKey(booth_member,on_delete=models.CASCADE,null=True)
#     ward_id=models.ForeignKey(ward_manager,on_delete=models.CASCADE,null=True)
#     elect_id=models.ForeignKey(election_setter,on_delete=models.CASCADE,null=True)

#     v_id=models.AutoField(primary_key=True)
#     voter_no=models.IntegerField()
#     idproof=models.IntegerField()
#     voter_name=models.CharField(max_length=100)
#     age=models.IntegerField()
#     phone=models.IntegerField()
