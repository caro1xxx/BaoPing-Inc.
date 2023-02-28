from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    pwd = models.CharField(max_length=64)
    create_time = models.IntegerField()
    last_login_time = models.IntegerField()
    email = models.CharField(max_length=50, unique=True)
    # 0: admin, 1: guest
    auth = models.IntegerField(default=1)
    avator = models.TextField(max_length=10, default='22')
    token = models.CharField(max_length=32)
    # 1: 正常 0: 其他
    status = models.IntegerField(default=1)


class Domain(models.Model):
    domain_name = models.CharField(max_length=50, unique=True)
    status = models.IntegerField(default=0)
    visit_count = models.IntegerField(default=0)
    expire_time = models.IntegerField()
    flow = models.IntegerField()


class VoteActivity(models.Model):
    create_user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE, related_name='user')
    vote_id = models.IntegerField(unique=True)
    flow = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    img = models.IntegerField(default=0)
    income = models.IntegerField(default=0)
    domain = models.ForeignKey(Domain, to_field='domain_name', on_delete=models.CASCADE)
    create_time = models.IntegerField()
    expire_time = models.IntegerField()


class VoteUser(models.Model):
    open_id = models.CharField(unique=True, max_length=128)
    wx_username = models.TextField()
    create_time = models.IntegerField(null=False)
    avator = models.TextField(default='')


class Feedback(models.Model):
    voteuser = models.ForeignKey(VoteUser, to_field='open_id', on_delete=models.CASCADE)
    content = models.TextField(null=False)
    # vote_id = models.models.IntegerField()
    create_time = models.IntegerField(null=False)


class ApplyPrize(models.Model):
    voteuser = models.ForeignKey(VoteUser, to_field='open_id', on_delete=models.CASCADE)
    name = models.CharField(max_length=8)
    phone_number = models.CharField(max_length=11)
    create_time = models.IntegerField()
    status = models.IntegerField(default=False)


class Token(models.Model):
    value = models.CharField(max_length=32,unique=True)
    expire_time = models.IntegerField()


class Logs(models.Model):
    who = models.CharField(max_length=20)
    action = models.TextField(max_length=20)
    target = models.TextField(max_length=20, null=False)
    create_time = models.IntegerField(null=False)


class OfficialAccount(models.Model):
    officialcount_name = models.TextField()
    app_id = models.TextField()
    region = models.TextField()
    wxpay_pos_id = models.TextField()
    wxpay_apiv2_secret_key = models.TextField()
    wxpay_apiv3_secret_key = models.TextField()


class Active(models.Model):
    domain_list = models.CharField(max_length=100)


class VoteRecord(models.Model):
    wx_username = models.TextField()
    voteuser = models.ForeignKey(VoteUser, to_field='open_id', on_delete=models.CASCADE)
    create_time = models.IntegerField(null=False)
    vote_activity = models.ForeignKey(VoteActivity, to_field='vote_id', on_delete=models.CASCADE)



class PaymentRecord(models.Model):
    voteuser = models.ForeignKey(VoteUser, to_field='open_id', on_delete=models.CASCADE)
    vote_activity = models.ForeignKey(VoteActivity, to_field='vote_id', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    create_time = models.IntegerField(null=False)
    ip = models.TextField(default='')
    phone_number = models.TextField(default='')
    system = models.TextField(default='')
    network = models.TextField(default='')