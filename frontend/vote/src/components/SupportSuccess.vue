<template>
  <div class="support" @click="props.data.close">
    <img class="support_img" src="../assets/img/5.png" alt="" />
    <div class="support_body">
      <div style="text-align: center">
        <div class="support_body_pk">{{ props.data.data.pk }}号</div>
        <div>
          <img
            class="support_body_avator"
            :src="HOST2 + '/media/' + props.data.data.avator"
            alt=""
          />
        </div>
        <div>
          {{ props.data.data.name }}
        </div>
        <div class="rank">
          <div>
            <div class="number">{{ props.data.data.count }}</div>
            <div class="dscription">支持次数</div>
          </div>
          <div>
            <div class="number">{{ props.data.data.rank }}</div>
            <div class="dscription">排名</div>
          </div>
        </div>
      </div>
      <div class="bot">
        <div>
          <img
            :src="HOST2 + '/media/' + $store.state.settings[92].value"
            alt=""
          />
        </div>
        <div></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { HOST2 } from "@/ENV";

const props = defineProps({
  data: Object,
});


</script>

<style lang="scss" scoped>
.support {
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
.support_img {
  width: 90%;
  height: 60%;
}
.support_body {
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
}
.support_body_pk {
  background-color: green;
  font-size: 15px;
  font-weight: bold;
  color: white;
  line-height: 30px;
  height: 30px;
  display: inline-block;
  padding: 0px 20px;
  border-radius: 20px;
}
.support_body_avator {
  width: 200px;
  height: 100px;
  margin: 20px 0px;
}
.rank {
  display: flex;

  div {
    text-align: center;
    width: 150px;
  }
}
.dscription {
  font-size: 13px;
}
.number {
  font-size: 25px;
  font-weight: bolder;
  color: rgb(157, 14, 16);
}
.bot {
  position: absolute;
  bottom: 100px;
  right: 10%;
  margin-top: 100px;
  div {
    width: 100px;
    height: 100px;
  }
}
</style>
