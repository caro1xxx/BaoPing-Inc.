<template>
  <div class="body" @click="$store.commit('changeVoteUserRecord')">
    <div
      class="body_table"
      @click="
        (e) => {
          e.stopPropagation();
        }
      "
    >
      <el-table
        class="body_el_table"
        v-if="tableData"
        :data="tableData"
        stripe
        style="width: 100%"
      >
        <el-table-column prop="vote_id" label="活动编号" width="180"
          ><template #default="scope">
            <el-button link type="primary" size="small">{{
              "#" + scope.row.vote_id
            }}</el-button></template
          ></el-table-column
        >
        <el-table-column prop="count" label="票数" width="180">
          <template #default="scope">
            <div v-if="!scope.row.isEdit">{{ scope.row.count }}</div>
            <el-input v-else type="text" v-model="scope.row.count"
          /></template>
        </el-table-column>
        <el-table-column prop="detail" label="详情" width="180">
          <template #default="scope">
            <div v-if="!scope.row.isEdit">{{ scope.row.detail }}</div>
            <el-input v-else type="text" v-model="scope.row.detail"
          /></template>
        </el-table-column>
        <el-table-column prop="name" label="选手名称" width="180">
          <template #default="scope">
            <div v-if="!scope.row.isEdit">{{ scope.row.name }}</div>
            <el-input v-else type="text" v-model="scope.row.name"
          /></template>
        </el-table-column>
        <el-table-column prop="avator" label="选手头像" width="180">
          <template #default="scope">
            <img
              :src="HOST + '/media/' + scope.row.avator"
              width="30"
              height="30"
              alt=""
            />
          </template>
        </el-table-column>
        <el-table-column label="删除" width="180">
          <template #default="scope">
            <span
              v-if="!scope.row.isEdit"
              style="margin-right: 20px; color: #2479fb; cursor: pointer"
              @click="editVoteUser(scope.row.userId)"
              >编辑</span
            >
            <span
              v-else
              style="margin-right: 20px; color: #2479fb; cursor: pointer"
              @click="saveEidt({ ...scope.row })"
              >保存</span
            >
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script setup>
import { useStore } from "vuex";
import { fether } from "@/utils/fether";
import { reactive } from "vue";
import { HOST } from "@/ENV";
import jsCookie from "js-cookie";
const $store = new useStore();
const tableData = reactive([]);

// 请求投票选手列表
const getUserVoteData = async () => {
  let result = await fether(
    `/votetarget/?vote_id=${$store.state.voteManagerUserRecordVoteid}`
  );
  if (result.code === 200) {
    let JSONResult = JSON.parse(result.data);
    JSONResult.forEach((item) => {
      tableData.push({
        avator: item.fields.avator,
        count: item.fields.count,
        detail: item.fields.detail,
        name: item.fields.name,
        vote_id: item.fields.vote_id,
        isEdit: false,
        userId: item.pk,
      });
    });
  } else {
    // 请求发送错误
    await $store.dispatch("GlobalMessageActions", "操作失败,请重试");
  }
};
getUserVoteData();

// 使可编辑
const editVoteUser = (pk) => {
  tableData.forEach((item, index) => {
    if (item.userId === pk) {
      tableData[index].isEdit = true;
    } else {
      tableData[index].isEdit = false;
    }
  });
};
// 提交编辑
const saveEidt = async (target) => {
  let result = await fether(`/votetarget/`, "put", {
    ...target,
    token: jsCookie.get("token"),
  });
  await $store.dispatch("GlobalMessageActions", result.msg);
};
</script>

<style lang="scss" scoped>
.body {
  position: absolute;
  bottom: 0px;
  left: 0;
  right: 0;
  top: 0;
  background-color: #00000074;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 5;
}
.body_table {
  width: 50%;
  height: 80%;
  background-color: white;
  border-radius: 5px;
  padding: 10px;
}

.body_el_table {
  height: 100%;
}
</style>
