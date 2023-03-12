from django.db import models
from django.core.files import File
from vote_manage import settings

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

    def natural_key(self):
        return {'name': self.name, 'username': self.username}


class Domain(models.Model):
    domain_name = models.CharField(max_length=50, unique=True)
    status = models.IntegerField(default=0)
    visit_count = models.IntegerField(default=0)
    expire_time = models.IntegerField()
    flow = models.IntegerField()
    vote_id = models.IntegerField()


class VoteUser(models.Model):
    open_id = models.CharField(unique=True, max_length=128, db_index=True)
    wx_username = models.TextField()
    create_time = models.IntegerField(null=False)
    avator = models.TextField(default='')

    def natural_key(self):
        return {'open_id': self.open_id, 'wx_username': self.wx_username, 'avator': self.avator}


class VoteActivity(models.Model):
    create_user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE, related_name='user')
    vote_id = models.IntegerField(unique=True, db_index=True)
    flow = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    img = models.FileField(upload_to='img', blank=True, verbose_name='缩略图')
    income = models.IntegerField(default=0)
    domain = models.ForeignKey(Domain, to_field='domain_name', on_delete=models.CASCADE)
    create_time = models.IntegerField()
    expire_time = models.IntegerField()
    name = models.TextField(default='')
    vote_everyday_begin_time = models.IntegerField(default=0)
    vote_everyday_end_time = models.IntegerField(default=0)
    vote_enroll_begin_time = models.IntegerField(default=0)
    vote_enroll_end_time = models.IntegerField(default=0)
    allowed_vote_region = models.TextField(default='')
    visit_count = models.IntegerField(default=0)
    visit_count_multiple = models.IntegerField(default=1)
    vote_count_restrict = models.TextField(default='[]')
    today_start_voteuser = models.CharField(max_length=128, default='')
    today_star_update_begin_time = models.IntegerField(default=0)
    today_star_update_end_time = models.IntegerField(default=0)
    allowed_alone_everyday_vote_count = models.IntegerField(default=0)
    allowed_alone_everyhour_vote_count = models.IntegerField(default=0)
    open_today_star_with = models.IntegerField(default=0)
    visible_no1_with = models.IntegerField(default=0)
    enable_vote_to_me = models.IntegerField(default=0)
    enable_comment = models.IntegerField(default=0)
    enable_vote_cert_code = models.IntegerField(default=0)
    enable_prize = models.IntegerField(default=0)
    enable_browser = models.IntegerField(default=0)
    auto_comment_voteuser = models.CharField(max_length=128, default='')
    auto_comment_begin_time = models.IntegerField(default=0)
    auto_comment_end_time = models.IntegerField(default=0)
    auto_comment_everyday_begin_time = models.IntegerField(default=0)
    auto_comment_everyday_end_time = models.IntegerField(default=0)
    auto_comment_space_minute = models.IntegerField(default=0)
    auto_comment_everyday_count_strict = models.IntegerField(default=0)
    template_id = models.IntegerField(default=1)
    description = models.TextField(default='')
    enterprises = models.TextField(default='')
    prize = models.TextField(default='')
    support = models.TextField(default='')
    contact = models.TextField(default='')

    top_roll_text = models.TextField(default='')
    start_adv_img = models.FileField(upload_to='img', blank=True, verbose_name='开场广告图')
    bottom_text = models.TextField(default='')
    video_adv = models.FileField(upload_to='video', blank=True, verbose_name='视频广告')
    target_video_adv = models.FileField(upload_to='vedio', blank=True, verbose_name='视频广告')
    bottom_support_text = models.TextField(default='')
    carousel_list = models.TextField(default='[]')
    temp_file = models.FileField(upload_to='temp', blank=True, verbose_name='临时文件')
    bottom_copyright = models.TextField(default='')
    officialcount_qrcode = models.FileField(upload_to='qr', blank=True, verbose_name='公众号二维码')
    popup = models.TextField(default='')
    vote_button_name = models.TextField(default='点赞')
    vote_unit_name = models.TextField(default='个')
    track_report = models.TextField(default='')
    vote_voteusers = models.ManyToManyField(
        VoteUser,
        through='VoteRecord',
        through_fields=('vote_activity', 'voteuser')
    )
    # payment_voteusers = models.ManyToManyField(
    #     PaymentRecord,
    # )

class VoteTarget(models.Model):
    vote_id = models.ForeignKey(VoteActivity, to_field='vote_id', on_delete=models.CASCADE)
    detail = models.TextField(default='')
    name = models.CharField(max_length=64)
    count = models.IntegerField(default=0)
    avator = models.FileField(upload_to='img', blank=True, null=True,
        # default=File(open(str(settings.MEDIA_ROOT) + '/img/1.png')),
        default = 'img/1.png'
    )
    status = models.IntegerField(default=0)
    def natural_key(self):
        return {'name': self.name, 'vote_id': self.vote_id, 'avator': self.avator}


class Feedback(models.Model):
    voteuser = models.ForeignKey(VoteUser, to_field='open_id', on_delete=models.CASCADE)
    content = models.TextField(null=False)
    vote_activity = models.ForeignKey(VoteActivity, to_field='vote_id', on_delete=models.CASCADE)
    create_time = models.IntegerField(null=False)


class ApplyPrize(models.Model):
    voteuser = models.ForeignKey(VoteUser, to_field='open_id', on_delete=models.CASCADE, related_name='voteuser')
    name = models.CharField(max_length=8)
    phone_number = models.CharField(max_length=11)
    create_time = models.IntegerField()
    status = models.IntegerField(default=False)
    vote_activity = models.IntegerField(db_index=True, default=0)


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
    qr_img = models.FileField(upload_to='img/offcial_account_qr/', blank=True, verbose_name='公众号二维码')


class Active(models.Model):
    domain_list = models.CharField(max_length=100)


class VoteRecord(models.Model):
    voteuser = models.ForeignKey(VoteUser, to_field='open_id', on_delete=models.CASCADE)
    vote_target = models.ForeignKey(VoteTarget, to_field='id', on_delete=models.CASCADE)
    create_time = models.IntegerField(null=False)
    vote_activity = models.ForeignKey(VoteActivity, to_field='vote_id', on_delete=models.CASCADE)
    ip = models.TextField(default='')
    phone_model = models.TextField(default='')
    system = models.TextField(default='')   
    network = models.TextField(default='')


class PaymentRecord(models.Model):
    voteuser = models.ForeignKey(VoteUser, to_field='open_id', on_delete=models.CASCADE)
    vote_activity = models.ForeignKey(VoteActivity, to_field='vote_id', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    create_time = models.IntegerField(null=False)
    ip = models.TextField(default='')
    phone_number = models.TextField(default='')
    phone_model = models.TextField(default='')
    system = models.TextField(default='')
    network = models.TextField(default='')  
    prize_type = models.TextField(default='')
    payment_order_id = models.TextField(default='')
    payment_status = models.IntegerField(default=0)
    # wxpay_transaction_id = models.TextField(default='')
    # wxpay_prepay_id = models.TextField(default='')


class Statics(models.Model):
    today_income = models.IntegerField(default=0)
    yesterday_income = models.IntegerField(default=0)
    update_time = models.IntegerField(default=0)


class StaticsHistory(models.Model):
    day_income = models.IntegerField(default=0)
    day_time = models.IntegerField(default=0)
    create_time = models.IntegerField(default=0)


class Settings(models.Model):
    name = models.TextField(default='')
    value = models.TextField(default='')


class Keys(models.Model):
    value = models.CharField(default='', db_index=True, max_length=128)
    expire_time = models.IntegerField(default=0)
    user_agent = models.ForeignKey(VoteUser, to_field='open_id', on_delete=models.CASCADE)
    has_used = models.IntegerField(default=0)


class Gift(models.Model):
    name = models.TextField(default='')
    value = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    img = models.FileField(upload_to='img/gift', blank=True, verbose_name='礼物图标', default='img/gift/rose.png')
    

class CommentRecord(models.Model):
    vote_target = models.ForeignKey(VoteTarget, to_field='id', on_delete=models.CASCADE)
    vote_user = models.ForeignKey(VoteUser, to_field='open_id', on_delete=models.CASCADE)
    content = models.TextField(default='')
    create_time = models.IntegerField(default=0)
    status = models.IntegerField(default=0)


class BlackList(models.Model):
    open_id = models.TextField(default='', null=True)
    ip = models.TextField(default='', null=True)


class TempFile(models.Model):
    file = models.FileField(upload_to='temp', blank=True, verbose_name='临时文件')


class AutoComment(models.Model):
    vote_id = models.TextField(default='')
    vote_target_id = models.TextField(default='')
    begin_time = models.IntegerField(default=0)
    end_time = models.IntegerField(default=0)
    day_begin_time = models.IntegerField(default=0)
    day_end_time = models.IntegerField(default=0)
    space = models.IntegerField(default=0)
    day_count_strict = models.IntegerField(default=0)
    update_time = models.IntegerField(default=0)
    day_vote_count = models.IntegerField(default=0)


class Task(models.Model):
    task_id = models.CharField(default='null', max_length=6, db_index=True)
    name = models.TextField(default='')
    status = models.TextField(default='')
    msg = models.TextField(default='')
    create_time = models.IntegerField(default=0)
