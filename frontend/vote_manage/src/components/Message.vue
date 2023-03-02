<template>
  <div class="message">
    <div class="message_body">
      <svg
        t="1677319471758"
        class="icon"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="5994"
        width="20"
        height="20"
      >
        <path
          d="M224 960c-6.4 0-12.8 0-19.2-6.4-6.4-6.4-12.8-12.8-12.8-25.6V832c-70.4 0-128-57.6-128-128V256c0-70.4 57.6-128 128-128h640c70.4 0 128 57.6 128 128v454.4c0 38.4-12.8 70.4-44.8 96-25.6 25.6-64 32-102.4 25.6h-76.8l-512 128c6.4 0 0 0 0 0zM192 192c-38.4 0-64 25.6-64 64v448c0 38.4 25.6 64 64 64h32c19.2 0 32 12.8 32 32v89.6l473.6-121.6H819.2c25.6 0 38.4 0 51.2-12.8 12.8-12.8 19.2-25.6 19.2-44.8V256c0-38.4-25.6-64-64-64H192z"
          fill="#ffffff"
          p-id="5995"
        ></path>
      </svg>
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
