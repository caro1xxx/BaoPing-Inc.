<template>
  <div class="body">
    <div class="body_btn" @click="refresh">
      <div>
        网络错误,点我刷新<svg
          t="1677331480221"
          class="icon"
          viewBox="0 0 1024 1024"
          version="1.1"
          xmlns="http://www.w3.org/2000/svg"
          p-id="14583"
          width="20"
          height="20"
        >
          <path
            d="M91.556 575.926l320.512 1.553a11.5 11.5 0 0 1 8.082 3.373c4.488 4.494 4.483 11.776-0.011 16.264L304.142 712.96c52.677 54.393 126.493 88.207 208.208 88.207 135.019 0 248.469-92.314 280.637-217.248l148.003 0.001C906.5 789.416 727.718 946 512.35 946c-121.75 0-231.807-50.04-310.715-130.67L99.626 917.205a11.5 11.5 0 0 1-8.126 3.363c-6.351 0-11.5-5.149-11.5-11.5V587.37c0.03-6.352 5.205-11.475 11.556-11.445zM512.35 77c120.871 0 230.219 49.321 309.003 128.93l106.02-105.881a11.5 11.5 0 0 1 8.127-3.363c6.351 0 11.5 5.149 11.5 11.5V429.882a11.496 11.496 0 0 1-5.887 9.984c0.091 0.503 0.175 1.01 0.257 1.516h-147.8l-0.191-0.744-178.447-0.864a11.5 11.5 0 0 1-7.831-3.13l-0.25-0.244c-4.489-4.494-4.484-11.775 0.01-16.263l111.991-111.844c-52.56-53.37-125.665-86.46-206.502-86.46-135.846 0-249.859 93.449-281.22 219.548H83.33C116.866 234.755 296.18 77 512.35 77z"
            fill="#ffffff"
            p-id="14584"
          ></path>
        </svg>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useStore } from "vuex";

const $store = new useStore();

const refresh = () => {
  $store.commit("reFresh");
};
</script>

<style lang="scss" scoped>
.body {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  cursor: default;
  z-index: 2;
  .body_btn {
    background-color: #2460e5;
    padding: 10px 20px;
    padding-right: 40px;
    color: white;
    border-radius: 5px;
    vertical-align: top;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    position: relative;
    svg {
      position: absolute;
      top: 11px;
    }
  }
}
</style>
