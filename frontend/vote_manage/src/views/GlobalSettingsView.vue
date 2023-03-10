<template>
  <div class="home">
    <Search />
    <div class="home_title">全局设置</div>
    <div class="home_hitn">
      全局设置下的状态将影响所有活动的"其他"选项中的输入状态
    </div>
    <div class="home_body">
      <div v-for="(item, index) in optionList" class="body_body_item">
        <label>{{ item.name }}</label>
        <el-switch
          class="switch"
          v-model="item.value"
          @change="saveSettings(index)"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue";
import { fether } from "@/utils/fether";
import jsCookie from "js-cookie";
import { reactive } from "vue";
import { useStore } from "vuex";

const $store = new useStore();
const optionList = reactive([]);
const optionList2 = reactive([]);

// 获取全局设置
const getSettings = async () => {
  //开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/settings/?token=${jsCookie.get("token")}`);
  if (result.code === 200) {
    let JSONResult = JSON.parse(result.data);
    JSONResult.forEach((item) => {
      optionList.push({
        name: item.fields.name,
        value: item.fields.value === "1" ? true : false,
        pk: item.pk,
      });
      optionList2.push({
        name: item.fields.name,
        value: item.fields.value,
        pk: item.pk,
      });
    });
  } else {
    await $store.dispatch("GlobalMessageActions", result.msg);
  }
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
};

// 提交保存
const saveSettings = async (target) => {
  //开启加载loading
  await $store.dispatch("NoticifyActions", true);
  optionList2[target].value = optionList[target].value ? "1" : "0";
  let result = await fether("/settings/", "put", {
    token: jsCookie.get("token"),
    data: { pk: optionList2[target].pk, value: optionList2[target].value },
  });
  await $store.dispatch("GlobalMessageActions", result.msg);
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
};

getSettings();
</script>

<style lang="scss" scoped>
.home {
  width: calc(100vw - 250px - 40px);
  height: calc(100vh - 40px);
  font-size: 20px;
  padding: 20px;
}
.home_title {
  font-size: 20px;
  font-weight: bold;
  margin: 20px 0px;
}
.home_body {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 10px;
  margin-top: 10px;
  height: calc(100vh - 170px);
  overflow: scroll;
}
.home_hitn {
  font-size: 10px;
}
.body_body_item {
  display: flex;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;

  border-bottom: 0.5px solid #cecece89;
  margin: 10px 0px;
  label {
    display: block;
    font-size: 13px;
    width: 90%;
  }
  .switch {
    width: 10%;
  }
}
</style>
