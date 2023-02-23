<!-- 系统设置 -->
<template>
  <div class="system_main">
    <div class="system_main_body">
      <Search />
      <div class="title_style">系统设置</div>
      <div class="setup_table">
        <div class="setup_table_head">
          <div>公众号设置</div>
        </div>
        <div class="setup_table_body_wrap">
          <div class="setup_table_body">
            <div></div>
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
    return {};
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
  font-weight: 50px;
}
.system_main_body {
  margin: 20px 20px;
}

.setup_table {
  border: 1px solid #b5c3d178;
  border-radius: 10px;
  height: calc(100vh - 410px);
  margin-top: 20px;
}
.setup_table_head {
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
}
.setup_table_body {
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
.setup_table_body_wrap {
  overflow: scroll;
  height: calc(100vh - 450px);
}
.setup_table_body_wrap::-webkit-scrollbar {
  display: none;
}
</style>
