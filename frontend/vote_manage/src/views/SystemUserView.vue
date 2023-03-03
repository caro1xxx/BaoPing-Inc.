<template>
  <div class="system_main">
    <div class="system_main_body">
      <Search />
      <div class="title_style" @click="editUser">系统用户</div>
      <div class="home_table">
        <div class="home_table_grid">
          <div
            v-for="(item, index) in tableData"
            class="home_table_item"
            :style="{ backgroundColor: item.status ? '#fff' : '#e9e9e9' }"
            @mouseenter="onClickMove(index, true)"
            @mouseleave="onClickMove(index, false)"
          >
            <div class="home_table_item_top">
              <img :src="HOST + '/media/avator/' + item.avator + '.png'" />
              <div>{{ item.name }}</div>
            </div>
            <div>邮箱:{{ item.email }}</div>
            <div style="margin-top: 5px; color: #cecece; font-size: 10px">
              最近登录:{{ item.last_login_time }}
            </div>
            <div class="home_table_item_move" v-show="item.isMove">
              <svg
                @click="editUserShowPopup({ ...item })"
                t="1677328515708"
                class="icon"
                viewBox="0 0 1024 1024"
                version="1.1"
                xmlns="http://www.w3.org/2000/svg"
                p-id="13403"
                width="30"
                height="30"
              >
                <path
                  d="M512 512m-512 0a512 512 0 1 0 1024 0 512 512 0 1 0-1024 0Z"
                  fill="#FDEBED"
                  p-id="13404"
                ></path>
                <path
                  d="M665.6 729.6H358.4c-28.16 0-51.2-23.04-51.2-51.2V345.6c0-28.16 23.04-51.2 51.2-51.2h285.44L455.68 483.84v72.96h71.68L716.8 367.36V678.4c0 28.16-23.04 51.2-51.2 51.2zM508.16 538.88h-35.84v-35.84l198.4-198.4c10.24-10.24 25.6-10.24 35.84 0 10.24 10.24 10.24 25.6 0 35.84L508.16 538.88z"
                  fill="#EC3A4E"
                  p-id="13405"
                ></path>
              </svg>
              <svg
                @click="deleteUser(item.username)"
                t="1677328484608"
                class="icon"
                viewBox="0 0 1024 1024"
                version="1.1"
                xmlns="http://www.w3.org/2000/svg"
                p-id="10871"
                width="30"
                height="30"
              >
                <path
                  d="M512 512m-512 0a512 512 0 1 0 1024 0 512 512 0 1 0-1024 0Z"
                  fill="#FDEBED"
                  p-id="10872"
                ></path>
                <path
                  d="M729.6 384H294.4c-7.68 0-12.8-5.12-12.8-12.8v-25.6c0-7.68 5.12-12.8 12.8-12.8h115.2v-25.6c0-14.08 11.52-25.6 25.6-25.6h153.6c14.08 0 25.6 11.52 25.6 25.6v25.6h115.2c7.68 0 12.8 5.12 12.8 12.8v25.6c0 7.68-5.12 12.8-12.8 12.8z m-371.2 38.4h307.2c28.16 0 51.2 23.04 51.2 51.2v217.6c0 28.16-23.04 51.2-51.2 51.2H358.4c-28.16 0-51.2-23.04-51.2-51.2V473.6c0-28.16 23.04-51.2 51.2-51.2z m192 243.2c0 7.68 5.12 12.8 12.8 12.8s12.8-5.12 12.8-12.8V537.6c0-7.68-5.12-12.8-12.8-12.8s-12.8 5.12-12.8 12.8v128z m-102.4 0c0 7.68 5.12 12.8 12.8 12.8s12.8-5.12 12.8-12.8V537.6c0-7.68-5.12-12.8-12.8-12.8s-12.8 5.12-12.8 12.8v128z"
                  fill="#EC3A4E"
                  p-id="10873"
                ></path>
              </svg>
            </div>
            <svg
              v-if="item.auth"
              t="1677327580968"
              class="icon home_table_item_auth"
              viewBox="0 0 1024 1024"
              version="1.1"
              xmlns="http://www.w3.org/2000/svg"
              p-id="5629"
              width="20"
              height="20"
            >
              <path
                d="M898.34 188.81L538.35 74.51l-359.87 114.3c-13.53 4.27-22.67 16.86-22.55 31.1v454.94c0.72 3.09 17.69 77.98 91.27 150.5 56.61 55.78 192.4 127.48 251.63 158.57 9.25 4.87 13.65 6.65 17.56 8.78l17.57 8.78c4.63 2.49 12.94 2.38 17.57 0l17.57-8.78c34.65-16.97 195-102.9 260.4-167.35 73.71-72.52 90.68-147.41 91.39-150.5V219.91c0.23-14.24-9.02-26.83-22.55-31.1zM542.86 930.98l-0.24-0.12h0.59c-0.23 0.12-0.35 0.12-0.35 0.12z m85.81-264.32h-58.16v81.9c0 18.99-15.43 34.42-34.42 34.42-18.99 0-34.42-15.43-34.42-34.42V537.29c0-0.71 0.12-1.3 0.12-1.9-6.29-1.9-12.58-4.16-18.87-7-21.24-9.73-39.4-27.18-51.51-47-12.58-20.65-19.23-46.53-17.21-70.74 2.37-27.65 12.34-51.75 30.03-73.23 30.62-37.15 86.88-52.22 131.98-35.73 25.52 9.38 46.29 25.05 61.96 47.12 13.77 19.35 20.77 43.44 21.37 67.06 0 0.71 0.12 1.3 0 2.02 0 0.83 0 1.66-0.12 2.49-1.66 52.46-37.74 101.95-89.02 115.61v60.41h58.16c18.99 0 34.42 15.43 34.42 34.42v1.42h0.12c-0.01 18.99-15.44 34.42-34.43 34.42z"
                fill="#2460e5"
                p-id="5630"
              ></path>
              <path
                d="M577.99 449.1c0.35-0.59 0.71-1.07 0.83-1.19a97.38 97.38 0 0 0 5.58-9.74c1.54-4.39 2.73-8.78 3.68-13.41 0.12-2.25 0.24-4.63 0.36-6.89 0-2.26-0.12-4.63-0.36-6.88-0.83-4.51-2.14-9.02-3.68-13.41a108.73 108.73 0 0 0-4.51-8.19c-0.36-0.36-1.19-1.54-2.61-3.8-1.3-1.43-2.61-2.97-4.03-4.27-1.66-1.66-3.44-3.32-5.34-4.87-0.59-0.35-1.06-0.71-1.19-0.83a97.226 97.226 0 0 0-9.73-5.58c-4.39-1.54-8.78-2.73-13.29-3.68-4.63-0.35-9.26-0.35-13.89 0-4.51 0.83-9.02 2.14-13.29 3.68a108.73 108.73 0 0 0-8.19 4.51c-0.36 0.36-1.54 1.19-3.8 2.61-1.43 1.3-2.97 2.61-4.27 4.03-1.66 1.66-3.32 3.44-4.87 5.34-0.35 0.59-0.71 1.07-0.83 1.19a97.226 97.226 0 0 0-5.58 9.73c-1.54 4.39-2.73 8.78-3.68 13.29-0.35 4.63-0.35 9.26 0 13.89 0.83 4.51 2.14 9.02 3.68 13.29 1.42 2.85 2.85 5.46 4.51 8.19 0.36 0.36 1.19 1.54 2.61 3.8 1.3 1.43 2.61 2.97 4.03 4.27 1.66 1.66 3.44 3.32 5.34 4.87 0.59 0.35 1.07 0.71 1.19 0.83 3.08 2.02 6.41 3.92 9.73 5.58 4.39 1.54 8.78 2.73 13.29 3.68 4.63 0.36 9.26 0.36 13.89 0 4.51-0.83 9.02-2.14 13.29-3.68 2.85-1.42 5.46-2.85 8.19-4.51 0.36-0.36 1.54-1.19 3.8-2.61 1.54-1.19 2.97-2.49 4.27-3.92 1.67-1.64 3.33-3.42 4.87-5.32z"
                fill="#2460e5"
                p-id="5631"
              ></path>
            </svg>
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
import { HOST } from "@/ENV";
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
    `/userinfo/?username=${Cookies.get("username")}&token=${Cookies.get(
      "token"
    )}`
  );
  isAxiosStatus(result, true)

  // 关闭加载loading
  $store.commit("noticifyLoading", false);
};

const isAxiosStatus = async (data, status) => {
  if (status === false) {
    tableData.splice(0, tableData.length)
  }
  if (data.code === 200) {
    //serve
    let JSONResult = await JSON.parse(data.data);
    JSONResult.forEach((item) => {
      tableData.push(item.fields);
    });
  } else {
    // 请求发送错误
    await $store.dispatch("refreshErroActions");
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
}

// 删除用户
const deleteUser = async (target) => {
  // 开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(
    `/userinfo/`,
    "delete",
    {
      username: target,
      token: Cookies.get("token"),
    },
    $store.state.userInfo.name,
    "系统用户"
  );
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
  let result = await fether(
    `/userinfo/`,
    "put",
    {
      data: {
        name: target.name,
        auth: target.auth,
        status: target.status,
        username: target.username,
      },
      token: Cookies.get("token"),
    },
    $store.state.userInfo.name,
    "系统用户"
  );
  if (result.code === 200) {
    for (let i = 0; i < tableData.length; i++) {
      if (tableData[i].username === target.username) {
        tableData[i].username = target.username;
        tableData[i].pwd = target.pwd;
        tableData[i].name = target.name;
        tableData[i].auth = target.auth;
        tableData[i].status = target.status;
      }
    }
  }
  await $store.dispatch("GlobalMessageActions", result.msg);
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
};

// 鼠标移入移出
const onClickMove = async (index, type) => {
  tableData[index].isMove = type;
};
// 鼠标移出

watch(
  () => $store.state.isUserEditSave,
  (newVal) => {
    saveUserEdit($store.state.editPopProps);
  }
);

// 监听筛选数据
watch(
  () => $store.state.filterData,
  (newVal) => {
    isAxiosStatus(newVal, false)
  },
)

getUserInfoList();
</script>

<style lang="scss" scoped>
.system_main {
  width: calc(100vw - 250px);
  height: calc(100vh);
  font-size: 20px;
}
.title_style {
  font-weight: bold;
  margin-top: 20px;
}
.system_main_body {
  padding: 20px 20px;
}
.home_table {
  margin-top: 20px;
  font-size: 10px;
  height: calc(100vh - 150px);
  overflow: scroll;
}
.home_table::-webkit-scrollbar {
  display: none;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}
.home_table_item {
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 4px 4px 0 rgba(236, 236, 236, 0.2),
    0 6px 20px 0 rgba(236, 236, 236, 0.2);
  padding: 10px 10px;
  position: relative;
}
.home_table_grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-gap: 10px;
}
.home_table_item_top {
  display: flex;
  justify-items: center;
  div {
    line-height: 30px;
    margin-left: 5px;
  }
  img {
    width: 30px;
    height: 30px;
  }
}
.home_table_item_auth {
  position: absolute;
  z-index: 2;
  right: 10px;
  top: 10px;
}
.home_table_item_move {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #5f87dc9d;
  border-radius: 5px;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  cursor: default;
  svg {
    margin: 0px 10px;
    cursor: pointer;
  }
}
</style>
