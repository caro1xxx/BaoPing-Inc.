<template>
  <div class="home">
    <Search />
    <div class="home_title">数据概括</div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue";
import { reactive } from "vue";

// 数据列表
const dataList = reactive([
  { title: "总访问量", value: 3000 },
  { title: "总访问量", value: 2000 },
  { title: "总访问量", value: 9999 },
]);

// 第二排数据列表
const dataListBot = reactive([
  { title: "总访问量", value: 122 },
  { title: "总访问量", value: 1000 },
  { title: "总访问量", value: 1000 },
  { title: "总访问量", value: 1000 },
]);
// 表头数据
const tableHead = reactive([
  { name: "活动ID" },
  { name: "域名" },
  { name: "访问流量" },
  { name: "状态" },
]);

// 表数据
const tableData = reactive([
  { id: "#1", domain: "http://www.baidu.com", flow: "1.2k", state: false },
  { id: "#2", domain: "http://www.baidu.com", flow: "1.2k", state: true },
  { id: "#3", domain: "http://www.baidu.com", flow: "1.2k", state: true },
  { id: "#4", domain: "http://www.baidu.com", flow: "1.2k", state: false },
  { id: "#4", domain: "http://www.baidu.com", flow: "1.2k", state: false },
  { id: "#4", domain: "http://www.baidu.com", flow: "1.2k", state: false },
  { id: "#4", domain: "http://www.baidu.com", flow: "1.2k", state: false },
  { id: "#4", domain: "http://www.baidu.com", flow: "1.2k", state: false },
  { id: "#4", domain: "http://www.baidu.com", flow: "1.2k", state: false },
]);
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
