<!-- 通用弹窗 -->
<template>
    <div class="body" @click="downProp">
      <div class="body_content">
        <div class="body_content_wrap">
          <div class="body_content_detail">
            {{ $store.state.publicData.value }}
          </div>
        </div>
        <div style="color: #ffffff;margin-top: 10px;font-size: 10px;text-align: center;">点击其他位置关闭</div>
      </div>
    </div>
</template>

<script setup>
import { useStore } from "vuex";
const $store = new useStore();
const props = defineProps({
  data: {
    close: () => {},
  },
});

// 关闭弹窗
const downProp = () => {
  $store.commit('chengePublicData')
}
</script>

<style lang="scss" scoped>
.body{
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
.body_content{
    width: 60%;
  }
  .body_content_wrap{
  padding: 10px;
  background-color: #f3f3f3;
}
.body_content_detail{
  background-color: #fff;
  padding: 10px 0px;
  text-align: center;
}
</style>