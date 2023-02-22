<template>
  <div class="home">
    <div class="home_body">
      <Search />
      <div class="home_title">数据概括</div>
      <div class="home_refresh">
        <img src="../assets/img/17.png" width="20" height="20" alt="" />
        <div>今日,2022/02/02</div>
      </div>
      <div class="home_data">
        <div class="home_data_item">
          <div v-for="item in dataList" class="home_data_item_item">
            <div class="home_data_item_value">{{ item.value }}</div>
            <div class="home_data_item_title">{{ item.title }}</div>
          </div>
        </div>
        <div class="home_data_item">
          <div v-for="item in dataListBot" class="home_data_item_item">
            <div class="home_data_item_value">{{ item.value }}</div>
            <div class="home_data_item_title">{{ item.title }}</div>
          </div>
        </div>
        <img src="../assets/img/20.png" class="home_backgound" alt="" />
      </div>
      <div class="home_table">
        <div class="home_table_head">
          <div v-for="item in tableHead" :key="item.name">{{ item.name }}</div>
        </div>
        <div class="home_table_body_wrap">
          <div class="home_table_body" v-for="item in tableData" :key="item.id">
            <div>{{ item.id }}</div>
            <div>{{ item.domain }}</div>
            <div>{{ item.flow }}</div>
            <div v-if="item.state">
              <img width="20" height="20" src="../assets/img/19.png" alt="" />
            </div>
            <div v-else>
              <img width="20" height="20" src="../assets/img/21.png" alt="" />
            </div>
          </div>
        </div>
      </div>
    </div>
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
  width: calc(100vw - 150px - 400px);
  height: calc(100vh);
  font-size: 20px;
}
.home_body {
  margin: 20px 20px;
}
.home_title {
  margin-top: 47px;
  font-size: 20px;
  font-weight: bold;
}
.home_refresh {
  font-size: 10px;
  color: #b5c3d1;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  margin-top: 10px;
}
.home_data_item {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 10px;
  width: 70%;
  font-size: 15px;
}
.home_data {
  margin-top: 50px;
  font-size: 20px;
  font-weight: bold;
  position: relative;
}
.home_data_item_title {
  text-align: center;
  font-size: 10px;
  font-weight: lighter;
  color: #b5c3d1;
}
.home_data_item_item {
  margin-bottom: 40px;
}
.home_data_item_value {
  text-align: center;
  font-size: 25px;
}
.home_backgound {
  position: absolute;
  right: 0px;
  top: -50px;
  width: 250px;
  height: 200px;
}
.home_table {
  border: 1px solid #b5c3d178;
  border-radius: 10px;
  height: calc(100vh - 410px);
}
.home_table_head {
  border-radius: 10px 10px 0px 0px;
  height: 40px;
  border-bottom: 1px solid #b5c3d178;
  box-shadow: 0 4px 4px 0 #bababa21;
  display: flex;
  div {
    width: 25%;
    text-align: center;
    line-height: 40px;
    font-size: 15px;
    font-weight: lighter;
  }
}
.home_table_body {
  display: flex;
  div {
    width: 25%;
    text-align: center;
    font-size: 14px;
    font-weight: lighter;
    color: #585858;
    margin: 10px 0px;
  }
}
.home_table_body_wrap {
  overflow: scroll;
  height: calc(100vh - 450px);
}
.home_table_body_wrap::-webkit-scrollbar {
  display: none;
}
</style>
