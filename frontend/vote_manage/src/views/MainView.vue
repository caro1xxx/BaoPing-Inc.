<template>
  <div class="main">
    <router-view v-if="!freshFlag" />
    <Loading v-show="$store.state.loadingState" />
    <Refresh v-show="$store.state.errorRefresh" />
  </div>
</template>

<script setup>
import Loading from "@/components/Loading.vue";
import Refresh from "@/components/Refresh.vue";
import { ref, watch } from "vue";
import { useStore } from "vuex";
const $store = useStore();
const freshFlag = ref(false);

watch(
  () => $store.state.freshFlag,
  (newVal) => {
    freshFlag.value = true;
    setTimeout(() => {
      freshFlag.value = false;
    }, 1000);
  }
);
</script>

<style lang="scss" scoped>
.main {
  position: relative;
}
</style>
