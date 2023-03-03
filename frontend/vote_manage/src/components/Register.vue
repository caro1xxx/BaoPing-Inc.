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
      <div
        @click="sendCode"
        :style="{
          cursor: !userInfo.isSendCodeState ? 'pointer' : 'not-allowed',
          backgroundColor: !userInfo.isSendCodeState ? '#2379fb' : '#cecece',
        }"
      >
        {{ userInfo.sendCodeContent }}
      </div>
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
      <input
        :checked="avatorList.isRemember"
        type="radio"
        @click="onClickRadio"
      />
      <div>记住我</div>
    </div>
    <button class="register_child_btn" @click="checkForm">注册并登录</button>
  </div>
</template>

<script setup>
import { reactive, onMounted, onBeforeUnmount } from "vue";
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
  { id: 1, img: require("../assets/img/avator/1.png"), select: false },
  { id: 2, img: require("../assets/img/avator/2.png"), select: false },
  { id: 3, img: require("../assets/img/avator/3.png"), select: false },
  { id: 4, img: require("../assets/img/avator/4.png"), select: false },
  { id: 5, img: require("../assets/img/avator/5.png"), select: false },
  { id: 6, img: require("../assets/img/avator/6.png"), select: false },
  { id: 7, img: require("../assets/img/avator/7.png"), select: false },
  { id: 8, img: require("../assets/img/avator/8.png"), select: false },
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
  isSendCodeState: false,
  sendCodeContent: "发送验证码",
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
  if (userInfo.sendCodeContent !== "发送验证码") return;
  let validator = new Validator();
  validator.add(userInfo.email, "isNonEmpty", "输入邮箱");
  validator.add(userInfo.email, "checkEmailFormat", "邮箱格式错误");
  let result = validator.start();
  if (result) {
    $store.dispatch("GlobalMessageActions", result);
    return;
  }
  sendSucess();
  let codeResult = await fether("/sendemailcode/", "post", {
    email: userInfo.email,
  });
  if (codeResult.code === 200) {
    await $store.dispatch("GlobalMessageActions", "发送成功");
  } else {
    await $store.dispatch("GlobalMessageActions", codeResult.msg);
  }
};

// 验证码发送成功 禁止点击发送验证码按钮
const sendSucess = () => {
  userInfo.isSendCodeState = true;
  userInfo.sendCodeContent = 60;
  let timer = setInterval(() => {
    if (userInfo.sendCodeContent <= 1) {
      userInfo.sendCodeContent = "发送验证码";
      clearInterval(timer);
      userInfo.isSendCodeState = false;
    } else {
      userInfo.sendCodeContent -= 1;
    }
  }, 1000);
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

// 登录成功
const loginSuccess = () => {
  $store.dispatch("authActions", true);
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
