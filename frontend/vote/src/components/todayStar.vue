<template>
  <div class="star" @click="props.data()">
    <img style="width: 70%; height: 40%" src="../assets/img/2.png" alt="" />
    <div class="star_body">
      <div class="star_body_text">
        <div class="title">竞争依然激烈,就保持这个势头!</div>
        <div class="gongxi">恭喜</div>
        <div class="value">
          {{ athleteName.name }}
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
import { fether } from "@/utils/fether";
import { useRoute } from "vue-router";
import { reactive } from "vue";
const $route = useRoute();
const $store = useStore();

const props = defineProps({
  data: {
    close: () => {},
  },
});

// 存储今日之星名字
const athleteName = reactive({
  name: "",
});

// 列表数据
const informationData = reactive([]);

// 获取今日之星
const getTodyStar = async () => {
  let result = await fether(`/todaystar/?vote_id=${$route.query.vote_id}`);
  athleteName.name = result[0].fields.name;
};
getTodyStar();
</script>

<style lang="scss" scoped>
@font-face {
  font-family: Tsanger02;
  src: url("../assets/font/TsangerYuYangT_W02_W02.ttf");
}
@font-face {
  font-family: Tsanger03;
  src: url("../assets/font/TsangerYuYangT_W03_W03.ttf");
}
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
  font-family: Tsanger02;
  color: white;
  position: absolute;
  top: 4%;
  font-size: 15px;
}
.gongxi {
  font-family: Tsanger03;
  font-size: 20px;
  font-weight: bold;
  position: absolute;
  top: 40%;
  color: white;
}
.value {
  font-family: Tsanger03;
  font-weight: bold;
  font-size: 25px;
  position: absolute;
  top: 56%;
  color: white;
}
.star_title {
  font-family: Tsanger02;
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
