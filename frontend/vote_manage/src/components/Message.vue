<template>
  <div class="message">
    <img src="../assets/img/14.png" width="20" height="20" alt="" />
    <div>{{ store.state.globalMessage }}</div>
  </div>
</template>

<script setup>
import store from "@/store";
</script>

<style lang="scss" scoped>
.message {
  font-size: 10px;
  position: absolute;
  color: #188cff;
  top: 30px;
  left: 45%;
  right: 45%;
  background-color: white;
  z-index: 20;
  box-shadow: 0 4px 8px 0 rgba(120, 120, 120, 0.2),
    0 6px 20px 0 rgba(143, 143, 143, 0.19);
  border-radius: 5px;
  height: 30px;
  line-height: 30px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding: 0px 10px;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  animation: showMessgae linear 0.5;
}
</style>
