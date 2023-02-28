<template>
  <div class="body">
    <div class="body_body">
      <div class="body_body_bar">
        <div>活动设置</div>
        <div>活动样式</div>
        <div>投票设置</div>
      </div>
      <div class="body_body_body">
        <div
          v-for="item in activitySettingOptions"
          :key="item.key"
          class="body_body_item"
        >
          <label>{{ item.label }}</label> <input :type="item.type" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from "vue";

const activitySettingOptions = reactive([
  { label: "活动名称", key: 1, type: "text" },
  { label: "浏览量", key: 2, type: "number" },
  { label: "浏览倍数", key: 3, type: "number" },
]);
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
  z-index: 5;
}
.body_body {
  width: calc(30vw - 40px);
  height: calc(80vh - 40px);
  background-color: white;
  border-radius: 3px;
  padding: 20px;
}
.body_body_bar {
  display: flex;
  div {
    font-size: 15px;
    width: 20%;
    margin-bottom: 10px;
    cursor: pointer;
  }
  border-bottom: 2px solid #d4d4d474;
}
.body_body_body {
  margin: 10px 0px;
}
.body_body_item {
  margin: 10px 0px;
  label {
    display: block;
    font-size: 13px;
    margin-bottom: 5px;
  }
  input {
    outline: none;
    border: 1px solid #e6e6e6;
    border-radius: 3px;
    width: 99%;
    height: 25px;
  }
}
</style>
