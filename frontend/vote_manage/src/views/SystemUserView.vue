<template>
  <div class="system_main">
    <div class="system_main_body">
      <Search />
      <div class="title_style" @click="editUser">系统用户</div>
      <div class="home_table">
        <div class="home_table_head">
          <div v-for="item in tableHead" :key="item.name">{{ item.name }}</div>
        </div>
        <div class="home_table_body_wrap">
          <div
            class="home_table_body"
            v-for="(item, index) in tableData"
            :key="index"
          >
            <div class="home_table_body_index">{{ "#" + index }}</div>
            <div>{{ item.username }}</div>
            <div>{{ item.name }}</div>
            <div>{{ item.auth }}</div>
            <div>{{ item.create_time }}</div>
            <div>{{ item.last_login_time }}</div>
            <div>{{ item.email }}</div>
            <div>{{ item.status }}</div>
            <div>
              <span
                class="home_table_body_handle"
                @click="editUserShowPopup({ ...item })"
                >修改</span
              ><span
                class="home_table_body_handle"
                @click="deleteUser(item.username)"
                >删除</span
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue";
import { fether } from "@/utils/fether";
import { reactive, watch } from "vue";
import { useStore } from "vuex";
import Cookies from "js-cookie";
const $store = new useStore();
// 表头
const tableHead = reactive([
  { name: "编号" },
  { name: "用户" },
  { name: "姓名" },
  { name: "权限" },
  { name: "创建时间" },
  { name: "最后登录时间" },
  { name: "邮箱" },
  { name: "状态" },
  { name: "操作" },
]);
// 表数据
const tableData = reactive([]);

// 获取用户信息
const getUserInfoList = async () => {
  // 开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(
    // 获取vuex中的username
    `/userinfo/?username=${$store.state.userInfo.username}&token=${Cookies.get(
      "token"
    )}`
  );
  if (result.code === 200) {
    let JSONResult = await JSON.parse(result.data);
    JSONResult.forEach((item) => {
      tableData.push(item.fields);
    });
  } else {
    await $store.dispatch("GlobalMessageActions", "获取失败,请刷新");
  }
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
};

// 删除用户
const deleteUser = async (target) => {
  // 开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/userinfo/`, "delete", {
    username: target,
    token: Cookies.get("token"),
  });
  if (result.code === 200) {
    for (let i = 0; i < tableData.length; i++) {
      if (tableData[i].username === target) {
        tableData.splice(i, 1);
        break;
      }
    }
  }
  await $store.dispatch("GlobalMessageActions", result.msg);
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
};

// 修改用户显示界面
const editUserShowPopup = async (target) => {
  await $store.dispatch("editUserActions", target);
};

// 提交修改用户
const saveUserEdit = async (target) => {
  // 开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/userinfo/`, "put", {
    data: {
      name: target.name,
      auth: target.auth,
      pwd: target.pwd,
      status: target.status,
      username: target.username,
    },
    token: Cookies.get("token"),
  });
  if (result.code === 200) {
    for (let i = 0; i < tableData.length; i++) {
      if (tableData[i].username === target.username) {
        tableData[i] = target;
      }
    }
  }
  await $store.dispatch("GlobalMessageActions", result.msg);
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
};

watch(
  () => $store.state.isUserEditSave,
  (newVal) => {
    saveUserEdit($store.state.editPopProps);
  }
);

getUserInfoList();
</script>

<style lang="scss" scoped>
.system_main {
  width: calc(100vw - 200px);
  height: calc(100vh);
  font-size: 20px;
}
.system_main_body {
  margin: 20px 20px;
}

.home_table {
  border: 1px solid #b5c3d178;
  border-radius: 10px;
  height: calc(100vh - 190px);
  margin-top: 20px;
  position: relative;
}
.home_table_head {
  user-select: none;
  border-radius: 10px 10px 0px 0px;
  height: 40px;
  border-bottom: 1px solid #b5c3d178;
  box-shadow: 0 4px 4px 0 #bababa21;
  display: flex;
  div {
    width: 11.111%;
    text-align: center;
    line-height: 40px;
    font-size: 15px;
    font-weight: lighter;
  }
  cursor: pointer;
}
.home_table_body {
  display: flex;
  div {
    width: 11.111%;
    text-align: center;
    font-size: 14px;
    font-weight: lighter;
    color: #585858;
    margin: 10px 0px;
  }
}
.home_table_body_item {
  cursor: pointer;
}
.home_table_body_index {
  font-style: italic;
  color: #4597e8 !important;
}
.home_table_body_handle {
  color: #4597e8 !important;
  margin: 0px 10px;
  cursor: pointer;
  user-select: none;
}
.home_table_body_wrap {
  height: calc(100vh - 230px);
  overflow: scroll;
}
</style>
