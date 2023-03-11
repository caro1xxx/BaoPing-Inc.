<template>
  <div class="home">
    <Search />
    <div class="home_title">
      <span>礼物管理</span>
      <svg
        @click="$store.commit('changeGiftAdd')"
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

    <div class="home_body">
      <el-table :data="voteNotesData" class="home_body_table">
        <el-table-column prop="id" label="编号">
          <template #default="scope">
            <span>#{{ scope.$index }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="name" label="礼物名称" />
        <el-table-column prop="value" label="价值/赞">
          <template #default="scope">
            <div>{{ scope.row.value }}个赞</div>
          </template>
        </el-table-column>
        <el-table-column prop="price" label="价格" />
        <el-table-column prop="status" label="开关">
          <template #default="scope">
            <el-switch
              :model-value="scope.row.status === 1 ? true : false"
              @change="changeGiftState(scope.row.name)"
            />
            <!-- <div>{{ scope.row.status === 1 ? "开" : "关" }}</div> -->
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template #default="scope">
            <span style="color: red" @click="deleteGift(scope.row)">删除</span>
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
import jsCookie from "js-cookie";
const $store = new useStore();
// 投票记录数据
const voteNotesData = reactive([]);

// 获取礼物列表
const getGift = async () => {
  // 开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/gift/?token=${Cookies.get("token")}`);
  if (result.code === 200) {
    let JSONResult = JSON.parse(result.data);
    JSONResult.forEach((item) => {
      voteNotesData.push({ ...item.fields, pk: item.pk });
    });
  } else {
    // 请求发送错误
    await $store.dispatch("refreshErroActions");
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
};

getGift();

// 删除礼物
const deleteGift = async (target) => {
  let result = await fether(`/gift/`, "delete", {
    token: Cookies.get("token"),
    pk: target.pk,
  });
  if (result.code === 200) {
    voteNotesData.forEach((item, inde) => {
      if (item.pk === target.pk) {
        voteNotesData.splice(inde, 1);
      }
    });
    await $store.dispatch("GlobalMessageActions", "删除成功");
  } else {
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
};

// 改变礼物状态
const changeGiftState = async (name) => {
  for (let i = 0; i < voteNotesData.length; i++) {
    if (voteNotesData[i].name === name) {
      voteNotesData[i].status = voteNotesData[i].status ? 0 : 1;
      let result = await fether("/gift/", "put", {
        data: { ...voteNotesData[i] },
        token: jsCookie.get("token"),
      });
      await $store.dispatch("GlobalMessageActions", result.msg);
      break;
    }
  }
};

watch(
  () => $store.state.giftAdd.value,
  (newVal) => {
    voteNotesData.push({
      ...$store.state.giftAdd.value,
      status: parseInt($store.state.giftAdd.value.status),
    });
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
  display: flex;
  justify-content: space-between;
  align-items: center;
  span,
  svg {
    cursor: pointer;
    user-select: none;
  }
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
