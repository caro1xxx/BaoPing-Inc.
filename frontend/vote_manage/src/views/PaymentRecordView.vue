<template>
  <div class="home">
    <Search />
    <div class="home_title">支付记录</div>
    <div class="home_body">
      <el-table :data="payNotesData" class="home_body_table">
        <el-table-column prop="id" label="活动">
          <template #default="scope">
            <span>{{ scope.$index }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="open_id" label="openid(用户名)" />
        <el-table-column prop="price" label="金额" />
        <el-table-column prop="prize_type" label="礼物类型" />
        <el-table-column prop="status" label="票数">
          <template #default="scope">
            <div>1</div>
          </template>
        </el-table-column>
        <el-table-column prop="payment_order_id" label="支付订单号" />
        <el-table-column prop="create_time" label="支付时间">
          <template #default="scope">
            <span>{{ getTime(scope.row.create_time) }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="payment_status" label="支付状态">
          <template #default="scope">
            <div>{{ scope.row.payment_status ? '开' : '关' }}</div>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template #default="scope">
            <span
              style="color: red"
              @click="deletePayNotes(scope.row, scope.$index)"
              >删除</span
            >
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue";
import { reactive, watch } from "vue";
import { useStore } from "vuex";
import { fether } from "@/utils/fether";
import Cookies from "js-cookie";
const $store = new useStore();
const payNotesData = reactive([]);

const isAxiosStatus = async (data, status) => {
  if (status === false) {
    payNotesData.splice(0, payNotesData.length);
  }
  if (data.code === 200) {
    let Arr = [];
    Arr = JSON.parse(data.data);
    Arr.map((item) => {
      payNotesData.push({
        ...item.fields,
        pk: item.pk,
        wx_username: item.fields.voteuser.wx_username,
        open_id: item.fields.voteuser.open_id,
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

// 获取支付记录数据
const getPayNotesData = async () => {
  // 开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/paymentrecord/?token=${Cookies.get("token")}`);
  if (result.code === 200) {
    let Arr = [];
    Arr = JSON.parse(result.data);
    Arr.map((item) => {
      payNotesData.push({
        ...item.fields,
        pk: item.pk,
        wx_username: item.fields.voteuser.wx_username,
      });
    });
    isAxiosStatus(result, true);
    // 关闭加载loading
    $store.commit("noticifyLoading", false);
  }
};
getPayNotesData();

const deletePayNotes = async (value, index) => {
  //开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(
    `/paymentrecord/`,
    `delete`,
    {
      pk: value.pk,
      token: Cookies.get("token"),
    },
    $store.state.userInfo.name,
    "支付记录"
  );
  if (result.code === 200) {
    // 删除本地数据
    payNotesData.splice(index, 1);
  }
  await $store.dispatch("GlobalMessageActions", result.msg);
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
};
const getTime = (value) => {
  if (value === 0) {
    return "1970/1/1 0:0";
  } else if (String(value).length > 10) {
    let d = new Date(value);
    return `${d.getFullYear()}/${
      d.getMonth() + 1
    }/${d.getDate()} ${d.getHours()}:${d.getMinutes()}`;
  } else {
    let d = new Date(value * 1000);
    return `${d.getFullYear()}/${
      d.getMonth() + 1
    }/${d.getDate()} ${d.getHours()}:${d.getMinutes()}`;
  }
};

// 监听筛选数据
watch(
  () => $store.state.filterData,
  (newVal) => {
    isAxiosStatus(newVal, false);
  }
);
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
  cursor: pointer;
  user-select: none;
}
svg {
  cursor: pointer;
}
.home_body {
  padding: 10px;
  background-color: #fff;
}
.home_body_table {
  height: calc(100vh - 168px);
  border-radius: 3px;
  span {
    cursor: pointer;
    user-select: none;
    margin: 0px 10px;
  }
}
</style>
