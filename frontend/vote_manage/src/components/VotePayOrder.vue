<template>
  <div class="body" @click="$store.commit('changePayOrderRecord')">
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
        <el-table-column prop="open_id" label="用户名(openid)" width="180" />
        <el-table-column prop="price" label="金额" width="180" />
        <el-table-column prop="payment_status" label="支付状态" width="180"
          ><template #default="scope">
            <el-button
              link
              :type="
                scope.row.payment_status === '支付成功' ? 'primary' : 'danger'
              "
              size="small"
              >{{ scope.row.payment_status }}</el-button
            ></template
          ></el-table-column
        >
        <el-table-column
          prop="payment_order_id"
          label="支付订单号"
          width="180"
        />
        <el-table-column prop="prize_type" label="礼物类型" width="180" />
        <el-table-column prop="network" label="网络" width="180" />
        <el-table-column prop="system" label="系统" width="180" />
        <el-table-column prop="phone_model" label="手机型号" width="180" />
        <el-table-column prop="phone_number" label="手机号" width="180" />
        <el-table-column prop="ip" label="ip" width="180" />
        <el-table-column prop="create_time" label="订单创建时间" width="180" />
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
    `/paymentrecord/?token=${jsCookie.get("token")}&vote_id=${
      $store.state.voteManagerPayOrderVoteid
    }`
  );
  if (result.code === 200) {
    let JSONResult = JSON.parse(result.data);
    console.log(JSONResult);
    JSONResult.forEach((item) => {
      tableData.push({
        create_time: parseStampTime(item.fields.create_time),
        ip: item.fields.ip,
        network: item.fields.network,
        payment_order_id: item.fields.payment_order_id,
        payment_status:
          item.fields.payment_status === 1 ? "支付成功" : "支付失败",
        phone_model: item.fields.phone_model,
        phone_number: item.fields.phone_number,
        price: item.fields.price,
        prize_type: item.fields.prize_type,
        system: item.fields.system,
        vote_activity: item.fields.vote_activity,
        open_id: item.fields.voteuser.open_id,
        actions: "删除",
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
