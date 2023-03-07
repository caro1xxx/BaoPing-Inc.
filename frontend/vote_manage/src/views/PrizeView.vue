<template>
  <div class="home">
    <Search />
    <div class="home_title">礼物管理</div>
    <div class="home_body">
      <el-table :data="voteNotesData" class="home_body_table">
        <el-table-column prop="id" label="编号">
          <template #default="scope">
            <span>#{{ scope.$index }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="open_id" label="礼物名称" />
        <el-table-column prop="vote_name" label="价值/赞">
          <template #default="scope">
            <div>1</div>
          </template>
        </el-table-column>
        <el-table-column prop="ip" label="价格" />
        <el-table-column prop="phone_model" label="开关" />
        <el-table-column label="操作">
          <template #default="scope">
            <span style="color: red">删除</span>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue";
import { reactive } from "vue";
import { useStore } from "vuex";
import { fether } from "@/utils/fether";
import Cookies from "js-cookie";
const $store = new useStore();
// 投票记录数据
const voteNotesData = reactive([]);
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
