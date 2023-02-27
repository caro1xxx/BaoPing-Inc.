<template>
  <div class="home">
    <Search />
    <div class="home_title">支付记录</div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue";
</script>

<style lang="scss" scoped>
.home {
  width: calc(100vw - 250px - 40px);
  height: calc(100vh - 40px);
  font-size: 20px;
  padding: 20px;
}
.home_title {
  font-size: 20px;
  font-weight: bold;
  margin: 20px 0px;
}
</style>
