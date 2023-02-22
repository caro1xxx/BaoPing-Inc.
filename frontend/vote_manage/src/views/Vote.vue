<template>
    <div class="system_main">
      <Search />
        <span class="title_style">投票管理</span>
    </div>

</template>

<script setup>
import Search from "@/components/Search.vue";
</script>

<style lang="scss" scoped>
.system_main{
  width: calc(100vw - 170px - 420px);
  height: calc(100vh - 40px);
  font-size: 40px;
  font-weight: 50px;
  margin: 20px 20px;
}
</style>