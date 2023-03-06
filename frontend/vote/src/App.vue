<template>
  <router-view />
</template>

<script setup>
import { fether } from "./utils/fether";
import { useStore } from "vuex";
import { useRoute, useRouter } from "vue-router";
const $route = useRoute();
const $router = useRouter();
const $store = new useStore();
// console.log($route.query.vote_id)
const getInitSetting = async () => {
  let result = await fether("/settings/");
  let voteSetting = await fether(
    `/alonevoteactivity/?vote_id=${$route.query.vote_id}`
  );
  if (!result || !voteSetting) return;
  const map1 = new Map();
  for await (let i of result) {
    map1.set(i.fields.name, i.fields.value === "0" ? false : true);
  }
  for (let i in voteSetting[0].fields) {
    map1.set(i, voteSetting[0].fields[i]);
  }
  await $store.dispatch("changeSettingsActions", map1);
  if ($store.state.settings.get("template_id") === 1)
    $router.push(`/one?vote_id=${$route.query.vote_id}`);
  else $router.push(`/two?vote_id=${$route.query.vote_id}`);
};
getInitSetting();
</script>

<style lang="scss" scoped></style>
