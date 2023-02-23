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
          :style="{ borderBottom: authFlag ? '3px solid #2379fb' : '' }"
          @click="() => changeAuth('login')"
        >
          账号登录
        </div>
        <div
          class="register_mask_body_login"
          :style="{ borderBottom: !authFlag ? '3px solid #2379fb' : '' }"
          @click="() => changeAuth('register')"
        >
          注册账号
        </div>
      </div>
      <Login v-if="authFlag" />
      <Register v-else />
    </div>
  </div>
</template>

<script setup>
import Register from "@/components/Register.vue";
import Login from "@/components/Login.vue";
import { ref } from "vue";
import { useRouter } from "vue-router";

// 标志是否点击登录
const authFlag = ref(true);

const router = useRouter();

// 改变注册或登录
const changeAuth = (flag) => {
  if (flag === "login") authFlag.value = true;
  else authFlag.value = false;
};

// 关闭
const closeAuth = () => {
  router.push("/");
};
</script>

<style lang="scss" scoped>
.register {
  width: calc(100vw - 150px - 400px);
  height: calc(100vh);
  background-color: #fff;
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
  width: calc(25vw);
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
  left: 370px;
  width: 20px;
  height: 20px;
  cursor: pointer;
}
</style>
