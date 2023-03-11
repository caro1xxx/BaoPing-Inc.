<template>
  <div class="welcome" @click="props.data.close">
    <img class="welcome_background" src="../assets/img/3.png" alt="" />
    <div class="welcome_body">
      <div class="body">
        <div>
          您已经<span style="color: yellow">{{ props.data.value }}分钟</span
          >没有来了,上次支持过的选手现在是
        </div>
        <div style="font-size: 30px">
          第<span style="font-size: 50px; font-weight: bold">{{
            props.data.ranking
          }}</span
          >名
        </div>
        <img
          style="width: 100px; height: 100px; margin: 20px 0px"
          :src="HOST2 + '/media/' + props.data.img"
          alt=""
        />
        <div style="font-weight: bold">{{ props.data.name }}</div>
        <div
          @click="
            (e) => {
              support(e);
            }
          "
          style="
            margin-top: 45px;
            font-weight: bold;
            font-size: 20px;
            color: #444444;
          "
        >
          马上支持
        </div>
        <div style="margin-top: 40px; font-size: 10px">
          冠军宝座仍被觊觎,不可松懈,坚持住
        </div>
        <div style="margin-top: 15px; font-size: 10px">
          点击任意位置关闭弹窗
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {HOST, HOST2 } from "@/ENV";
import { fether } from "@/utils/fether";
import { useStore } from "vuex";
import base64 from "base-64";
import { isNetWork } from "../utils/network";
import Mobile from "mobile-detect";
import { useRoute } from "vue-router";
import { defineEmits } from "vue";
const $route = useRoute();
const $store = useStore();
const emit = defineEmits(["returnPage", 'returnPage1']);
// const emit1 = defineEmits([""]);
const props = defineProps({
  data: Object,
});
const returnPage = () => {
  let params = {
    status: false,
  };
  emit("returnPage", params);
};
const returnPage1 = () => {
  let params = {
    status: false,
    data: props.data
  };
  emit("returnPage1", params);
};
const returnPage2 = () => {
  let params = {
    status: false,
    data: props.data
  };
  emit("returnPage2", params);
};

const support = async (e)  => {
  e.stopPropagation();
  /**
   * 点击之后打开验证码弹窗
   * 验证成功并发送请求后
   * 判断是否有公众号二维码有就弹没有就关闭
   */

  // 判断是否在投票时间内
  let newTime = new Date();
  // 得到开始投票时间
  let start_time =
    $store.state.settings[50].value >
    parseInt((newTime.getTime() / 1000) % 86400) * 3600;
  if (start_time) {
    alert("投票未开始");
    // 得到结束投票时间
  } else if (
    parseInt((newTime.getTime() / 1000) % 86400) >
    $store.state.settings[51].value
  ) {
    alert("投票已结束");
    // 在投票时间内
  } else {
    if ($store.state.settings[26].value) {
      returnPage()
    } else if ($store.state.settings[20].value) {
      returnPage1()
    } else {
    //   没有开启验证码弹窗时点击直接发送点赞请求
      let keys = await getKey();
      let sercet = await encryption(keys);
      const md = new Mobile(navigator.userAgent);
      let result = await fether("/support/", "post", {
        data: {
          open_id: "wxtest6",
          vote_target_id: props.data.pk,
          vote_id: $route.query.vote_id,
          phone_model: md.mobile(),
          system: md.os(),
          network: isNetWork(),
          key: sercet,
        },
      });
      if (!result) return;
      returnPage2()
    }
  }
};
const encryption = async (key) => {
  return base64.encode(key + "vote");
};

// 请求key
const getKey = () => {
  return fetch(`${HOST}/keys/?open_id=00001`)
    .then((res) => res.json())
    .then((data) => {
      if (data.code === 200) {
        return data.key;
      }
    });
};
</script>

<style lang="scss" scoped>
.welcome {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  background-color: #00000074;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  z-index: 10;
}
.welcome_background {
  height: 60%;
  width: 80%;
  position: relative;
}
.welcome_body {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  z-index: 11;
  .body {
    width: 50%;
    height: 30%;
    color: white;
    text-align: center;
  }
}
</style>
