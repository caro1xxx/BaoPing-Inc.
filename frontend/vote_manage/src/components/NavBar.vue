<template>
  <div class="navbar">
    <div class="navbar_logo">
      <div class="navbar_logo_text">Vote</div>
    </div>
    <div class="navbar_midd">
      <div class="navbar_midd_body">
        <div class="navbar_midd_body_excuteing">
          <img
            src="../assets/img/16.png"
            alt=""
            class="icon_style navbar_icon"
          />
          <div>执行中</div>
          <img
            src="../assets/img/15.png"
            alt=""
            class="icon_style navbar_notify"
          />
        </div>
        <div class="navbar_midd_body_line"></div>
        <div class="navbar_midd_body_itemparent">
          <div
            v-for="item in navItme"
            :key="item"
            class="navbar_midd_body_itemFor"
            @click="SureMenu(item.path)"
          >
            <img :src="item.img" alt="" class="icon_style" />
            <div class="navbar_midd_body_item">{{ item.name }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from "vue";
import { useRouter } from "vue-router";

const navItme = reactive([
  { name: "数据信息", img: require("../assets/img/2.png"), path: "/" },
  { name: "系统管理", img: require("../assets/img/5.png"), path: "/system" },
  { name: "消息管理", img: require("../assets/img/7.png"), path: "/news" },
  { name: "投票管理", img: require("../assets/img/3.png"), path: "/Vote" },
  { name: "订单管理", img: require("../assets/img/4.png"), path: "/Order" },
  {
    name: "粉丝管理",
    img: require("../assets/img/6.png"),
    path: "/Vermicelli",
  },
  {
    name: "自动任务",
    img: require("../assets/img/1.png"),
    path: "/Assignment",
  },
]);
const router = useRouter();
const SureMenu = (value) => {
  router.push(`${value}`);
};
</script>

<style lang="scss" scoped>
.navbar {
  width: 200px;
  height: calc(100vh);
  background-color: #fafdff;
  font-size: 10px;
  color: #b5c3d1;
}
.navbar_logo {
  font-size: 40px;
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
  left: 32px;
}
.navbar_midd {
  width: 100%;
  height: calc(100vh - 102px);
}
.navbar_midd_body {
  margin: 0px 25px;
}
.navbar_midd_body_excuteing {
  display: flex;
  justify-content: center;
  position: relative;
  .navbar_icon {
    position: absolute;
    left: 10px;
    top: 71px;
  }
  padding-top: 76px;
}
.navbar_midd_body_line {
  height: 1px;
  padding-top: 22px;
  border-bottom: 1px solid #b5c3d17a;
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
    top: -5px;
  }
}
.navbar_notify {
  position: absolute;
  right: 10px;
  top: 75px;
  width: 20px;
  height: 20px;
}
</style>
