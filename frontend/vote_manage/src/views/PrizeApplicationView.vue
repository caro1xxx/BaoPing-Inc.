<template>
  <div class="home">
    <Search />
    <div class="home_title">奖品申请</div>
    <div class="home_table_wrap">
      <el-table :data="prizeData" class="home_table">
        <el-table-column prop="id" label="活动">
          <template #default="scope">
            <span>{{ scope.$index }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="wx_username" label="openid(用户名)" />
        <el-table-column prop="name" label="姓名" />
        <el-table-column prop="phone_number" label="手机号" />
        <el-table-column prop="create_time" label="申请时间">
          <template #default="scope">
            <span>{{ getTime(scope.row.create_time) }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="status" label="状态" />
        <el-table-column label="操作">
          <template #default="scope">
            <span @click="deletePrize(scope.row, scope.$index)" style="color: red;">删除</span>
            <span @click="undataData(scope.row, scope.$index)" style="color: #409eff;">编辑</span>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue"
import { fether } from "@/utils/fether"
import { reactive, watch } from "vue"
import { useStore } from "vuex"
import Cookies from 'js-cookie'
const $store = new useStore()

// 奖品申请数据
const prizeData = reactive([])

// 获取奖品列表
const getPrize = async () => {
  //开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(
    `/applyprize/?token=${Cookies.get('token')}`
  )
  if (result.code === 200) {
    let Arr = []
    Arr = JSON.parse(result.data)
    let newObj = {}
    for (let i = 0; i < Arr.length; i++) {
      newObj.create_time = Arr[i].fields.create_time,
      newObj.name = Arr[i].fields.name,
      newObj.phone_number = Arr[i].fields.phone_number,
      newObj.status = Arr[i].fields.status,
      newObj.open_id = Arr[i].fields.voteuser.open_id,
      newObj.wx_username = Arr[i].fields.voteuser.wx_username,
      newObj.pk = Arr[i].pk
      prizeData.push(newObj)
    }
  } else {
    //请求发送错误
    await $store.dispatch("refreshErroActions");
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
  //关闭加载loading
  $store.commit("noticifyLoading", false);
}
getPrize()

// 编辑
const undataData = async  (value, index) => {
  value.index = index
  $store.commit('changePrizeStatus', value)
}

// 删除奖品数据
const deletePrize = async (value, index) => {
  //开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/applyprize/`, `delete`, {
    token: Cookies.get("token"),
    pk: value.pk
  })
  if (result.code === 200) {
    // 删除本地数据
    prizeData.splice(index, 1)
  }
  await $store.dispatch("GlobalMessageActions", result.msg);
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
}

const getTime = (value)=> {
  let d = new Date(value * 1000)
  return `${d.getFullYear()}/${d.getMonth() + 1}/${d.getDate()} ${d.getHours()}:${d.getMinutes()}`;
}


watch(
  () => $store.state.prizeData,
  (newVal) => {
      prizeData[newVal.index].wx_username = newVal.wx_username,
      prizeData[newVal.index].name = newVal.name,
      prizeData[newVal.index].phone_number = newVal.phone_number,
      prizeData[newVal.index].create_time = newVal.create_time,
      prizeData[newVal.index].status = newVal.status
  },
  {
    deep: true
  }
)
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
.home_table_wrap{
  padding: 10px;
  background-color: #fff;
}
.home_table{
  height: calc(100vh - 178px);
  margin-top: 10px;
  border-radius: 3px;
  span{
    cursor: pointer;
    user-select: none;
    margin: 0px 10px;
  }
}
svg{
  margin-right: 15px;
}
</style>
