<template>
  <div class="home">
    <Search />
    <div class="home_title">投票记录</div>
    <div class="home_body">
      <el-table :data="voteNotesData" class="home_body_table">
        <el-table-column prop="id" label="编号">
          <template #default="scope">
            <span>{{ scope.$index }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="wx_username" label="openid(用户名)" />
        <el-table-column prop="vote_name" label="票数">
          <template #default="scope">
            <span>1</span>
          </template>
        </el-table-column>
        <el-table-column prop="ip" label="ip" />
        <el-table-column prop="phone_model" label="手机型号" />
        <el-table-column prop="system" label="系统" />
        <el-table-column prop="network" label="网络" />
        <el-table-column label="操作">
          <template #default="scope">
            <span style="color: red;" @click="deleteVote(scope.row, scope.$index)">删除</span>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue"
import { reactive } from "vue"
import { useStore } from "vuex"
import { fether } from '@/utils/fether'
import Cookies from 'js-cookie'
const $store = new useStore()
// 投票记录数据
const voteNotesData = reactive([

])
// 获取投票记录数据
const getVoteData = async () => {
  // 开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(
    `/voterecord/?token=${Cookies.get('token')}`
  )
  if (result.code === 200) {
    let Arr = []
    Arr = JSON.parse(result.data)
    let newObj = {}
    for (let i = 0; i < Arr.length; i++) {
      newObj.wx_username = Arr[i].fields.voteuser.wx_username,
      newObj.open_id = Arr[i].fields.voteuser.open_id,
      newObj.ip = Arr[i].fields.ip,
      newObj.phone_model = Arr[i].fields.phone_model,
      newObj.system = Arr[i].fields.system,
      newObj.network = Arr[i].fields.network,
      newObj.pk = Arr[i].pk
      voteNotesData.push(newObj)
    }
  } else {
    // 请求发送错误
    await $store.dispatch("refreshErroActions");
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
}
getVoteData()

// 删除投票记录
const deleteVote = async (value, index) => {
  //开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/voterecord/`, `delete`, {
    pk: value.pk,
    token: Cookies.get("token"),
  })
  if (result.code === 200) {
    // 删除本地数据
    voteNotesData.splice(index, 1)
  }
  await $store.dispatch("GlobalMessageActions", result.msg);
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
}
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
svg{
  cursor: pointer;
}
.home_body{
  padding: 10px;
  background-color: #fff;
}
.home_body_table{
  height: calc(100vh - 168px);
  border-radius: 3px;
  span{
    cursor: pointer;
    user-select: none;
    margin: 0px 10px;
  }
}
</style>
