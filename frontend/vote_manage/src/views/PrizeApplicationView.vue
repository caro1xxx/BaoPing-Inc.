<template>
  <div class="home">
    <Search />
    <div class="home_title">奖品申请</div>
    <el-table :data="prizedata" class="realmlist">
      <el-table-column prop="id" label="活动" />
      <el-table-column prop="username" label="openid(用户名)" />
      <el-table-column prop="name" label="姓名" />
      <el-table-column prop="phone_number" label="手机号" />
      <el-table-column prop="create_time" label="申请时间" />
      <el-table-column prop="status" label="状态" />
      <el-table-column label="操作">
        <template #default="scope">
          <svg @click="deleterealm()" t="1677475434506" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6493" id="mx_n_1677475434509" width="20" height="20">
            <path d="M607.897867 768.043004c-17.717453 0-31.994625-14.277171-31.994625-31.994625L575.903242 383.935495c0-17.717453 14.277171-31.994625 31.994625-31.994625s31.994625 14.277171 31.994625 31.994625l0 351.94087C639.892491 753.593818 625.61532 768.043004 607.897867 768.043004z" fill="#F40606" p-id="6494">
            </path><path d="M415.930119 768.043004c-17.717453 0-31.994625-14.277171-31.994625-31.994625L383.935495 383.935495c0-17.717453 14.277171-31.994625 31.994625-31.994625 17.717453 0 31.994625 14.277171 31.994625 31.994625l0 351.94087C447.924744 753.593818 433.647573 768.043004 415.930119 768.043004z" fill="#F40606" p-id="6495">
            </path><path d="M928.016126 223.962372l-159.973123 0L768.043004 159.973123c0-52.980346-42.659499-95.983874-95.295817-95.983874L351.94087 63.989249c-52.980346 0-95.983874 43.003528-95.983874 95.983874l0 63.989249-159.973123 0c-17.717453 0-31.994625 14.277171-31.994625 31.994625s14.277171 31.994625 31.994625 31.994625l832.032253 0c17.717453 0 31.994625-14.277171 31.994625-31.994625S945.73358 223.962372 928.016126 223.962372zM319.946246 159.973123c0-17.545439 14.449185-31.994625 31.994625-31.994625l320.806316 0c17.545439 0 31.306568 14.105157 31.306568 31.994625l0 63.989249L319.946246 223.962372 319.946246 159.973123 319.946246 159.973123z" fill="#F40606" p-id="6496">
            </path><path d="M736.048379 960.010751 288.123635 960.010751c-52.980346 0-95.983874-43.003528-95.983874-95.983874L192.139761 383.591466c0-17.717453 14.277171-31.994625 31.994625-31.994625s31.994625 14.277171 31.994625 31.994625l0 480.435411c0 17.717453 14.449185 31.994625 31.994625 31.994625l448.096758 0c17.717453 0 31.994625-14.277171 31.994625-31.994625L768.215018 384.795565c0-17.717453 14.277171-31.994625 31.994625-31.994625s31.994625 14.277171 31.994625 31.994625l0 479.231312C832.032253 916.835209 789.028725 960.010751 736.048379 960.010751z" fill="#F40606" p-id="6497">
            </path></svg>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue"
import { fether } from "@/utils/fether"
import { reactive } from "vue"
import { useStore } from "vuex"
import Cookies from 'js-cookie'
const $store = new useStore()

// 奖品申请数据
const prizedata = reactive([])

// 获取奖品列表
const getprize = async () => {
  //开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(
    `/applyprize/?token=${Cookies.get('token')}`
  )
  if (result.code === 200) {
    prizedata.push(...result.data)
  } else {
    //请求发送错误
    await $store.dispatch("refreshErroActions");
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
  //关闭加载loading
  $store.commit("noticifyLoading", false);
}
getprize()

// 将时间戳转换
const gettime = (value) => {
  let Time = new Date()
  let y = Time.getFullYear(value)
  let m = Time.getMonth(value) + 1
  let d = Time.getDate(value)
  let h = Time.getHours(value)
  let M = Time.getMinutes(value)
  let s = Time.getSeconds(value)
  let str = ''
  str = `${y}/${zroon(m)}/${zroon(d)} ${zroon(h)}:${zroon(M)}:${zroon(s)}`
  return str
}
// 补零
const zroon = (number) => {
  if (number < 10) {
    return `0${number}`
  } else {
    return number
  }
}

// 状态改变
const changestatus = async  (value, index) => {
  //开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/applyprize/`, `put`, {
    token: Cookies.get("token"),
    status: value.status,
    apply_prize_id: value.apply_prize_id
  })
  if (result.code === 200) {
    prizedata[index].status = !prizedata[index].status
  }
  await $store.dispatch("GlobalMessageActions", result.msg);
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
}

// 删除奖品数据
const deleteprize = async () => {
  //开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/applyprize/`, `delete`, {
    token: Cookies.get("token"),
    apply_prize_id: value.apply_prize_id
  })
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
.realmlist{
  height: calc(100vh - 148px);
  margin-top: 10px;
  border-radius: 3px;
}
</style>
