<template>
  <div style="display: flex">
    <NavBar />
    <router-view />
    <SiderBar />
    <Message v-if="$store.state.globalMessage !== ''" />
  </div>
</template>

<script setup>
import NavBar from "./components/NavBar.vue";
import SiderBar from "./components/SiderBar.vue";
import Message from "./components/Message.vue";
import { useStore } from "vuex";
const $store = useStore();

</script>

<style lang="scss">
@font-face {
  font-family: Memo;
  src: url("./assets/font/agave\ regular\ Nerd\ Font\ Complete\ Mono.ttf");
}

* {
  font-family: Memo;
}
</style>
