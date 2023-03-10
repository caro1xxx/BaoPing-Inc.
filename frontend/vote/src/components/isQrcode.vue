<template>
  <div class="body" @click="props.data.close">
    <div class="body_content" @click="(e) => e.stopPropagation()">
      <div>你已点赞成功</div>
      <img
        class="qscodeImg"
        v-if="$store.state.settings[26].value"
        :src="`${HOST}/media/${$store.state.settings[92].value}`"
        alt=""
      />
    </div>
  </div>
</template>

<script setup>
import { defineEmits } from "vue";
import { useStore } from "vuex";
import { HOST } from "../ENV";
const emit = defineEmits(["returnPage"]);
const $store = new useStore();
const props = defineProps({
  data: Object,
});
</script>

<style lang="scss" scoped>
.body {
  position: absolute;
  top: 0px;
  right: 0;
  left: 0;
  bottom: 0;
  background-color: #00000074;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 6;
}
.body_content {
  width: 80%;
  height: 40%;
  background-color: #f3f3f3;
  border-radius: 10px;
}
.body_content > div {
  height: 40px;
  font-size: 25px;
  font-weight: 500;
  text-align: center;
  line-height: 40px;
  margin-top: 20px;
}
.downImg {
  position: absolute;
  top: 245px;
  left: 365px;
}

.qscodeImg {
  width: 40%;
  height: 40%;
  display: block;
  margin: 20px auto 0px;
}
</style>
