<template>
  <div class="home">
    <Search />
    <div class="home_title">进行中的任务</div>
    <div class="home_title_body">
      <div v-for="(item, index) in tableData" class="item">
        <div class="id">{{ item.pk }}</div>
        <div style="width: 30%">
          <span class="title">{{ item.name }}</span>
        </div>
        <div style="width: 30%">
          <span class="title">{{ item.task_id }}</span>
        </div>
        <div style="width: 30%">
          <span class="title">{{ parseStampTime(item.create_time) }}</span>
        </div>
        <el-tag v-if="item.status === '1'" class="ml-2" type="success"
          >成功</el-tag
        >
        <el-tag v-else-if="item.status === '2'" class="ml-2" type="danger"
          >失败</el-tag
        >
        <el-tag v-else class="ml-2">进行中</el-tag>
      </div>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue";
import { fether } from "@/utils/fether";
import jsCookie from "js-cookie";
import { reactive, onMounted } from "vue";
import { useStore } from "vuex";
import { parseStampTime } from "../utils/stampTime";
const $store = useStore();

const tableData = reactive([]);

// 获取任务
const getTask = async () => {
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/task/?token=${jsCookie.get("token")}`);
  if (result.code === 200) {
    let JSONResult = JSON.parse(result.data);
    JSONResult.forEach((item) => {
      tableData.push({ ...item.fields, pk: item.pk });
    });
  } else {
    await $store.dispatch("refreshErroActions");
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
  await $store.dispatch("NoticifyActions", false);
};

onMounted(() => {
  setInterval(() => {
    fether(`/task/?token=${jsCookie.get("token")}`)
      .then((res) => res.json())
      .then((result) => {
        if (result.code === 200) {
          let JSONResult = JSON.parse(result.data);
          JSONResult.forEach((item) => {
            tableData.push({ ...item.fields, pk: item.pk });
          });
        }
      });
  }, 1000 * 60 * 5);
});

getTask();
</script>

<style lang="scss" scoped>
.home {
  width: calc(100vw - 250px - 40px);
  height: calc(100vh - 40px);
  font-size: 20px;
  padding: 20px;
  user-select: none;
}
.home_title {
  font-size: 20px;
  font-weight: bold;
  margin: 20px 0px;
}
.home_title_body {
  height: calc(80vh);
  overflow: scroll;
}
.item {
  margin: 10px 10px;
  border-radius: 5px;
  box-shadow: 0 4px 8px 0 rgba(142, 142, 142, 0.2),
    0 6px 20px 0 rgba(149, 149, 149, 0.19);
  padding: 10px;
  display: flex;
  .title {
    font-size: 15px;
    color: #a7d1ff;
    border: 1px solid #f3f7ff;
    border-radius: 5px;
    padding: 3px 3px;
    margin: 0px 5%;
    background-color: #e7f1f8;
  }
  .id {
    width: 20px;
    height: 20px;
    background-color: #0d6efd;
    border-radius: 50%;
    text-align: center;
    line-height: 20px;
    color: white;
    font-size: 10px;
    border: 2px solid rgb(0, 57, 133);
  }
}
</style>
