<template>
  <div class="welcome" @click="props.data.close">
    <img class="welcome_background" src="../assets/img/3.png" alt="" />
    <div class="welcome_body">
      <div class="body">
        <div>
          您已经<span style="color: yellow">{{ props.data.value }}分钟</span
          >没有来了,上次支持过的选手现在是
        </div>
        <div style="font-size: 30px">
          第<span style="font-size: 50px; font-weight: bold">{{
            props.data.ranking
          }}</span
          >名
        </div>
        <img
          style="width: 100px; height: 100px; margin: 20px 0px"
          :src="HOST2 + '/meida/' + props.data.img"
          alt=""
        />
        <div style="font-weight: bold">{{ props.data.name }}</div>
        <div
          @click="
            (e) => {
              support(e);
            }
          "
          style="
            margin-top: 45px;
            font-weight: bold;
            font-size: 20px;
            color: #444444;
          "
        >
          马上支持
        </div>
        <div style="margin-top: 40px; font-size: 10px">
          冠军宝座仍被觊觎,不可松懈,坚持住
        </div>
        <div style="margin-top: 15px; font-size: 10px">
          点击任意位置关闭弹窗
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { HOST2 } from "@/ENV";

const props = defineProps({
  data: Object,
});

const support = (e) => {
  e.stopPropagation();
};
</script>

<style lang="scss" scoped>
.welcome {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background-color: #00000074;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  z-index: 10;
}
.welcome_background {
  height: 60%;
  width: 80%;
  position: relative;
}
.welcome_body {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  z-index: 11;
  .body {
    width: 50%;
    height: 30%;
    color: white;
    text-align: center;
  }
}
</style>
