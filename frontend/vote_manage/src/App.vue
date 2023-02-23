<template>
  <div style="display: flex">
    <NavBar />
    <router-view />
    <!-- <SiderBar /> -->
  </div>
</template>

<script setup>
import NavBar from "./components/NavBar.vue";
// import SiderBar from "./components/SiderBar.vue";
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
