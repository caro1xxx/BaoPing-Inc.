<template>
  <div class="editor">
    <div style="background-color: white">
      <vue3-tinymce v-model="state.content" :setting="state.setting" />
    </div>
    <img
      @click="props.data.close(state.content)"
      class="close"
      src="../assets/img/31.png"
      alt=""
    />
  </div>
</template>

<script setup>
import { fether } from "@/utils/fether";
import Vue3Tinymce from "@jsdawn/vue3-tinymce";
import { reactive } from "vue";

const props = defineProps({
  data: {
    value: String,
    close: (change) => {},
  },
});

// 编辑框配置
const state = reactive({
  content: props.data.value,
  // editor 配置项
  setting: {
    height: "calc(100vh)", // editor 高度
    width: "calc(50vw)",
    language_url: "/langs/zh-Hans.js",
    language: "zh-Hans",
  },
});
</script>

<style lang="scss" scoped>
.editor {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0px;
  z-index: 6;
  display: flex;
  align-items: end;
  justify-content: end;
}
.close {
  position: absolute;
  right: calc(51vw);
  width: 30px;
  height: 30px;
  top: 10px;
  cursor: pointer;
}
</style>
