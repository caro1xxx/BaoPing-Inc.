## 接口

方法：post

url：/register/

参数（示例）：

{"data": {"name": "xiaohua", "username": "xiaotest", "pwd": "xiaohuaxiaohua", "email": "isliliyu@gmail.com", "email_code": "234986"}}



方法：post

url：/sendemailcode/

参数（示例）：{"email": "isliliyu@gmail.com"}


方法：post

url：/voteactivity/

参数（示例）：
```
{
    "token": "zxCPvHNrcp2GwOMEWLZshaIylR1UTdDg",
    "data": {
        "vote_name": "acafjfi",
        "create_user_username": "yangjie",
        "create_time": "0",
        "img": "0",
        "expire_time": "0",
    }
}
```


方法：put

url：/voteactivity/

参数（示例）：
```
{
    "token": "zxCPvHNrcp2GwOMEWLZshaIylR1UTdDg",
    "data": {
        "content": "activity_settings",
        "vote_id": "413295",
        "vote_everyday_begin_time": "0",
        "vote_everyday_end_time": "0",
        "vote_enroll_begin_time": "0",
        "vote_enroll_end_time": "0",
        "allowed_vote_region": "0",
        "visit_count": "0",
        "visit_count_multiple": "1"
    }
}
{
    "token": "zxCPvHNrcp2GwOMEWLZshaIylR1UTdDg",
    "data": {
        "content": "vote_settings",
        "vote_id": "413295",
        "vote_count_restrict": "0",
        "today_start_voteuser_open_id": "wxxiaotest",
        "today_star_update_begin_time": "0",
        "today_star_update_end_time": "0",
        "allowed_alone_everyday_vote_count": "0",
        "allowed_alone_everyhour_vote_count": "0",
        "open_today_star_with": "0",
		"visible_no1_with": "0",
		"enable_vote_to_me": "0",
		"enable_comment": "0",
		"enable_vote_cert_code": "0"
    }
}
{
    "token": "zxCPvHNrcp2GwOMEWLZshaIylR1UTdDg",
    "data": {
        "content": "auto_comment_settings",
        "vote_id": "413295",
        "auto_comment_voteuser_open_id": "wxiaotest",
        "auto_comment_begin_time": "0",
        "auto_comment_end_tie": "0",
        "auto_comment_everyday_begin_time": "0",
        "auto_comment_everyday_end_time": "0",
        "auto_comment_space_minute": "0",
        "auto_comment_everyday_count_strict": "0"
    }
}
```



方法：get

url：/officialaccount/

参数（示例）：
null



方法：put

url：/officialaccount/

参数（示例）：
```
{
    "token": "zxCPvHNrcp2GwOMEWLZshaIylR1UTdDg",
    "data": {
        "name": "商户名",
        "app_id": "fajhkdf413295",
        "region": "Shanghai",
        "wx_pay_pos_id": "wxgsfd343240",
        "wx_pay_apiv2_secret_key": "wxpaygfnkdjg34",
        "wx_pay_apiv3_secret_key": "wxpaygfnkdjg34"
    }
}
```

方法：get

url：/login

参数（示例）：
```
{
    "token": "zxCPvHNrcp2GwOMEWLZshaIylR1UTdDg",
}
```


方法：post

url：/login

参数（示例）：
```json
{
    "token": "zxCPvHNrcp2GwOMEWLZshaIylR1UTdDg",
    "data": {
        "name": "商户名",
        "app_id": "fajhkdf413295",
        "region": "Shanghai",
        "wx_pay_pos_id": "wxgsfd343240",
        "wx_pay_apiv2_secret_key": "wxpaygfnkdjg34",
        "wx_pay_apiv3_secret_key": "wxpaygfnkdjg34"
    }
}
```



方法：get

url：/paymentrecord/

参数（示例）：

```json
{
    "token": "zxCPvHNrcp2GwOMEWLZshaIylR1UTdDg",
    "value": "all/serch key搜索关键字/不传", 
  	"page_num": "页码/不传"
}
```



方法：delete

url：/paymentrecord/

参数（示例）：

```json
{
    "token": "zxCPvHNrcp2GwOMEWLZshaIylR1UTdDg",
    "pk": ""
}
```



方法：get

url：/voterecord/

参数（示例）：

```json
{
    "token": "zxCPvHNrcp2GwOMEWLZshaIylR1UTdDg",
    "value": "all/serch key搜索关键字/不传", 
  	"page_num": "页码/不传"
}
```



方法：delete

url：/voterecord/

参数（示例）：

```json
{
    "token": "zxCPvHNrcp2GwOMEWLZshaIylR1UTdDg",
    "pk": ""
}
```



