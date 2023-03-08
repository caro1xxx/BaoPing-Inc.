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
  let map1 = [];
  for await (let i of result) {
    map1.push({
      name: i.fields.name,
      value: i.fields.value === "0" ? false : true,
    });
  }
  for (let i in voteSetting[0].fields) {
    map1.push({
      name: i,
      value: voteSetting[0].fields[i],
    });
  }
  await $store.dispatch("changeSettingsActions", map1);
  if ($store.state.settings[77] === 1)
    $router.push(`/one?vote_id=${$route.query.vote_id}`);
  else $router.push(`/two?vote_id=${$route.query.vote_id}`);
};
getInitSetting();
</script>

<style lang="scss" scoped>
*::-webkit-scrollbar {
  display: none;
}
* {
  scrollbar-width: none;
}
* {
  -ms-overflow-style: none;
}
</style>
