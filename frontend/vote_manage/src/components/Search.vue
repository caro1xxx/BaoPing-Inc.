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
import {  useStore } from "vuex"
import { reactive } from "vue";
const $router = useRouter();
const $store = new useStore()

const contentBox = reactive({
  searchKey: '',
  searchValue: '',
  axiosUrl: '',
})

const query = async (e) => {
  if (e.code === "Enter") {
    if (e.target.value === '') {
      contentBox.searchValue = ''
    } else {
      contentBox.searchValue = e.target.value
    }
    switch ($router.currentRoute.value.fullPath) {
      case "/system/systemuser":
        if (contentBox.searchValue) {
          if (e.target.value.length > 4) { // 用户名
            contentBox.searchKey = 'username'
          } else if (2 <= e.target.value.length <= 4) { //姓名
            contentBox.searchKey = 'name'
          }
          contentBox.axiosUrl = `/userinfo/?username=${jsCookie.get('username')}&token=${jsCookie.get('token')}&search_key=${contentBox.searchKey}&search_value=${contentBox.searchValue}`
        } else {
          contentBox.axiosUrl = `/userinfo/?username=${jsCookie.get('username')}&token=${jsCookie.get('token')}`
        }
        break;
      case "/system/gloabldomain": //域名
        if (contentBox.searchValue) {
            let reg = /[A-Za-z0-9]+\.[A-Za-z0-9]+[\/=\?%\-&_~`@[\]\':+!]*([^<>\"\"])*$/;
            if (reg.test(contentBox.searchValue)) {
              console.log(1);
              contentBox.searchKey = 'domain_name'
              contentBox.axiosUrl = `/domain/?token=${jsCookie.get('token')}&search_key=${contentBox.searchKey}&search_value=${contentBox.searchValue}`
            } else {
              console.log(2);
              $store.dispatch("GlobalMessageActions", '域名格式不正确');
            }
        } else {
            contentBox.axiosUrl = `/domain/?token=${jsCookie.get('token')}`
          }
        break;
      case "/message/prizeapplication":
        if (e.target.value.length) { // 手机号
          contentBox.searchKey = 'phone_number'
          contentBox.axiosUrl = `/applyprize/?token=${jsCookie.get('token')}&search_key=${contentBox.searchKey}&search_value=${contentBox.searchValue}`
        } else {
          contentBox.axiosUrl = `/applyprize/?token=${jsCookie.get('token')}`
        }
        break;
      case "/vote/activity":
        if (contentBox.searchValue) {
          if (e.target.value.length === 6) { // 活动参数
            contentBox.searchKey = 'vote_id'
          } else { ///创建者
            contentBox.searchKey = 'create_user__name'
          }
          contentBox.axiosUrl = `/voteactivity/?token=${jsCookie.get('token')}&search_key=${contentBox.searchKey}&search_value=${contentBox.searchValue}`
        } else {
          contentBox.axiosUrl = `/voteactivity/?token=${jsCookie.get('token')}`
        }
        break;
      case "/order/paymentrecord":  //支付订单号
      if (contentBox.searchValue) {
            contentBox.searchKey = 'payment_order_id'
            contentBox.axiosUrl = `/paymentrecord/?token=${jsCookie.get('token')}&search_key=${contentBox.searchKey}&search_value=${contentBox.searchValue}`
          } else {
            contentBox.axiosUrl = `/paymentrecord/?token=${jsCookie.get('token')}`
          }
        break;
      case "/parent/voteparent": // open_id
      if (contentBox.searchValue) {
            contentBox.searchKey = 'open_id'
            contentBox.axiosUrl = `/voteuser/?token=${jsCookie.get('token')}&search_key=${contentBox.searchKey}&search_value=${contentBox.searchValue}`
          } else {
            contentBox.axiosUrl = `/voteuser/?token=${jsCookie.get('token')}`
          }
        break;
      }
      let result = await fether(contentBox.axiosUrl)
      if (result.code === 200) {
        $store.commit('getFilterData', result)
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
