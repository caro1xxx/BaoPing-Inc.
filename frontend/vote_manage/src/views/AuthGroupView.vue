
<template>
  <div class="limits_main">
    <div class="limits_main_body">
      <Search />
      <div class="title_style">权限分组</div>
      <div class="limits_table">
        <div class="limits_table_head">
          <div v-for="item in limitsheated" :key="item.name">{{ item.name }}</div>
        </div>
        <div class="limits_table_body_wrap">
          <div class="limits_table_body" v-for="item in linmitsdata" :key="item.Id">
            <div>{{ item.Id }}</div>
            <div>{{ item.username }}</div>
            <div>{{ item.creatId }}</div>
            <div>{{ item.creattime }}</div>
            <div>{{ item.updatetime }}</div>
            <div class="limits_table_operatebox">
              <span>编辑</span>
              <span>删除</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue";
import { reactive } from "vue";

// 权限分组表头数据
const limitsheated = reactive([
  {name: 'ID'},
  {name: '账户'},
  {name: '创建ID'},
  {name: '创建时间'},
  {name: '更新时间'},
  {name: '操作'}
])

// 权限分组数据
const linmitsdata = reactive([
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
  {Id: '890',username: '李华', creatId: '1111',creattime: '2022-10-13 21:11:36', updatetime: '2023-01-01 10:11:24'},
])

</script>

<style lang="scss" scoped>
.limits_main {
  width: calc(100vw - 200px);
  height: calc(100vh);
  font-size: 20px;
  font-weight: 50px;
}
.limits_main_body {
  margin: 20px 20px;
}
.limits_table {
  border: 1px solid #b5c3d178;
  border-radius: 10px;
  height: calc(100vh - 180px);
  margin-top: 20px;
}
.limits_table_head {
  user-select: none;
  border-radius: 10px 10px 0px 0px;
  height: 40px;
  border-bottom: 1px solid #b5c3d178;
  box-shadow: 0 4px 4px 0 #bababa21;
  display: flex;
  div {
    flex: 1;
    text-align: center;
    line-height: 40px;
    font-size: 15px;
    font-weight: lighter;
  }
  cursor: pointer;
}
.limits_table_body {
  display: flex;
  div {
    flex: 1;
    text-align: center;
    font-size: 14px;
    font-weight: lighter;
    color: #585858;
    margin: 10px 0px;
  }
  .limits_table_operatebox{
    display: flex;
    justify-content: center;
    color: #188CFF;
    span{
      margin: 0px 10px;
    }
  }
}
.limits_table_body_wrap {
  height: calc(100vh - 322px);
  overflow-y: scroll;
}
.limits_table_body_wrap::-webkit-scrollbar {
  display: none;
}
</style>
