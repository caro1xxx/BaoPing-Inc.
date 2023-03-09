<template>
  <todayStarVue v-if="todayStarState" />
  <router-view />
</template>

<script setup>
import { fether } from "./utils/fether";
import { useStore } from "vuex";
import { useRoute, useRouter } from "vue-router";
import todayStarVue from "@/components/todayStar.vue";
import Mobile from "mobile-detect";
import { ref } from "vue";
const $route = useRoute();
const $router = useRouter();
const $store = new useStore();
// console.log($route.query.vote_id)

// 今日执行是否显示
const todayStarState = ref(false);

// 获取初始化设置信息
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
  // 如果开启浏览器访问,那么检测环境
  if ($store.state.settings[69].value && !isEnv()) {
    return;
  }
  getStarShowDate();
  if ($store.state.settings[77].value === 1)
    $router.push(`/one?vote_id=${$route.query.vote_id}`);
  else $router.push(`/two?vote_id=${$route.query.vote_id}`);
};

// 判断当前环境
const isEnv = () => {
  const md = new Mobile(navigator.userAgent);
  if (md.userAgent() !== "WeChat") return false;
  return true;
};

// 判断是否达到今日之星显示日期
const getStarShowDate = () => {
  let currentDateStamp = new Date().getTime();
  if (!currentDateStamp > $store.state.settings[63].value * 1000)
    todayStarState.value = true;
  else todayStarState.value = false;
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
