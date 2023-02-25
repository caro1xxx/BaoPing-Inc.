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
    <!-- <Loading v-show="$store.state.loadingState" /> -->
  </div>
</template>

<script setup>
import MainView from "./views/MainView.vue";
import NavBar from "./components/NavBar.vue";
import Message from "./components/Message.vue";
import EditPopup from "./components/EditPopup.vue";
import SubNavBar from "./components/SubNavBar.vue";
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
