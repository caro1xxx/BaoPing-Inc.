<template>
  <div class="star" @click="props.data()">
    <div class="star_body">
      <img src="../assets/img/2.png" alt="" />
      <div class="title">竞争依然激烈,就保持这个势头!</div>
      <div class="content">
        <div style="font-size: 20px; font-weight: bold; margin-right: 10px">
          恭喜
        </div>
        <div style="font-size: 25px">{{ $store.state.settings[58].value }}</div>
        <div style="font-size: 20px">
          获得<span style="color: #f5c85f; font-weight: bold">今日之星</span>
        </div>
      </div>
      <div class="support_do" @click="(e) => support(e)">支持一下</div>
      <div class="close">点击任意位置关闭弹窗</div>
    </div>
  </div>
</template>

<script setup>
import { useStore } from "vuex";
const $store = useStore();

const props = defineProps({
  data: {
    close: () => {},
  },
});

// 支持一下
const support = (e) => {
  e.stopPropagation();
  console.log(1);
};
</script>

<style lang="scss" scoped>
.star {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background-color: #00000074;

  background-size: 100% 110%;
  background-repeat: no-repeat;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  z-index: 10;
}
.star_body {
  width: 70%;
  position: relative;
  display: inline-flex;
  vertical-align: top;
  align-items: center;
  justify-content: center;
}
.title {
  color: white;
  position: absolute;
  top: 15px;
  font-size: 15px;
}
.content {
  margin-top: 50px;
  position: absolute;
  color: white;
  text-align: center;
  div {
    line-height: 50px;
  }
}
.support_do {
  color: white;
  position: absolute;
  bottom: -80px;
  height: 40px;
  width: 70%;
  line-height: 40px;
  font-weight: bold;
  font-size: 15px;
  text-align: center;
  background-color: rgb(139, 33, 31);
  border-radius: 20px;
  border: 2px solid rgb(231, 176, 100);
}
.close {
  position: absolute;
  bottom: -100px;
  font-size: 10px;
  color: white;
}
</style>
