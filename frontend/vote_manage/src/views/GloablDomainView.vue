<template>
  <div class="home">
    <Search />
    <div class="home_title">
      <span>全局域名</span>
        <svg
        @click="openDialog"
        t="1677544620358"
        class="icon add"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="1501"
        width="25"
        height="25"
      >
        <path
          d="M514.048 62.464q93.184 0 175.616 35.328t143.872 96.768 96.768 143.872 35.328 175.616q0 94.208-35.328 176.128t-96.768 143.36-143.872 96.768-175.616 35.328q-94.208 0-176.64-35.328t-143.872-96.768-96.768-143.36-35.328-176.128q0-93.184 35.328-175.616t96.768-143.872 143.872-96.768 176.64-35.328zM772.096 576.512q26.624 0 45.056-18.944t18.432-45.568-18.432-45.056-45.056-18.432l-192.512 0 0-192.512q0-26.624-18.944-45.568t-45.568-18.944-45.056 18.944-18.432 45.568l0 192.512-192.512 0q-26.624 0-45.056 18.432t-18.432 45.056 18.432 45.568 45.056 18.944l192.512 0 0 191.488q0 26.624 18.432 45.568t45.056 18.944 45.568-18.944 18.944-45.568l0-191.488 192.512 0z"
          p-id="1502"
          fill="#2460e5"
        ></path>
      </svg>
    </div>
    <div class="home_body_table_wrap">
      <el-table :data="realmAddData" class="home_body_table">
      <el-table-column prop="id" label="编号" >
        <template #default="scope">
          <span>{{ scope.$index }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="domain_name" label="域名" />
      <el-table-column prop="expire_time" label="有效期">
        <template #default="scope">
          <span v-if="scope.row.expire_time">{{ getTime(scope.row.expire_time) }}</span>
        </template>
      </el-table-column>
      <el-table-column prop="status" label="状态" />
      <el-table-column label="操作">
        <template #default="scope">
            <span @click="deleteRealm(scope.row, scope.$index)" style="color: red;">删除</span>
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
import { reactive,watch } from "vue"
import {  useStore } from "vuex"
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
      realmAddData.push({...item.fields})
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

const getTime = (value)=> {
  if (value === 0) {
    return '1970/1/1 0:0'
  } else if (String(value).length > 10) {
    let d = new Date(value)
    return `${d.getFullYear()}/${d.getMonth() + 1}/${d.getDate()} ${d.getHours()}:${d.getMinutes()}`;
  } else {
    let d = new Date(value * 1000)
    return `${d.getFullYear()}/${d.getMonth() + 1}/${d.getDate()} ${d.getHours()}:${d.getMinutes()}`;
  }
}

watch(
  () => $store.state.realmData,
  (newVal) => {
    if (newVal.key) {
      realmAddData[newVal.index].domain_name = newVal.domain_name,
      realmAddData[newVal.index].expire_time = newVal.expire_time,
      realmAddData[newVal.index].status = newVal.status
    } else if (newVal.domain_name) {
      realmAddData.push({
        domain_name: newVal.domain_name,
        expire_time: newVal.expire_time,
        status: newVal.status,
      })
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
  display: flex;
  justify-content: space-between;
  align-items: center;
  span,svg{    
    cursor: pointer;
    user-select: none;
  }
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
  height: calc(100vh - 168px);
  border-radius: 3px;
  span{
    cursor: pointer;
    user-select: none;
    margin: 0px 10px;
  }
}
.home_body_table::-webkit-scrollbar {
  display: none;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}
.home_body_table_wrap{
  padding: 10px;
  background-color: white;
}
</style>
