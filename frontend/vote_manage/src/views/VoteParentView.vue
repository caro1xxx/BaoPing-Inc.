<template>
  <div class="home">
    <Search />
    <div class="home_title">投票选手</div>
    <div class="home_table_wrap">
      <el-table :data="athleteData" class="home_table">
        <el-table-column prop="id" label="编号">
          <template #default="scope">
            <span>{{ scope.$index }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="wx_username" label="openid(用户名)" />
        <el-table-column prop="avator" label="姓名" />
        <el-table-column prop="open_id" label="open_id" />
        <el-table-column prop="create_time" label="申请时间">
          <template #default="scope">
            <span>{{ getTime(scope.row.create_time) }}</span>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue"
import { fether } from "@/utils/fether"
import { reactive } from "vue"
import Cookies from 'js-cookie'

//投票选手数据
const athleteData = reactive([])

//获取投票选手信息
const getAthleteData = async () => {
  let result = await fether(`/voteuser/?token=${Cookies.get('token')}`)
  if (result.code === 200) {
    let Arr = []
    Arr = JSON.parse(result.data)
    console.log(Arr);
    Arr.map(item => {
      athleteData.push({...item.fields, pk: item.pk})
    })
  }
}
getAthleteData()

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
}
</style>
