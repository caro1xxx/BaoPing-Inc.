from django.db import models

# Create your models here.

class OfficialAccount(models.Model):
    officialcount_name = models.TextField(default='')
    region = models.TextField(default='')
    wxpay_pos_id = models.TextField(default='')
    wxpay_apiv2_secret_key = models.TextField(default='')
    wxpay_apiv3_secret_key = models.TextField(default='')
    qr_img = models.FileField(upload_to='img/offcial_account_qr/', blank=True, verbose_name='公众号二维码')
    access_token_value = models.TextField(default='')
    access_token_expire_time = models.IntegerField(default=0)
    wxpay_mchid = models.TextField(default='')
    wxpay_appid = models.TextField(default='')
    wxpay_app_key = models.TextField(default='')
    wxpay_notify_url = models.TextField(default='')