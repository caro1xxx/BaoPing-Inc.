<template>
  <router-view />
</template>

<script setup>
import { fether } from "./utils/fether";
import { useStore } from "vuex";
const $store = new useStore();
const getInitSetting = async () => {
  let result = await fether("/settings/");
  const map1 = new Map();
  for await (let i of result) {
    map1.set(i.fields.name, i.fields.value);
  }
  await $store.dispatch("changeSettingsActions", map1);
};
getInitSetting();
</script>

<style lang="scss" scoped></style>
