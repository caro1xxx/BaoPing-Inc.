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
        <el-table-column prop="vote_activity" label="活动" width="180"
          ><template #default="scope">
            <el-button link type="primary" size="small">{{
              "#" + scope.row.vote_activity
            }}</el-button></template
          ></el-table-column
        >
        <el-table-column prop="openid" label="用户名(openid)" width="180" />
        <el-table-column prop="count" label="票数" width="180" />
        <el-table-column prop="ip" label="ip" width="180" />
        <el-table-column prop="phone_model" label="手机型号" width="180" />
        <el-table-column prop="system" label="系统" width="180" />
        <el-table-column prop="network" label="网络" width="180" />
        <el-table-column prop="create_time" label="投票时间" width="180" />
      </el-table>
    </div>
  </div>
</template>

<script setup>
import { useStore } from "vuex";
import { fether } from "@/utils/fether";
import { parseStampTime } from "../utils/stampTime";
import jsCookie from "js-cookie";
import { reactive } from "vue";
const $store = new useStore();
const tableData = reactive([]);

// 请求用户投票数据
const getUserVoteData = async () => {
  let result = await fether(
    `/voterecord/?token=${jsCookie.get("token")}&vote_id=${
      $store.state.voteManagerUserRecordVoteid
    }`
  );
  if (result.code === 200) {
    let JSONResult = JSON.parse(result.data);
    JSONResult.forEach((item) => {
      tableData.push({
        vote_activity: item.fields.vote_activity,
        openid: item.fields.voteuser.open_id,
        count: "x1",
        ip: item.fields.ip,
        phone_model: item.fields.phone_model,
        system: item.fields.system,
        network: item.fields.network,
        create_time: parseStampTime(item.fields.create_time),
        action: "删除",
      });
    });
  } else {
    // 请求发送错误
    await $store.dispatch("GlobalMessageActions", "操作失败,请重试");
  }
};
getUserVoteData();
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
