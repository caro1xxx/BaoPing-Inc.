from django.db import models

# Create your models here.

class domain(models.Model):
    domain_name = models.CharField(max_length=50, unique=True)
    status = models.IntegerField(default=0)
    visit_count = models.IntegerField(default=0)
    expire_time = models.IntegerField()
    flow = models.IntegerField()
    vote_id = models.IntegerField()


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


class VoteActivity(models.Model):
    create_user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE, related_name='user')
    vote_id = models.IntegerField(unique=True, db_index=True)
    flow = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    img = models.FileField(upload_to='img', blank=True, verbose_name='缩略图')
    income = models.IntegerField(default=0)
    domain = models.ForeignKey(domain, to_field='domain_name', on_delete=models.CASCADE)
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
    # payment_voteusers = models.ManyToManyField(
    #     PaymentRecord,
    # )
    def natural_key(self):
        return {'name': self.name, 'vote_id': self.vote_id}
