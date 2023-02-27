<template>
  <div class="register_mask_body_input">
    <input
      v-model="userInfo.name"
      maxlength="4"
      type="text"
      placeholder="真实姓名"
      class="register_mask_body_inp"
    />
    <input
      v-model="userInfo.username"
      type="text"
      maxlength="8"
      placeholder="用户名(长度5-8)"
      class="register_mask_body_inp"
    />
    <input
      v-model="userInfo.password"
      type="password"
      maxlength="16"
      placeholder="密码(长度8-16)"
      class="register_mask_body_inp"
    />
    <input
      v-model="userInfo.rePassword"
      type="password"
      maxlength="16"
      placeholder="重复密码"
      class="register_mask_body_inp"
    />
    <input
      v-model="userInfo.email"
      type="text"
      placeholder="邮箱"
      class="register_mask_body_inp"
    />
    <div class="register_sendbody">
      <input
        v-model="userInfo.code"
        type="text"
        maxlength="6"
        placeholder="邮箱验证码"
        class="register_mask_body_inp"
        style="width: 70%"
      />
      <div @click="sendCode">发送验证码</div>
    </div>
    <div class="register_selecttitle">选择头像</div>
    <div class="register_selectavator">
      <div
        v-for="item in avatorList"
        class="register_selectavator_item"
        :key="item.id"
      >
        <img
          @click="() => selectedAvator(item.id)"
          :src="item.img"
          alt=""
          width="30"
          height="30"
        />
        <img
          class="register_selectavator_item_select"
          src="../assets/img/select.png"
          alt=""
          v-show="item.select"
        />
      </div>
    </div>
    <div class="register_child_radio">
      <input type="radio" @click="onClickRadio" />
      <div>记住我</div>
    </div>
    <button class="register_child_btn" @click="checkForm">注册并登录</button>
  </div>
</template>

<script setup>
import { reactive } from "vue";
import { Validator } from "@/utils/validator";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { fether } from "@/utils/fether";
import { HOST } from "@/ENV";
import Cookies from "js-cookie";

const router = useRouter();

const $store = useStore();
// 头像列表
const avatorList = reactive([
  { id: 22, img: require("../assets/img/22.png"), select: false },
  { id: 23, img: require("../assets/img/23.png"), select: false },
  { id: 24, img: require("../assets/img/24.png"), select: false },
  { id: 25, img: require("../assets/img/25.png"), select: false },
  { id: 26, img: require("../assets/img/26.png"), select: false },
  { id: 27, img: require("../assets/img/27.png"), select: false },
  { id: 28, img: require("../assets/img/28.png"), select: false },
  { id: 29, img: require("../assets/img/29.png"), select: false },
]);

// 点击记住
const onClickRadio = () => {
  avatorList.isRemember = !avatorList.isRemember;
};

// 用户输入
const userInfo = reactive({
  name: "",
  username: "",
  password: "",
  rePassword: "",
  email: "",
  code: "",
  avator: "",
  isRemember: false,
});

// 选择头像
const selectedAvator = (id) => {
  avatorList.forEach((item, index) => {
    if (item.id === id) {
      avatorList[index].select = true;
      userInfo.avator = id;
    } else avatorList[index].select = false;
  });
};

// 校验输入
const checkForm = () => {
  let validator = new Validator();
  validator.add(userInfo.name, "isNonEmpty", "输入姓名");
  validator.add(userInfo.name, "minLength", "长度需大于1", 2);
  validator.add(userInfo.username, "isNonEmpty", "输入用户名");
  validator.add(userInfo.username, "minLength", "长度需大于5", 5);
  validator.add(userInfo.password, "isNonEmpty", "输入密码");
  validator.add(userInfo.password, "minLength", "长度需大于8", 8);
  validator.add(userInfo.rePassword, "isNonEmpty", "重复密码");
  validator.add(userInfo.rePassword, "minLength", "长度需大于8", 8);
  validator.add(
    [userInfo.rePassword, userInfo.password],
    "comparePsd",
    "密码不一致"
  );
  validator.add(userInfo.email, "isNonEmpty", "输入邮箱");
  validator.add(userInfo.email, "checkEmailFormat", "邮箱格式错误");
  validator.add(userInfo.code, "isNonEmpty", "输入验证码");
  validator.add(userInfo.code, "codeLength", "验证码长度等于4");
  validator.add(userInfo.avator, "isNonEmpty", "选择头像");
  let result = validator.start();
  $store.dispatch("GlobalMessageActions", result);
  if (!result) register();
  else $store.dispatch("GlobalMessageActions", result);
};

// 是否记住记住登录
const rememberUser = (flag, value) => {
  if (flag) Cookies.set("token", value, { expires: 7 });
  else Cookies.set("token", value);
};

// 注册
const register = () => {
  let form = new FormData();
  form.append("name", userInfo.name);
  form.append("username", userInfo.username);
  fetch(`${HOST}/register/`, {
    method: "post",
    body: JSON.stringify({
      data: {
        name: userInfo.name,
        username: userInfo.username,
        pwd: userInfo.password,
        email: userInfo.email,
        email_code: userInfo.code,
        avator: userInfo.avator,
      },
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.code === 200) {
        // 保存用户信息
        $store.dispatch("UserActions", JSON.parse(data.data)[0].fields);
        rememberUser(
          userInfo.isRemember,
          JSON.parse(data.data)[0].fields.token
        );
        loginSuccess();
      }
    });
};

// 请求验证码
const sendCode = async () => {
  let validator = new Validator();
  validator.add(userInfo.email, "isNonEmpty", "输入邮箱");
  validator.add(userInfo.email, "checkEmailFormat", "邮箱格式错误");
  let result = validator.start();
  $store.dispatch("GlobalMessageActions", result);
  if (result) return;
  let codeResult = await fether("/sendemailcode/", "post", {
    email: userInfo.email,
  });
  let res = await $store.dispatch("GlobalMessageActions", codeResult.msg);
};

// 登录成功
const loginSuccess = () => {
  router.push("/");
};
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
.register_selecttitle {
  font-size: 10px;
  margin-bottom: 10px;
}
.register_selectavator {
  display: flex;
}
.register_selectavator_item {
  position: relative;
  margin-bottom: 10px;
  cursor: pointer;
}
.register_selectavator_item_select {
  position: absolute;
  z-index: 11;
  right: 5px;
  top: 5px;
}
.register_sendbody {
  display: flex;
  div {
    width: 25%;
    text-align: center;
    line-height: 42px;
    height: 42px;
    border-radius: 5px;
    background-color: #2379fb;
    color: white;
    font-size: 10px;
    cursor: pointer;
    margin-left: 5%;
  }
}
</style>
