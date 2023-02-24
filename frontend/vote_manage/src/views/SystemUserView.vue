<template>
  <div class="system_main">
    <div class="system_main_body">
      <Search />
      <div class="title_style">系统用户</div>
      <div class="home_table">
        <div class="home_table_head">
          <div v-for="item in tableHead" :key="item.name">{{ item.name }}</div>
        </div>
        <div class="home_table_body_wrap">
          <div class="home_table_body" v-for="item in tableData" :key="item.id">
            <div>{{ item.id }}</div>
            <div>{{ item.username }}</div>
            <div>{{ item.createid }}</div>
            <div>{{ item.oldid }}</div>
            <div>{{ item.createtime }}</div>
            <div>{{ item.oldtime }}</div>
            <div>{{ item.card }}</div>
            <div v-if="item.state">
              <img width="20" height="20" src="../assets/img/19.png" alt="" />
            </div>
            <div v-else>
              <img width="20" height="20" src="../assets/img/21.png" alt="" />
            </div>
            <div class="home_table_body_item">{{ item.operate }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Search from "@/components/Search.vue";

export default {
  data() {
    return {
      tableHead: [
        { name: "UID" },
        { name: "用户" },
        { name: "创建ID" },
        { name: "最后登录ID" },
        { name: "创建时间" },
        { name: "最后登录" },
        { name: "身份" },
        { name: "状态" },
        { name: "操作" },
      ],
      tableData: [
        {
          id: "pupu",
          username: "yangjie",
          createid: "5358535615",
          oldid: "5358535615",
          createtime: "2023-2-15 10:30:49",
          oldtime: "2023-2-16 11:02:36",
          card: "协作者",
          state: false,
          operate: "删除",
        },
        {
          id: "pupu",
          username: "yangjie",
          createid: "5358535615",
          oldid: "5358535615",
          createtime: "2023-2-15 10:30:49",
          oldtime: "2023-2-16 11:02:36",
          card: "协作者",
          state: true,
          operate: "删除",
        },
        {
          id: "pupu",
          username: "yangjie",
          createid: "5358535615",
          oldid: "5358535615",
          createtime: "2023-2-15 10:30:49",
          oldtime: "2023-2-16 11:02:36",
          card: "协作者",
          state: true,
          operate: "删除",
        },
        {
          id: "pupu",
          username: "yangjie",
          createid: "5358535615",
          oldid: "5358535615",
          createtime: "2023-2-15 10:30:49",
          oldtime: "2023-2-16 11:02:36",
          card: "协作者",
          state: false,
          operate: "删除",
        },
        {
          id: "pupu",
          username: "yangjie",
          createid: "5358535615",
          oldid: "5358535615",
          createtime: "2023-2-15 10:30:49",
          oldtime: "2023-2-16 11:02:36",
          card: "协作者",
          state: false,
          operate: "删除",
        },
        {
          id: "pupu",
          username: "yangjie",
          createid: "5358535615",
          oldid: "5358535615",
          createtime: "2023-2-15 10:30:49",
          oldtime: "2023-2-16 11:02:36",
          card: "协作者",
          state: false,
          operate: "删除",
        },
        {
          id: "pupu",
          username: "yangjie",
          createid: "5358535615",
          oldid: "5358535615",
          createtime: "2023-2-15 10:30:49",
          oldtime: "2023-2-16 11:02:36",
          card: "协作者",
          state: false,
          operate: "删除",
        },
        {
          id: "pupu",
          username: "yangjie",
          createid: "5358535615",
          oldid: "5358535615",
          createtime: "2023-2-15 10:30:49",
          oldtime: "2023-2-16 11:02:36",
          card: "协作者",
          state: false,
          operate: "删除",
        },
        {
          id: "pupu",
          username: "yangjie",
          createid: "5358535615",
          oldid: "5358535615",
          createtime: "2023-2-15 10:30:49",
          oldtime: "2023-2-16 11:02:36",
          card: "协作者",
          state: false,
          operate: "删除",
        },
      ],
    };
  },
  components: {
    Search,
  },
};
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
  height: calc(100vh - 410px);
  margin-top: 20px;
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
.home_table_body_wrap {
  overflow: scroll;
  height: calc(100vh - 450px);
}
.home_table_body_wrap::-webkit-scrollbar {
  display: none;
}
.home_table_body_item {
  cursor: pointer;
}
</style>
