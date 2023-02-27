<template>
  <div class="register"></div>
  <div class="register_mask">
    <div class="register_mask_body">
      <img
        src="../assets/img/31.png"
        @click="closeAuth"
        class="register_mask_close"
        alt=""
      />
      <div class="register_mask_body_body">
        <div
          class="register_mask_body_login"
          :style="{ borderBottom: authFlag[0] ? '3px solid #2379fb' : '' }"
          @click="() => changeAuth('login')"
        >
          账号登录
        </div>
        <div
          class="register_mask_body_login"
          :style="{ borderBottom: authFlag[1] ? '3px solid #2379fb' : '' }"
          @click="() => changeAuth('register')"
        >
          注册账号
        </div>
        <div
          class="register_mask_body_login"
          :style="{ borderBottom: authFlag[2] ? '3px solid #2379fb' : '' }"
          @click="() => changeAuth('lost')"
        >
          找回密码
        </div>
      </div>
      <Login v-if="authFlag[0]" />
      <Register v-if="authFlag[1]" />
      <ForgetPwd v-if="authFlag[2]" />
    </div>
  </div>
</template>

<script setup>
import Register from "@/components/Register.vue";
import Login from "@/components/Login.vue";
import ForgetPwd from "@/components/ForgetPwd.vue";
import { ref } from "vue";
import { useRouter } from "vue-router";

// 标志是否点击登录
const authFlag = ref([true, false, false]);

const router = useRouter();

// 改变注册或登录或找回密码
const changeAuth = (flag) => {
  if (flag === "login") {
    authFlag.value[0] = true;
    authFlag.value[1] = false;
    authFlag.value[2] = false;
  } else if (flag === "lost") {
    authFlag.value[2] = true;
    authFlag.value[0] = false;
    authFlag.value[1] = false;
  } else {
    authFlag.value[1] = true;
    authFlag.value[0] = false;
    authFlag.value[2] = false;
  }
};

// 关闭
const closeAuth = () => {
  router.push("/");
};
</script>

<style lang="scss" scoped>
.register {
  /* width: calc(100vw - 150px - 400px);
  height: calc(100vh);
  background-color: #fff; */
}
.register_mask {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 10;
  background-color: #00000074;
  display: flex;
  justify-content: center;
  align-items: center;
}
.register_mask_body {
  width: 400px;
  background-color: white;
  border-radius: 3px;
  position: relative;
}
.register_mask_body_login {
  margin: 20px 20px;
  font-size: 14px;
  text-align: center;
  line-height: 30px;
  cursor: pointer;
}
.register_mask_body_body {
  display: flex;
}
.register_mask_close {
  position: absolute;
  left: 420px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
</style>
