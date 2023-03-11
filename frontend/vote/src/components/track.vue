<template>
  <div class="track" @click="props.data.close">
    <div class="track_body" @click="(e) => e.stopPropagation()">
      <div class="track_body_content">
        <div class="track_body_content_item" v-for="item in reportList">
          <div>{{ item.title }}</div>
          <div
            style="
              font-size: 10px;
              font-style: italic;
              color: #cecece;
              margin: 10px 10px;
            "
          >
            详情见:{{ item.link }}
            <span
              style="float: right; color: #0d6efd"
              @click="toTarget(item.link)"
              >查看详情</span
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, onMounted } from "vue";
import { useStore } from "vuex";

const $store = useStore();
const props = defineProps({
  data: Object,
});

const reportList = reactive([]);

const toTarget = (url) => {
  window.open("https://" + url);
};

onMounted(() => {
  let JSONList = JSON.parse($store.state.settings[96].value);
  JSONList.forEach((item) => {
    reportList.push({ ...item });
  });
});
</script>

<style lang="scss" scoped>
.track {
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
.track_body {
  height: 60%;
  width: 80%;
  border-radius: 5px;
  padding: 10px;
  background-color: #f3f3f3;
}
.track_body_content {
  background-color: white;
  border-radius: 5px;
  height: 100%;
  overflow: scroll;
}

.track_body_content::-webkit-scrollbar {
  display: none;
}
.track_body_content_item {
  margin: 10px 0px;
  padding: 10px;
  font-size: 15px;
  border-bottom: 0.5px solid #ededed;
}
</style>
