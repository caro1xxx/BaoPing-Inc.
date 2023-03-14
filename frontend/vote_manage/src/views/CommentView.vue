<template>
  <div class="home">
    <Search />
    <div class="home_title">评论管理</div>
    <div style="padding: 10px; background-color: white; border-radius: 3px">
      <el-table :data="tableData" class="table_style">
        <el-table-column prop="vote_target" label="评论目标" width="180" />
        <el-table-column prop="vote_user" label="评论用户" width="180" />
        <el-table-column prop="content" label="内容"
          ><template #default="scope"
            ><div class="content">{{ scope.row.content }}</div></template
          ></el-table-column
        >
        <el-table-column prop="status" label="审核状态" width="100"
          ><template #default="scope"
            ><el-switch
              @change="changeCommentStatus(scope.row.pk)"
              :model-value="scope.row.status === 1 ? true : false"
          /></template>
        </el-table-column>
        <el-table-column prop="create_time" label="评论时间" width="100">
          <template #default="scope">
            <div>{{ parseStampTime(scope.row.create_time) }}</div>
          </template>
        </el-table-column>
        <el-table-column prop="操作" label="操作" width="100">
          <template #default="scope"
            ><div
              style="color: red; cursor: pointer"
              @click="deleteComments(scope.row.pk)"
            >
              删除
            </div>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue";
import { fether } from "@/utils/fether";
import jsCookie from "js-cookie";
import { reactive } from "vue";
import { useStore } from "vuex";
import { parseStampTime } from '../utils/stampTime'
const tableData = reactive([]);
const $store = useStore();
// 获取评论数据
const getComment = async () => {
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/comment/?token=${jsCookie.get("token")}`);
  if (result.code == 200) {
    let JSONResult = JSON.parse(result.data);
    JSONResult.forEach((item) => {
      console.log(item.fields);
      tableData.push({ ...item.fields, pk: item.pk });
    });
  } else {
    // 请求发送错误
    await $store.dispatch("refreshErroActions");
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
  await $store.dispatch("NoticifyActions", false);
};

const changeCommentStatus = async (pk) => {
  for (let i = 0; i < tableData.length; i++) {
    if (tableData[i].pk === pk) {
      tableData[i].status = tableData[i].status === 1 ? 0 : 1;
      let result = await fether("/comment/", "put", {
        token: jsCookie.get("token"),
        data: { pk: pk, status: tableData[i].status },
      });
      await $store.dispatch("GlobalMessageActions", result.msg);
      break;
    }
  }
};

const deleteComments = async (pk) => {
  for (let i = 0; i < tableData.length; i++) {
    if (tableData[i].pk === pk) {
      tableData.splice(i, 1);
      let result = await fether("/comment/", "delete", {
        token: jsCookie.get("token"),
        pk: pk,
      });
      await $store.dispatch("GlobalMessageActions", result.msg);
      break;
    }
  }
};

getComment();
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
.table_style {
  height: calc(78vh);
}
.table_style::-webkit-scrollbar {
  display: none;
}
.content {
  max-height: 60px;
  overflow: scroll;
}
</style>
