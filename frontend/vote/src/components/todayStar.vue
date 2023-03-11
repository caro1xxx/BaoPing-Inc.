<template>
  <div class="star" @click="props.data()">
    <img style="width: 70%; height: 40%" src="../assets/img/2.png" alt="" />
    <div class="star_body">
      <div class="star_body_text">
        <div class="title">竞争依然激烈,就保持这个势头!</div>
        <div class="gongxi">恭喜</div>
        <div class="value">
          {{ $store.state.settings[58].value }}
        </div>
        <div class="star_title">
          获得<span style="color: #f5c85f; font-weight: bold">今日之星</span>
        </div>
        <div class="close">点击任意位置关闭弹窗</div>
      </div>
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
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  z-index: 11;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
}
.star_body_text {
  width: 70%;
  height: 40%;
  display: inline-flex;
  vertical-align: top;
  align-items: center;
  justify-content: center;
  position: relative;
}
.title {
  color: white;
  position: absolute;
  top: 4%;
  font-size: 15px;
}
.gongxi {
  font-size: 20px;
  font-weight: bold;
  position: absolute;
  top: 40%;
  color: white;
}
.value {
  font-weight: bold;
  font-size: 25px;
  position: absolute;
  top: 56%;
  color: white;
}
.star_title {
  font-weight: bold;
  font-size: 20px;
  position: absolute;
  top: 70%;
  color: white;
}
.close {
  position: absolute;
  bottom: -10%;
  font-size: 10px;
  color: white;
}
</style>
