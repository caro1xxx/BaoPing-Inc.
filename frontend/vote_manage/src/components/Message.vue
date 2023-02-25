<template>
  <div class="message">
    <div class="message_body">
      <img src="../assets/img/14.png" width="20" height="20" alt="" />
      <div>{{ store.state.globalMessage }}</div>
    </div>
  </div>
</template>

<script setup>
import store from "@/store";
</script>

<style lang="scss" scoped>
.message {
  font-size: 10px;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  z-index: 20;
  background-color: #2460e5;
  text-align: center;
}
.message_body {
  display: inline;
  color: #fff;
  background-color: #2460e5;
  height: 30px;
  line-height: 30px;
  padding: 0px 10px;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  animation: showMessgae linear 0.5;
}
</style>
