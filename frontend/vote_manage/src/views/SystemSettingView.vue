<!-- 系统设置 -->
<template>
  <div class="system_main">
    <div class="system_main_body">
      <Search />
      <div class="title_style">系统设置</div>
      <div class="system_main_content">
        <div class="setup_table redius1 dislodgeborder">
          <div class="setup_table_head">
            <div>公众号设置</div>
          </div>
          <div class="setup_table_body_wrap">
            <div class="setup_table_body">
              <div class="setup_table_body_left">
                <div class="setup_table_body_head">
                  <div v-for="item in accountHead" :key="item.name">
                    {{ item.name }}
                  </div>
                </div>
                <div class="setup_table_body_content">
                  <div>
                    <input type="text" :value="accountSetuo.accountNam" />
                  </div>
                  <div><input type="text" :value="accountSetuo.appId" /></div>
                  <div>
                    <input type="text" :value="accountSetuo.AppScret" />
                  </div>
                  <div>
                    <input type="text" :value="accountSetuo.Merchant" />
                  </div>
                  <div>
                    <input type="text" :value="accountSetuo.Paymentkey1" />
                  </div>
                  <div>
                    <input type="text" :value="accountSetuo.Paymentkey2" />
                  </div>
                  <div><img :src="accountSetuo.accountinmg" alt="" /></div>
                </div>
              </div>
              <div class="setup_table_body_right">
                <button>提交</button>
              </div>
            </div>
          </div>
        </div>
        <div class="setup_table dislodgeborder">
          <div class="setup_table_head">
            <div>cou云存储</div>
          </div>
          <div class="setup_table_body_wrap">
            <div class="setup_table_body">
              <div class="setup_table_body_left">
                <div class="setup_table_body_head">
                  <div v-for="item in couhead" :key="item.name">
                    {{ item.name }}
                  </div>
                </div>
                <div class="setup_table_body_content">
                  <div><input type="text" :value="coudata.SecretId" /></div>
                  <div><input type="text" :value="coudata.SecretKey" /></div>
                  <div><input type="text" :value="coudata.region" /></div>
                  <div><input type="text" :value="coudata.realmname" /></div>
                  <div><input type="text" :value="coudata.isopen" /></div>
                  <div><input type="text" :value="coudata.bucket" /></div>
                </div>
              </div>
              <div class="setup_table_body_right">
                <button>提交</button>
              </div>
            </div>
          </div>
        </div>
        <div class="setup_table redius2">
          <div class="setup_table_head">
            <div>网站设置</div>
          </div>
          <div class="setup_table_body_wrap">
            <div class="setup_table_body">
              <div class="setup_table_body_left">
                <div class="setup_table_body_head">
                  <div v-for="item in setuphead" :key="item.name">
                    {{ item.name }}
                  </div>
                </div>
                <div class="setup_table_body_content">
                  <div><input type="text" :value="setupdata.SecretId" /></div>
                  <div><input type="text" :value="setupdata.LOGO" /></div>
                </div>
              </div>
              <div class="setup_table_body_right">
                <button>提交</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue";
import { reactive } from "vue";

// 公众号设置表头数据
const accountHead = reactive([
  { name: "公众号名称" },
  { name: "Appid" },
  { name: "AppScret" },
  { name: "微信支付微商号" },
  { name: "微信支付APiv2密钥" },
  { name: "微信支付APiv3密钥" },
  { name: "公众二维码" },
]);

// 公众号设置数据
const accountSetuo = reactive({
  accountNam: "1",
  appId: "1",
  AppScret: "1",
  Merchant: "1",
  Paymentkey1: "1",
  Paymentkey1: "1",
  accountinmg: require("../assets/img/1.png"),
});

// cou云存储表头数据
const couhead = reactive([
  { name: "SecretId" },
  { name: "SecretKey" },
  { name: "region" },
  { name: "访问域名" },
  { name: "是否开启" },
  { name: "bucket" },
]);

// cou云存储数据
const coudata = reactive({
  SecretId: "1",
  SecretKey: "1",
  region: "1",
  realmname: "1",
  isopen: false,
  bucket: "1",
});

// 网站设置表头
const setuphead = reactive([{ name: "程序名称" }, { name: "网站LOGO" }]);

// 网站设置数据
const setupdata = reactive({
  ordername: "1",
  LOGO: "1",
});

// 网站设置数据
</script>

<style lang="scss" scoped>.system_main {
   width: calc(100vw - 200px);
   height: calc(100vh);
   font-size: 20px;
   font-weight: 50px;
  }
  .system_main_body {
   margin: 20px 20px;
  }
  .system_main_content{
   width: 100%;
   height: calc(100vh - 155px);
   display: flex;
   flex-direction: column;
   .setup_table {
    border: 1px solid #b5c3d178;
    flex: 1;
   }
   .setup_table_head {
    border-radius: 10px 10px 0px 0px;
    height: 40px;
    line-height: 40px;
    border-bottom: 1px solid #b5c3d178;
    box-shadow: 0 4px 4px 0 #bababa21;
    display: flex;
    color: #000;
    font-size: 20px;
    cursor: pointer;
    user-select: none;
    div {
     width: 11.111%;
     text-align: center;
     font-size: 15px;
     font-weight: lighter;
    }
   }
   .setup_table_body {
    width: 100%;
    height: calc((100vh - 364px) / 3);
    display: flex;
    text-align: center;
    font-size: 14px;
    font-weight: lighter;
    color: #585858;
   }
   .setup_table_body_left{
    width: 87.5%;
    .setup_table_body_head{
     height: 40px;
     display: flex;
     align-items: center;
     div{
      width: 12.5%;
     }
    }
    .setup_table_body_content{
     display: flex;
     align-items: center;
     div{
      width: 12.5%;
      display: flex;
      justify-content: flex-end;
     }
     input{
      border-style: none;
      outline: none;
     }
     img{
      width: 50px;
      height: 50px;
      background-size: 100%;
      background-repeat: no-repeat;
      margin: auto;
     }
    }
   }
   .setup_table_body_right{
    flex: 1;
    display: flex;
    align-items: flex-end;
    button{
     width: 50px;
     height: 30px;
     background-color: #188CFF;
     color: #fff;
     border-style: none;
     border-radius: 10px;
     font-size: 15px;
     cursor: pointer;
    user-select: none;
    }
   }
  }
  // 更改表格圆角样式
  .redius1{
    border-radius: 10px 10px 0px 0px;
    margin-top: 20px;
  }
  .redius2{
    border-radius: 0px 0px 10px 10px;
  }

  // 去除表格下边框
  .dislodgeborder{
    border-bottom: none;
  }
</style>
