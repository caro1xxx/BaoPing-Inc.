<template>
  <div class="star">
    <div class="star_body">今日之星:{{ $store.state.settings[58].value }}</div>
  </div>
</template>

<script setup>
import { useStore } from "vuex";
const $store = useStore();
</script>

<style lang="scss" scoped>
.star {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background-color: #00000074;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  z-index: 10;
}
.star_body {
  height: 50%;
  width: 70%;
  background-color: white;
}
</style>
