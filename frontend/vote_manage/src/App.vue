<template>
  <div style="display: flex; position: relative">
    <NavBar />
    <SubNavBar />
    <MainView />
    <Message v-if="$store.state.globalMessage !== ''" />
    <EditPopup
      v-if="$store.state.editPopProps.name !== ''"
      :data="$store.state.editPopProps"
    />
    <AuthView v-if="!$store.state.isAuth" />
    <EditActivity v-if="$store.state.voteManagePopup.state" />
    <AddActivity v-if="$store.state.voteManageAddPopup" />
    <!-- <EditActivity /> -->
    <!-- 全局域名编辑弹窗 -->
    <UpdateRealm v-if="$store.state.isRealmUpdata" />
    <!-- 奖品申请编辑弹窗 -->
    <UpdatePrize v-if="$store.state.isPrizeUpdate" />
    <!-- 投票管理页面 与活动相关联的投票用户 -->
    <VoteUserActivity v-if="$store.state.voteManagerUserRecord" />
    <!-- 投票管理页面 与活动相关联的订单记录 -->
    <VotePayOrder v-if="$store.state.voteManagerPayOrder" />
  </div>
</template>

<script setup>
import MainView from "./views/MainView.vue";
import NavBar from "./components/NavBar.vue";
import Message from "./components/Message.vue";
import EditPopup from "./components/EditPopup.vue";
import SubNavBar from "./components/SubNavBar.vue";
import AuthView from "./views/AuthView.vue";
import EditActivity from "./components/EditActivity.vue";
import AddActivity from "./components/AddActivity.vue";
import { useStore } from "vuex";
import Cookies from "js-cookie";
import { ref } from "vue";
import UpdateRealm from "./components/UpdateRealm.vue";
import UpdatePrize from "./components/UpdataPrize.vue";
import VoteUserActivity from "./components/VoteUserActivity.vue";
import VotePayOrder from "./components/VotePayOrder.vue";
const $store = useStore();
if (Cookies.get("token") === undefined) {
  $store.dispatch("authActions", false);
}
</script>

<style lang="scss">
@font-face {
  font-family: Memo;
  src: url("./assets/font/agave\ regular\ Nerd\ Font\ Complete\ Mono.ttf");
}

* {
  font-family: Memo;
}
</style>
