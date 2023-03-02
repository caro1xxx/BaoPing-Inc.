<template>
  <div class="system_main">
    <div class="system_main_body">
      <Search />
      <div class="title_style" @click="editUser">反馈信息</div>
      <div style="padding: 10px; background-color: white; border-radius: 3px">
        <el-table
          :data="tableData"
          class="body_system_table"
          style="width: 100%"
        >
          <el-table-column prop="avator" label="头像" width="180">
            <template #default="scope">
              <img
                :src="HOST + '/media/avator/' + scope.row.avator + '.png'"
                alt=""
              />
            </template>
          </el-table-column>
          <el-table-column prop="create_time" label="反馈时间" width="180" />
          <el-table-column prop="content" label="内容" />
          <el-table-column prop="open_id" label="oepnid" />
          <el-table-column prop="wx_username" label="微信名称" />
        </el-table>
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
import { HOST } from "../ENV";
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
    let JSONResult = JSON.parse(result.data);
    console.log(JSONResult);
    JSONResult.forEach((item) => {
      tableData.push({
        content: item.fields.content,
        create_time: parseStampTime(item.fields.create_time),
        avator: item.fields.voteuser.avator,
        open_id: item.fields.voteuser.open_id,
        wx_username: item.fields.voteuser.wx_username,
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
.title_style {
  font-weight: bold;
  margin: 20px 0px;
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
.body_system_table {
  height: calc(78vh);
}
</style>
