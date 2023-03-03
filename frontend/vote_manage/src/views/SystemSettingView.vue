<template>
  <div class="home">
    <Search />
    <div class="home_title"><span>系统设置</span></div>
    <div class="systemseting-content">
      <div class="systemseting-content-left">
        <div class="grid">
          <div>
            <div class="systemthing-content-title">公众号名称</div>
            <div>
              <input
                type="text"
                class="smalllinput"
                v-model="officialdata.data.officialcount_name"
              />
            </div>
          </div>
          <div>
            <div class="systemthing-content-title">Appid</div>
            <div>
              <input
                type="text"
                class="smalllinput"
                v-model="officialdata.data.app_id"
              />
            </div>
          </div>
          <div>
            <div class="systemthing-content-title">region</div>
            <div>
              <input
                type="text"
                class="smalllinput"
                v-model="officialdata.data.region"
              />
            </div>
          </div>
          <div>
            <div class="systemthing-content-title">微信支付商户号</div>
            <div>
              <input
                type="text"
                class="smalllinput"
                v-model="officialdata.data.wxpay_pos_id"
              />
            </div>
          </div>
        </div>
        <div class="grid1">
          <div class="span-col-2">
            <div class="systemthing-content-title">微信支付APIv2密钥</div>
            <div>
              <input
                type="text"
                class="biginput"
                v-model="officialdata.data.wxpay_apiv2_secret_key"
              />
            </div>
          </div>
          <div class="span-col-2">
            <div class="systemthing-content-title">微信支付APIv3密钥</div>
            <div>
              <input
                type="text"
                class="biginput"
                v-model="officialdata.data.wxpay_apiv3_secret_key"
              />
            </div>
          </div>
          <div>
            <button @click="preserve()">保存</button>
          </div>
        </div>
      </div>
      <div class="systemseting-content-right">
        <img class="images" src="../assets/img/1.png" alt="" />
      </div>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue";
import { fether } from "@/utils/fether";
import { reactive } from "vue";
import { useStore } from "vuex";
import Cookies from "js-cookie";
const $store = new useStore();

// 公众号数据
const officialdata = reactive({
  data: {
    app_id: "",
    officialcount_name: "",
    region: "",
    wx_pay_apiv2_secret_key: "",
    wxpay_apiv3_secret_key: "",
    wxpay_pos_id: "",
  },
});

// 获取公众号信息
const getofficial = async () => {
  // 开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/officialaccount/?token=${Cookies.get("token")}`);
  //
  // let result = await fether(
  //   `/officialaccount/?token=h0iLxzKyDbZCAJg9m3Yd8BWRrsHQtEvG`
  // )
  if (result.code === 200) {
    officialdata.data = { ...result.data };
    // officialdata = {...result.data}
    // officialdata.push({ ...result.data, isMove: false });
  } else {
    // 请求发送错误
    await $store.dispatch("refreshErroActions");
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
};

// 保存修改数据
const preserve = async () => {
  // 开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(
    `/officialaccount/`,
    `put`,
    {
      token: Cookies.get("token"),
      data: {
        app_id: officialdata.data.app_id,
        officialcount_name: officialdata.data.officialcount_name,
        region: officialdata.data.region,
        wxpay_apiv2_secret_key: officialdata.data.wxpay_apiv2_secret_key,
        wxpay_apiv3_secret_key: officialdata.data.wxpay_apiv3_secret_key,
        wxpay_pos_id: officialdata.data.wxpay_pos_id,
      },
      token: Cookies.get("token"),
      // token: 'h0iLxzKyDbZCAJg9m3Yd8BWRrsHQtEvG'
    },
    $store.state.userInfo.name,
    "系统设置"
  );
  await $store.dispatch("GlobalMessageActions", result.msg);
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
};
getofficial();
</script>

<style lang="scss" scoped>
.home {
  width: calc(100vw - 250px - 40px);
  height: calc(100vh - 40px);
  font-size: 20px;
  padding: 20px;
}
.home_title {
  font-size: 20px;
  font-weight: bold;
  margin: 20px 0px;
  span {
    cursor: pointer;
    user-select: none;
  }
}
.systemseting-content {
  height: calc(100vh - 148px);
  display: flex;
}
.systemseting-content-left {
  flex: 1;
  height: 148px;
}
.systemthing-content-title {
  height: 30px;
  line-height: 30px;
  color: #000;
  font-size: 12px;
}
.systemseting-content-right {
  width: 142px;
  height: 148px;
}
.images {
  width: 142px;
  height: 148px;
  background-size: 100%;
  background-repeat: no-repeat;
}
.grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 10px;
  grid-template-rows: 74px;
}
.grid1 {
  margin-top: 10px;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-gap: 10px;
  grid-template-rows: 74px;
}
.span-col-2 {
  grid-column: span 2 / auto;
}
input {
  border: 1px solid #e9e9e9;
  outline: 1px solid #e9e9e9;
  border-radius: 3px;
  margin-top: 15px;
  height: 23px;
  box-shadow: 0 4px 4px 0 rgba(236, 236, 236, 0.2),
    0 6px 20px 0 rgba(236, 236, 236, 0.2);
}
.smalllinput {
  width: 70%;
}
.biginput {
  width: 75%;
}
button {
  width: 120px;
  height: 29px;
  margin-top: 45px;
  background-color: #2460e5;
  color: #fff;
  border: 0px;
  border-radius: 3px;
  margin-right: 244px;
  user-select: none;
  cursor: pointer;
}
</style>
