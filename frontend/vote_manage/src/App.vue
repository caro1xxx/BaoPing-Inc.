<template>
  <div style="display: flex; position: relative">
    <NavBar />
    <router-view />
    <Message v-if="$store.state.globalMessage !== ''" />
    <Loading v-show="$store.state.loadingState" />
    <EditPopup
      v-if="$store.state.editPopProps.name !== ''"
      :data="$store.state.editPopProps"
    />
  </div>
</template>

<script setup>
import NavBar from "./components/NavBar.vue";
import Message from "./components/Message.vue";
import Loading from "./components/Loading.vue";
import EditPopup from "./components/EditPopup.vue";
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
