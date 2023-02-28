<template>
  <div style="display: flex; position: relative">
    <NavBar />
    <SubNavBar />
    <MainView />
    <Message v-if="$store.state.globalMessage !== ''" />
    <EditPopup
      v-if="$store.state.editPopProps.name !== ''"
      :data="$store.state.editPopProps"
    />
    <AuthView v-if="!$store.state.isAuth" />
    <EditActivity />
    <!-- <Loading v-show="$store.state.loadingState" /> -->
  </div>
</template>

<script setup>
import MainView from "./views/MainView.vue";
import NavBar from "./components/NavBar.vue";
import Message from "./components/Message.vue";
import EditPopup from "./components/EditPopup.vue";
import SubNavBar from "./components/SubNavBar.vue";
import AuthView from "./views/AuthView.vue";
import EditActivity from "./components/EditActivity.vue";
import { useStore } from "vuex";
import Cookies from "js-cookie";
import { ref } from "vue";
const $store = useStore();
if (Cookies.get("token") === undefined) {
  $store.dispatch("authActions", false);
}
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
