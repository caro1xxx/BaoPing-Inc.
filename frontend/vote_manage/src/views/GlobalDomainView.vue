<!-- 全局域名 -->
<template>
  <div class="system_main">
    <div class="system_main_body">
      <Search />
      <div class="title_style">全局域名</div>
      <div class="setup_table">
        <div class="setup_table_head">
          <div>全局域名</div>
        </div>
        <div class="setup_table_body_wrap">
          <div class="setup_table_body">
            <div class="setup_table_body_left">
              <div class="setup_table_body_head">
                <div v-for="(item) in realmHead" :key="item.name">{{ item.name }}</div>
              </div>
              <div class="setup_table_body_content">
                <div><input type="text" :value="realmSetuo.homerealm"></div>
                <div><input type="text" :value="realmSetuo.listrealm"></div>
                <div><input type="text" :value="realmSetuo.sharerealm"></div>
                <div><input type="text" :value="realmSetuo.Merchant"></div>
                <div><input type="text" :value="realmSetuo.Paymentkey1"></div>
                <div><input type="text" :value="realmSetuo.Paymentkey2"></div>
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
</template>

<script setup>
import Search from "@/components/Search.vue";
import { reactive } from "vue";

// 公众号设置表头数据
const realmHead = reactive([
  {name: '首页域名'},
  {name: '列表域名'},
  {name: '分享域名'},
  {name: '支付域名'},
  {name: '授权域名'},
  {name: '扫码回调域名'},
])

// 公众号设置数据
const realmSetuo = reactive({
  homerealm: '1',
  listrealm: '1',
  sharerealm:'1',
  payrealm:'1',
  empowerrewalm: '1',
  returnrealm: '1',
})
</script>

<style lang="scss" scoped>
.system_main {
  width: calc(100vw - 200px);
  height: calc(100vh);
  font-size: 20px;
  font-weight: 50px;
}
.system_main_body {
  margin: 20px 20px;
}

.setup_table {
  border: 1px solid #b5c3d178;
  border-radius: 10px;
  margin-top: 20px;
}
.setup_table_head {
  border-radius: 10px 10px 0px 0px;
  height: 40px;
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
    line-height: 40px;
    font-size: 15px;
    font-weight: lighter;
  }
}
.setup_table_body {
  height: 200px;
  display: flex;
  text-align: center;
  font-size: 14px;
  font-weight: lighter;
  color: #585858;
  margin: 10px 0px;
}
.setup_table_body_left{
  flex: 1;
  .setup_table_body_head{
    height: 40px;
    display: flex;
    align-items: center;
    div{
      cursor: pointer;
      width: 14.28%;
    }
  }
  .setup_table_body_content{
    height: 80px;
    display: flex;
    align-items: center;
    div{
      width: 14.28%;
      display: flex;
      justify-content: flex-end;
    }
    input{
      border-style: none;
      outline: none;
      width: 80%;
    }
    img{
      width: 80px;
      height: 80px;
      background-size: 100%;
      background-repeat: no-repeat;
      margin: auto;
    }
  }
}
.setup_table_body_right{
  width: 200px;
  button{
    width: 50px;
    height: 30px;
    background-color: #188CFF;
    color: #fff;
    border-style: none;
    border-radius: 10px;
    margin-top: 130px;
    cursor: pointer;
    user-select: none;
  }
}
</style>
