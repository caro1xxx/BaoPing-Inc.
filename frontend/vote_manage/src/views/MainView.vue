<template>
  <div class="main">
    <router-view />
    <Loading v-show="$store.state.loadingState" />
  </div>
</template>

<script setup>
import Loading from "@/components/Loading.vue";
import { useStore } from "vuex";
const $store = useStore();
</script>

<style lang="scss" scoped>
.main {
  position: relative;
}
</style>
