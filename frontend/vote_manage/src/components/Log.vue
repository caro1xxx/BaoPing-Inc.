<template>
  <div class="log">
    <div class="login_body_title">操作日志</div>
    <div class="log_body">
      <div v-for="item in logs" class="log_item">
        <div>{{ item.who }}</div>
        <div style="color: #2460e5">{{ item.action }}</div>
        <div>了{{ item.target }}</div>
        <div style="display: flex; flex-flow: row-reverse; color: #aaa">
          {{ parseStampTime(item.create_time) }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { fether } from "@/utils/fether";
import jsCookie from "js-cookie";
import { reactive } from "vue";
import { useStore } from "vuex";
import { parseStampTime } from "../utils/stampTime";
const $store = new useStore();

const logs = reactive([]);

const getLogs = async () => {
  let result = await fether(`/logs/?token=${jsCookie.get("token")}`);
  if (result.code === 200) {
    let JSONResult = JSON.parse(result.data);
    JSONResult.forEach((item) => {
      logs.push({ ...item.fields });
    });
  } else {
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
};

getLogs();
</script>

<style lang="scss" scoped>
.log {
  background-color: rgb(255, 255, 255);
  position: absolute;
  right: 0;
  width: calc(20vw);
  bottom: 0;
  top: 0;
  z-index: 4;
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 10px 0 rgba(0, 0, 0, 0.19);
  animation: 0.5s linear show;
  cursor: pointer;
  user-select: none;
}
.log_body {
  margin: 10px;
  height: calc(100vh - 50px);
  overflow: scroll;
}
.log_body::-webkit-scrollbar {
  display: none;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}
.login_body_title {
  font-weight: 15px;
  font-weight: bold;
  margin: 10px;
}
@keyframes show {
  from {
    right: calc(-20vw);
  }
  to {
    right: 0px;
  }
}
.log_item {
  height: 40px;
  div {
    display: inline-block;
    font-size: 10px;
  }
}
</style>
