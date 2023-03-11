<template>
  <div class="body">
    <div class="body_title">{{ $store.state.subNavBarList.navName }}</div>
    <div v-for="(item, index) in $store.state.subNavBarList.item" :key="index">
      <div class="body_item" @click="goPage(item.path)">{{ item.name }}</div>
      <div class="body_desciptions">{{ item.description }}</div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useStore } from "vuex";
const $store = new useStore();
const $router = useRouter();
const goPage = (path) => {
  $router.push(path);
};
</script>

<style lang="scss" scoped>
.body {
  user-select: none;
  width: 200px;
  height: calc(100vh);
  background-color: white;
}
.body_title {
  font-size: 18px;
  margin: 20px 10px;
  font-weight: bold;
  cursor: pointer;
}
.body_item {
  font-size: 15px;
  margin: 0px 10px;
  cursor: pointer;
  border-left: 3px solid #2460e5;
  padding-left: 5px;
}
.body_desciptions {
  font-size: 10px;
  margin: 5px 10px;
  margin-bottom: 20px;
  color: #acacac;
  /* border-bottom: 1px solid #dbdbdb9a; */
}
</style>
