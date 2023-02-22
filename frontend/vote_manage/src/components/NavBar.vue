<template>
  <div class="navbar">
    <div class="navbar_logo">
      <div class="navbar_logo_text">Vote</div>
    </div>
    <div class="navbar_midd">
      <div class="navbar_midd_body">
        <div class="navbar_midd_body_excuteing">执行中</div>
        <div class="navbar_midd_body_line"></div>
        <div class="navbar_midd_body_itemparent">
          <div
            v-for="item in navItme"
            :key="item"
            class="navbar_midd_body_itemFor"
          >
            <img :src="item.img" alt="" width="25" height="25" />
            <div class="navbar_midd_body_item">{{ item.name }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from "vue";

const navItme = reactive([
  { name: "数据信息", img: require("../assets/img/2.png") },
  { name: "系统管理", img: require("../assets/img/5.png") },
  { name: "消息管理", img: require("../assets/img/7.png") },
  { name: "投票管理", img: require("../assets/img/3.png") },
  { name: "订单管理", img: require("../assets/img/4.png") },
  { name: "粉丝管理", img: require("../assets/img/6.png") },
  { name: "自动任务", img: require("../assets/img/1.png") },
]);
</script>

<style lang="scss" scoped>
.navbar {
  width: 273px;
  height: calc(100vh);
  background-color: #fafdff;
  font-size: 15px;
  color: #b5c3d1;
}
.navbar_logo {
  font-size: 50px;
  font-weight: 700;
  font-style: italic;
  color: #4597e8;
  height: 72px;
  width: 100%;
  position: relative;
}
.navbar_logo_text {
  position: absolute;
  top: 36px;
  left: 52px;
}
.navbar_midd {
  width: 100%;
  height: calc(100vh - 102px);
}
.navbar_midd_body {
  margin: 0px 52px;
}
.navbar_midd_body_excuteing {
  padding-top: 76px;
  text-align: center;
}
.navbar_midd_body_line {
  height: 1px;
  padding-top: 22px;
  border-bottom: 1px solid #b5c3d1;
}
.navbar_midd_body_item {
  margin-bottom: 30px;
}
.navbar_midd_body_itemparent {
  padding-top: 63px;
}
.navbar_midd_body_itemFor {
  display: flex;
  justify-content: center;
  position: relative;
  img {
    position: absolute;
    left: 10px;
    top: -3px;
  }
}
</style>
