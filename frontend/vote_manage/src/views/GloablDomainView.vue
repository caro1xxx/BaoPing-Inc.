<template>
  <div class="home">
    <Search />
    <div class="home_title">全局域名</div>
    <div class="home_body">
      <el-button text @click="openDialog()">
        <svg t="1677473562522" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2330" width="20" height="20">
        <path d="M512 992C246.912 992 32 777.088 32 512 32 246.912 246.912 32 512 32c265.088 0 480 214.912 480 480 0 265.088-214.912 480-480 480z m0-64c229.76 0 416-186.24 416-416S741.76 96 512 96 96 282.24 96 512s186.24 416 416 416z" fill="#2460E5" p-id="2331"></path>
        <path d="M256 544a32 32 0 0 1 0-64h512a32 32 0 0 1 0 64H256z" fill="#2460E5" p-id="2332"></path>
        <path d="M480 256a32 32 0 0 1 64 0v512a32 32 0 0 1-64 0V256z" fill="#2460E5" p-id="2333"></path></svg>
      </el-button>
    </div>
    <el-table :data="realmAddData" class="home_body_table">
      <el-table-column prop="id" label="编号" />
      <el-table-column prop="domain_name" label="域名" />
      <el-table-column prop="expire_time" label="有效期">
        <template #default="scope">
          <span>{{ parseStampTime(scope.row.expire_time) }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="createdtime" label="创建时间" />
      <el-table-column prop="status" label="状态" />
      <el-table-column label="操作">
        <template #default="scope">
          <svg @click="deleteRealm(scope.row, scope.$index)" t="1677475434506" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6493" id="mx_n_1677475434509" width="20" height="20">
            <path d="M607.897867 768.043004c-17.717453 0-31.994625-14.277171-31.994625-31.994625L575.903242 383.935495c0-17.717453 14.277171-31.994625 31.994625-31.994625s31.994625 14.277171 31.994625 31.994625l0 351.94087C639.892491 753.593818 625.61532 768.043004 607.897867 768.043004z" fill="#F40606" p-id="6494">
            </path><path d="M415.930119 768.043004c-17.717453 0-31.994625-14.277171-31.994625-31.994625L383.935495 383.935495c0-17.717453 14.277171-31.994625 31.994625-31.994625 17.717453 0 31.994625 14.277171 31.994625 31.994625l0 351.94087C447.924744 753.593818 433.647573 768.043004 415.930119 768.043004z" fill="#F40606" p-id="6495">
            </path><path d="M928.016126 223.962372l-159.973123 0L768.043004 159.973123c0-52.980346-42.659499-95.983874-95.295817-95.983874L351.94087 63.989249c-52.980346 0-95.983874 43.003528-95.983874 95.983874l0 63.989249-159.973123 0c-17.717453 0-31.994625 14.277171-31.994625 31.994625s14.277171 31.994625 31.994625 31.994625l832.032253 0c17.717453 0 31.994625-14.277171 31.994625-31.994625S945.73358 223.962372 928.016126 223.962372zM319.946246 159.973123c0-17.545439 14.449185-31.994625 31.994625-31.994625l320.806316 0c17.545439 0 31.306568 14.105157 31.306568 31.994625l0 63.989249L319.946246 223.962372 319.946246 159.973123 319.946246 159.973123z" fill="#F40606" p-id="6496">
            </path><path d="M736.048379 960.010751 288.123635 960.010751c-52.980346 0-95.983874-43.003528-95.983874-95.983874L192.139761 383.591466c0-17.717453 14.277171-31.994625 31.994625-31.994625s31.994625 14.277171 31.994625 31.994625l0 480.435411c0 17.717453 14.449185 31.994625 31.994625 31.994625l448.096758 0c17.717453 0 31.994625-14.277171 31.994625-31.994625L768.215018 384.795565c0-17.717453 14.277171-31.994625 31.994625-31.994625s31.994625 14.277171 31.994625 31.994625l0 479.231312C832.032253 916.835209 789.028725 960.010751 736.048379 960.010751z" fill="#F40606" p-id="6497">
            </path></svg>
            <el-button @click="undataData(scope.row, scope.$index)" type="primary">编辑</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue"
import { fether } from "@/utils/fether"
import { reactive,watch } from "vue"
import {  useStore } from "vuex"
import { parseStampTime } from '../utils/stampTime'
import Cookies from 'js-cookie'
const $store = new useStore()

// 域名管理数据
const realmAddData = reactive([])

// 获取域名列表
const getRealm = async () => {
  //开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(
    `/domain/?token=${Cookies.get('token')}`
  )
  if (result.code === 200) {
    let Arr = []
    Arr = JSON.parse(result.data)
    Arr.map(item => {
      realmAddData.push(item.fields)
    })
  } else {
    //请求发送错误
    await $store.dispatch("refreshErroActions");
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
  //关闭加载loading
  $store.commit("noticifyLoading", false);
}
getRealm()
// 编辑数据
const undataData = async (value, index) => {
  value.key = true
  value.index = index
  $store.commit('undateRealmStatus', value)
}

// 删除域名列表数据
const deleteRealm = async (value, index) => {
  //开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/domain/`, `delete`, {
    domain: value.domain_name,
    token: Cookies.get("token"),
  })
  if (result.code === 200) {
    // 删除本地数据
    realmAddData.splice(index, 1)
  }
  await $store.dispatch("GlobalMessageActions", result.msg);
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
}
watch(
  () => $store.state.realmData,
  (newVal) => {
    if (newVal.key) {
      realmAddData[newVal.index].domain_name = newVal.domain_name,
      realmAddData[newVal.index].expire_time = newVal.expire_time,
      realmAddData[newVal.index].status = newVal.status
    } else if (newVal.domain_name) {
      // 新增时状态默认为1
      newVal.status = 1
      realmAddData.push(newVal)
    }
  },
  {
    deep: true
  }
)

// 开启弹窗
const openDialog = () => {
  // key为判断是否为新增或编辑的钥匙  true为编辑false为新增
 $store.commit('undateRealmStatus', {
  key: false
 })
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
.home_body{
  display: flex;
  justify-content: flex-end;
}
.home_body,svg{
  cursor: pointer;
}
svg{
  margin-right: 15px;
}
.home_body_table{
  height: calc(100vh - 178px);
  margin-top: 10px;
  border-radius: 3px;
}
.home_body_table::-webkit-scrollbar {
  display: none;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}
</style>
