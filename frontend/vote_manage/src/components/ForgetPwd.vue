<template>
  <div class="register_mask_body_input">
    <input
      type="text"
      placeholder="注册账号时的邮箱"
      v-model="userInputInfo.email"
      class="register_mask_body_inp"
    />
    <input
      type="password"
      placeholder="新密码(长度8-16)"
      v-model="userInputInfo.password"
      class="register_mask_body_inp"
      maxlength="16"
    />
    <div class="register_sendbody">
      <input
        v-model="userInputInfo.code"
        type="text"
        maxlength="6"
        placeholder="邮箱验证码"
        class="register_mask_body_inp"
        style="width: 70%"
      />
      <div
        @click="sendCode"
        class="btn"
        :style="{
          cursor: !userInputInfo.isSendCodeState ? 'pointer' : 'not-allowed',
          backgroundColor: !userInputInfo.isSendCodeState
            ? '#2379fb'
            : '#cecece',
        }"
      >
        {{ userInputInfo.sendCodeContent }}
      </div>
    </div>
    <div class="register_child_radio">
      <input
        :checked="userInputInfo.isRemember"
        type="radio"
        @click="onClickRadio"
      />
      <div>记住我</div>
    </div>
    <button class="register_child_btn" @click="checkForm">确定并登录</button>
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
const userInputInfo = ref({
  password: "",
  isRemember: false,
  email: "",
  code: "",
  isSendCodeState: false,
  sendCodeContent: "发送验证码",
});

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
  validator.add(userInputInfo.value.email, "isNonEmpty", "输入邮箱");
  validator.add(userInputInfo.value.email, "checkEmailFormat", "邮箱格式错误");
  validator.add(userInputInfo.value.password, "isNonEmpty", "输入密码");
  validator.add(userInputInfo.value.password, "minLength", "长度需大于8", 8);
  validator.add(userInputInfo.value.code, "isNonEmpty", "输入验证码");
  let result = validator.start();
  if (!result) authUser(userInputInfo);
  else $store.dispatch("GlobalMessageActions", result);
};

// 是否记住记住登录
const rememberUser = (flag, value) => {
  console.log(flag, value);
  if (flag) Cookies.set("token", value, { expires: 7 });
  else Cookies.set("token", value);
};

// 验证
const authUser = async (input) => {
  const result = await fether("/setnewpassword/", "post", {
    email: userInputInfo.value.email,
    new_pwd: userInputInfo.value.password,
    code: userInputInfo.value.code,
  });
  // 更新通知
  await $store.dispatch(
    "GlobalMessageActions",
    result.code === 200 ? "登录成功" : result.msg
  );
  console.log(result.code);
  if (result.code === 200) {
    // 保存用户信息
    await $store.dispatch("UserActions", JSON.parse(result.data)[0].fields);
    rememberUser(
      userInputInfo.value.isRemember,
      JSON.parse(result.data)[0].fields.token
    );
    loginSuccess();
  }
};

// 发送邮件
const sendCode = async () => {
  if (userInputInfo.value.sendCodeContent !== "发送验证码") return;
  let validator = new Validator();
  validator.add(userInputInfo.value.email, "isNonEmpty", "输入邮箱");
  validator.add(userInputInfo.value.email, "checkEmailFormat", "邮箱格式错误");
  let result = validator.start();
  if (result) {
    $store.dispatch("GlobalMessageActions", result);
    return;
  }
  sendSucess();
  let codeResult = await fether("/forgetpasswordsendemail/", "post", {
    email: userInputInfo.value.email,
  });
  if (codeResult.code === 200) {
    await $store.dispatch("GlobalMessageActions", "发送成功");
  } else {
    await $store.dispatch("GlobalMessageActions", codeResult.msg);
  }
};

// 验证码发送成功 禁止点击发送验证码按钮
const sendSucess = () => {
  userInputInfo.value.isSendCodeState = true;
  userInputInfo.value.sendCodeContent = 60;
  let timer = setInterval(() => {
    if (userInputInfo.value.sendCodeContent <= 1) {
      userInputInfo.value.sendCodeContent = "发送验证码";
      clearInterval(timer);
      userInputInfo.value.isSendCodeState = false;
    } else {
      userInputInfo.value.sendCodeContent -= 1;
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
.register_mask_body_inp {
  width: 100%;
  display: block;
  outline: none;
  border: none;
  border-bottom: 1px solid #efefef;
  margin-bottom: 20px;
  line-height: 40px;
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
.btn {
  user-select: none;
}
</style>
