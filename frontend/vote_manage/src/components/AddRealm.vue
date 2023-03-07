<template>
  <div class="body">
    <div class="body_content">
      <div class="body_content_head">新增</div>
      <div class="body_content_body">
        <div class="body_content_item">
          <label>域名</label>
          <el-input v-model="realmAddData.domain_name" placeholder="请输入" />
        </div>
        <div class="body_content_item">
          <label>有效期</label>
          <el-date-picker
            v-model="realmAddData.expire_time"
            type="datetime"
            placeholder="请选择时间"
            format="YYYY/MM/DD HH:mm:ss"
          />
        </div>
        <div class="body_content_button">
          <button class="body_content_button_item1" @click="closePopup">
            取消
          </button>
          <button class="body_content_button_item2" @click="sureRealmData">
            确认
          </button>
        </div>
      </div>
      <img
        @click="closePopup"
        class="body_content_close"
        src="../assets/img/31.png"
        alt=""
      />
    </div>
  </div>
</template>

<script setup>
import { reactive } from "vue";
import { useStore } from "vuex";
import { fether } from "@/utils/fether";
import Cookies from "js-cookie";
const $store = new useStore();
const closePopup = () => {
  $store.commit("changeRealmStatus");
};

// 新增域名数据
const realmAddData = reactive({
  domain_name: "",
  expire_time: "",
});

// 点击确认按钮
const sureRealmData = async () => {
  realmAddData.expire_time =
    new Date(realmAddData.expire_time).getTime() / 1000;
  //开启加载loading
  await $store.dispatch("NoticifyActions", true);
  // 判断值是否输入
  if (!realmAddData.domain_name) {
    await $store.dispatch("GlobalMessageActions", "域名未输入");
  } else if (!realmAddData.expire_time) {
    await $store.dispatch("GlobalMessageActions", "域名有效期未输入");
  } else {
    let result = await fether(`/domain/`, `post`, {
      domain: realmAddData.domain_name,
      expire_time: Math.floor(realmAddData.expire_time / 1000),
      token: Cookies.get("token"),
    });
    if (result.code === 200) {
      // 向本地新增数据
      $store.commit("preserveRealmData", realmAddData);
      await $store.dispatch("GlobalMessageActions", result.msg);
    } else {
      //   请求发送错误
      await $store.dispatch("refreshErroActions");
      await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
    }
    // 关闭加载loading
    $store.commit("noticifyLoading", false);
    $store.commit("changeRealmStatus");
  }
};
</script>

<style lang="scss" scoped>
.body {
  position: absolute;
  top: 0px;
  right: 0;
  left: 0;
  bottom: 0;
  background-color: #00000074;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 5;
}
.body_content {
  width: calc(25vw - 40px);
  height: calc(50vh - 40px);
  background-color: white;
  border-radius: 3px;
  padding: 20px;
  position: relative;
}
.body_content_head {
  font-size: 15px;
  cursor: pointer;
  border-bottom: 2px solid #d4d4d474;
  margin-bottom: 10px;
}
.body_content_close {
  position: absolute;
  right: -60px;
  top: 0px;
  width: 30px;
  height: 30px;
  cursor: pointer;
}
.body_content_item {
  margin-bottom: 10px;
  label {
    display: block;
    font-size: 13px;
    margin-bottom: 5px;
  }
  .el-input {
    width: 100%;
  }
}
.body_content_button {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  position: absolute;
  bottom: 20px;
  left: 0px;
  button {
    margin-right: 20px;
    width: 20%;
    height: 100%;
    border: 1px solid #dcdfe6;
    outline: none;
    border-radius: 5px;
    padding: 5px 0px;
  }
  .body_content_button_item1 {
    border: 1px solid #dcdfe6;
  }
  .body_content_button_item2 {
    background-color: #409eff;
    color: #ffffff;
  }
}
</style>
