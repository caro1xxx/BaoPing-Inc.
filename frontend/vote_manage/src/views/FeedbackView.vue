<template>
  <div class="system_main">
    <div class="system_main_body">
      <Search />
      <div class="title_style" @click="editUser">反馈信息</div>
      <div class="home_table">
        <div class="home_table_grid">
          <div
            v-for="(item, index) in tableData"
            class="home_table_item"
            @mouseenter="onClickMove(index, true)"
            @mouseleave="onClickMove(index, false)"
          >
            <div class="home_table_item_top">
              <img :src="require(`../assets/img/avator/${item.avator}.png`)" />
              <div>{{ item.wx_username }}</div>
            </div>
            <div style="margin-left: 30px">{{ item.content }}</div>
            <div
              style="
                margin-top: 5px;
                color: #cecece;
                font-size: 10px;
                text-align: end;
              "
            >
              反馈时间:{{ item.create_time }}
            </div>
            <div class="home_table_item_move" v-show="item.isMove">
              <svg
                @click="deleteFeedback(item.pk)"
                t="1677328484608"
                class="icon"
                viewBox="0 0 1024 1024"
                version="1.1"
                xmlns="http://www.w3.org/2000/svg"
                p-id="10871"
                width="30"
                height="30"
              >
                <path
                  d="M512 512m-512 0a512 512 0 1 0 1024 0 512 512 0 1 0-1024 0Z"
                  fill="#FDEBED"
                  p-id="10872"
                ></path>
                <path
                  d="M729.6 384H294.4c-7.68 0-12.8-5.12-12.8-12.8v-25.6c0-7.68 5.12-12.8 12.8-12.8h115.2v-25.6c0-14.08 11.52-25.6 25.6-25.6h153.6c14.08 0 25.6 11.52 25.6 25.6v25.6h115.2c7.68 0 12.8 5.12 12.8 12.8v25.6c0 7.68-5.12 12.8-12.8 12.8z m-371.2 38.4h307.2c28.16 0 51.2 23.04 51.2 51.2v217.6c0 28.16-23.04 51.2-51.2 51.2H358.4c-28.16 0-51.2-23.04-51.2-51.2V473.6c0-28.16 23.04-51.2 51.2-51.2z m192 243.2c0 7.68 5.12 12.8 12.8 12.8s12.8-5.12 12.8-12.8V537.6c0-7.68-5.12-12.8-12.8-12.8s-12.8 5.12-12.8 12.8v128z m-102.4 0c0 7.68 5.12 12.8 12.8 12.8s12.8-5.12 12.8-12.8V537.6c0-7.68-5.12-12.8-12.8-12.8s-12.8 5.12-12.8 12.8v128z"
                  fill="#EC3A4E"
                  p-id="10873"
                ></path>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue";
import { fether } from "@/utils/fether";
import { reactive, watch } from "vue";
import { useStore } from "vuex";
import Cookies from "js-cookie";
import { parseStampTime } from "../utils/stampTime";
const $store = new useStore();
// 表数据
const tableData = reactive([]);

// 获取反馈信息
const getFeedbackList = async () => {
  // 开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(
    `/feedback/?token=${Cookies.get("token")}&value=all`
  );
  if (result.code === 200) {
    //serve
    result.data.forEach((item) => {
      tableData.push({
        ...item,
        create_time: parseStampTime(item.create_time),
      });
    });
  } else {
    // 请求发送错误
    await $store.dispatch("refreshErroActions");
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
};

// 删除反馈信息
const deleteFeedback = async (pk) => {
  // 开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/feedback/`, "delete", {
    token: Cookies.get("token"),
    feedback_id: pk,
  });
  if (result.code === 200) {
    tableData.forEach((item, index) => {
      if (item.pk === pk) {
        tableData.splice(index, 1);
      }
    });
  } else {
    // 请求发送错误
    await $store.dispatch("refreshErroActions");
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
};

// 鼠标移入移出
const onClickMove = async (index, type) => {
  tableData[index].isMove = type;
};

watch(
  () => $store.state.isUserEditSave,
  (newVal) => {
    saveUserEdit($store.state.editPopProps);
  }
);

getFeedbackList();
</script>

<style lang="scss" scoped>
.system_main {
  width: calc(100vw - 250px);
  height: calc(100vh);
  font-size: 20px;
}
.system_main_body {
  padding: 20px 20px;
}
.home_table {
  margin-top: 20px;
  font-size: 10px;
  height: calc(100vh - 150px);
  overflow: scroll;
}
.home_table::-webkit-scrollbar {
  display: none;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}
.home_table_item {
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 4px 4px 0 rgba(236, 236, 236, 0.2),
    0 6px 20px 0 rgba(236, 236, 236, 0.2);
  padding: 10px 10px;
  position: relative;
}
.home_table_grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-gap: 10px;
}
.home_table_item_top {
  display: flex;
  justify-items: center;
  div {
    line-height: 30px;
    margin-left: 5px;
  }
  img {
    width: 30px;
    height: 30px;
  }
}
.home_table_item_auth {
  position: absolute;
  z-index: 2;
  right: 10px;
  top: 10px;
}
.home_table_item_move {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #5f87dc9d;
  border-radius: 5px;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  cursor: default;
  svg {
    margin: 0px 10px;
    cursor: pointer;
  }
}
</style>
