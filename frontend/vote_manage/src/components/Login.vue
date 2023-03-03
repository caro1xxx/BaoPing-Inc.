<template>
  <div class="register_mask_body_input">
    <input
      type="text"
      autofocus
      placeholder="账号"
      v-model="userInputInfo.username"
      class="register_mask_body_inp"
      maxlength="8"
    />
    <input
      type="password"
      placeholder="密码"
      v-model="userInputInfo.password"
      class="register_mask_body_inp"
      maxlength="16"
    />
    <div class="register_child_radio">
      <input
        :checked="userInputInfo.isRemember"
        type="radio"
        @click="onClickRadio"
      />
      <div>记住我</div>
    </div>
    <button class="register_child_btn" @click="checkForm">登录</button>
  </div>
</template>

<script setup>
import { fether } from "@/utils/fether";
import { ref, onMounted, onBeforeUnmount } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { Validator } from "@/utils/validator";
import Cookies from "js-cookie";

// 用户输入信息
const userInputInfo = ref({ username: "", password: "", isRemember: false });

// vuex实例
const $store = new useStore();
const router = useRouter();

// 点击记住
const onClickRadio = () => {
  userInputInfo.value.isRemember = !userInputInfo.value.isRemember;
};

// 校验输入
const checkForm = () => {
  let validator = new Validator();
  validator.add(userInputInfo.value.username, "isNonEmpty", "输入账号");
  validator.add(userInputInfo.value.username, "minLength", "长度需大于5", 5);
  validator.add(userInputInfo.value.username, "isNonEmpty", "输入密码");
  validator.add(userInputInfo.value.password, "minLength", "长度需大于8", 8);
  let result = validator.start();
  if (!result) authUser(userInputInfo);
  else $store.dispatch("GlobalMessageActions", result);
};

// 是否记住记住登录
const rememberUser = (flag, target) => {
  if (flag) {
    Cookies.set("token", target.token, { expires: 7 });
    Cookies.set("username", target.username, { expires: 7 });
  } else {
    Cookies.set("token", target.token);
    Cookies.set("username", target.username);
  }
};

// 登录
const authUser = async (input) => {
  const result = await fether("/login/", "post", {
    username: input.value.username,
    pwd: input.value.password,
  });
  // 更新通知
  await $store.dispatch(
    "GlobalMessageActions",
    result.code === 200 ? "登录成功" : result.msg
  );
  if (result.code === 200) {
    // 保存用户信息
    await $store.dispatch("UserActions", JSON.parse(result.data)[0].fields);
    rememberUser(userInputInfo.value.isRemember, {
      token: JSON.parse(result.data)[0].fields.token,
      username: JSON.parse(result.data)[0].fields.username,
    });
    loginSuccess();
  }
};

// 登录成功
const loginSuccess = () => {
  $store.dispatch("authActions", true);
  router.push("/");
};

// enter
const keyDownEnter = (e) => {
  if (e.code !== "Enter") return;
  checkForm();
};

onMounted(() => {
  window.addEventListener("keypress", keyDownEnter);
});
onBeforeUnmount(() => {
  window.removeEventListener("keypress", keyDownEnter);
});
</script>

<style lang="scss" scoped>
.register_mask_body_input {
  margin: 0px 20px;
}
.register_mask_body_inp {
  width: 100%;
  display: block;
  outline: none;
  border: none;
  border-bottom: 1px solid #efefef;
  margin-bottom: 20px;
  line-height: 40px;
}
.register_child_btn {
  background-color: #2379fb;
  width: 100%;
  height: 40px;
  outline: none;
  border: none;
  color: white;
  border-radius: 5px;
  box-shadow: none;
  margin-bottom: 20px;
  cursor: pointer;
}
.register_child_radio {
  font-size: 10px;
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  position: relative;
  cursor: pointer;
  div {
    position: absolute;
    top: 1px;
    left: 20px;
  }
}
</style>
