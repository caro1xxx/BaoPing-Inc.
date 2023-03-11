<template>
  <div class="popup">
    <div class="popup_body">
      <img
        src="../assets/img/31.png"
        @click="closePopup"
        class="register_mask_close"
        alt=""
      />
      <div class="popup_body_margin">
        <label class="titles">姓名</label>
        <input
          type="text"
          placeholder="姓名"
          v-model="userEditInfo.name"
          class="register_mask_body_inp"
          maxlength="8"
        />
        <label class="titles">权限(0代表普通,1代表管理)</label>
        <input
          type="text"
          placeholder="权限"
          v-model="userEditInfo.auth"
          class="register_mask_body_inp"
          maxlength="8"
        />
        <label class="titles">是否可用(输入开或关)</label>
        <input
          type="text"
          placeholder="状态"
          v-model="userEditInfo.status"
          class="register_mask_body_inp"
          maxlength="8"
        />
        <button class="register_child_btn" @click="checkForm">保存</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from "vue";
import { useStore } from "vuex";
import { Validator } from "@/utils/validator";
const $store = new useStore();
const props = defineProps({
  data: {
    name: String,
    state: Number,
    password: String,
    auth: Number,
    username: String,
  },
});
const userEditInfo = reactive({
  name: props.data.name,
  status: props.data.status ? "开" : "关",
  pwd: props.data.pwd,
  auth: props.data.auth,
  username: props.data.username,
});

const closePopup = () => {
  $store.state.editPopProps.name = "";
};

// 检查
const checkForm = async () => {
  let validator = new Validator();
  validator.add(userEditInfo.name, "isNonEmpty", "输入账号");
  validator.add(userEditInfo.status, "isNonEmpty", "输入状态");
  validator.add(userEditInfo.auth, "isNonEmpty", "请输入权限");
  validator.add(userEditInfo.name, "maxLength", "姓名最大长度为4", 4);
  validator.add(userEditInfo.name, "minLength", "姓名最小长度为2", 2);
  validator.add(userEditInfo.auth, "isNumber", "输入错误");
  let result = validator.start();
  if (!result) {
    $store.dispatch("editUserActions", { ...userEditInfo });
    $store.dispatch("handleUserEditActions", 1);
  } else {
    $store.dispatch("GlobalMessageActions", result);
  }
};
</script>

<style lang="scss" scoped>
.popup {
  background-color: #00000074;
  position: absolute;
  top: 0%;
  bottom: 0%;
  left: 0%;
  right: 0%;
  z-index: 5;
  display: flex;
  align-items: center;
  justify-content: center;
}
.popup_body {
  position: relative;
  width: 300px;
  background-color: white;
  border-radius: 3px;
}
.popup_body_margin {
  margin: 20px;
  .titles {
    font-size: 15px;
  }
}
.register_mask_body_inp {
  width: 260px;
  display: block;
  outline: none;
  border: none;
  border-bottom: 1px solid #efefef;
  margin-bottom: 20px;
  line-height: 40px;
}
.register_child_btn {
  background-color: #2379fb;
  width: 260px;
  height: 40px;
  outline: none;
  border: none;
  color: white;
  border-radius: 5px;
  box-shadow: none;
  cursor: pointer;
}
.register_mask_close {
  position: absolute;
  left: 320px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
</style>
