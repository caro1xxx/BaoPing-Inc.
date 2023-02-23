<!-- 系统设置 -->
<template>
  <div class="system_main">
    <div class="system_main_body">
      <Search />
      <div class="title_style">权限分组</div>
    </div>
  </div>
</template>

<script>
import Search from "@/components/Search.vue";

export default {
  data() {
    return {};
  },
  components: {
    Search,
  },
};
</script>

<style lang="scss" scoped>
.system_main {
  width: calc(100vw - 200px);
  height: calc(100vh);
  font-size: 20px;
  font-weight: 50px;
}
.system_main_body {
  margin: 20px 20px;
}
</style>
