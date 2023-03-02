<template>
  <div class="search">
    <img src="../assets/img/18.png" width="25" height="25" alt="" />
    <input
      @keypress="(e) => query(e)"
      class="search_payload"
      placeholder="搜索..."
    />
  </div>
  <div class="search_line"></div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { fether } from "@/utils/fether";
import jsCookie from "js-cookie";
const $router = useRouter();

const query = async (e) => {
  if (e.code === "Enter") {
    switch ($router.currentRoute.value.fullPath) {
      case "/system/systemuser":
        let result = await fether(`/userinfo/?token=${jsCookie.get("token")}`);
        // console.log(result);
        break;
    }
  }
};
</script>

<style lang="scss" scoped>
.search {
  font-size: 15px;
  color: #b5c3d1;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
}
.search_payload {
  width: calc(70vw);
  margin-left: 20px;
  outline: none;
  border: none;
  background-color: #f9f9f9;
}

.search_payload::placeholder {
  color: #b5c3d1;
}
.search_line {
  height: 1px;
  border-bottom: 1px solid #b5c3d17a;
  margin-top: 15px;
}
</style>
