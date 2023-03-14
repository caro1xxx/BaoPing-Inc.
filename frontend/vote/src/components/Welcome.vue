<template>
  <div class="welcome" @click="props.data.close">
    <img class="welcome_background" src="../assets/img/3.png" alt="" />
    <div class="welcome_body">
      <div class="body">
        <div class="titles">
          您已经<span style="color: yellow">{{ props.data.value }}分钟</span
          >没有来了,上次支持过的选手现在是
        </div>
        <div class="di">
          第<span style="font-size: 50px; font-weight: bold">{{
            props.data.ranking
          }}</span
          >名
        </div>
        <img class="avaotr" :src="HOST2 + '/media/' + props.data.img" alt="" />
        <div class="username">{{ props.data.name }}</div>
        <div
          @click="
            (e) => {
              support(e);
            }
          "
          class="suddenSupport"
        >
          马上{{ $store.state.settings[94].value }}
        </div>
        <div class="encourage">冠军宝座仍被觊觎,不可松懈,坚持住</div>
        <div class="hint">点击任意位置关闭弹窗</div>
        <div class="sustain_person">
          <div v-for="item in personList">
            <img :src="item" alt="">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { HOST, HOST2 } from "@/ENV";
import { fether } from "@/utils/fether";
import { useStore } from "vuex";
import base64 from "base-64";
import { isNetWork } from "../utils/network";
import Mobile from "mobile-detect";
import { useRoute } from "vue-router";
import { defineEmits, reactive} from "vue";
const $route = useRoute();
const $store = useStore();
const emit = defineEmits(["returnPage", "returnPage1"]);
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
    data: props.data,
  };
  emit("returnPage1", params);
};
const returnPage2 = () => {
  let params = {
    status: false,
    data: props.data,
  };
  emit("returnPage2", params);
};

const support = async (e) => {
  e.stopPropagation();
  /**
   * 点击之后打开验证码弹窗
   * 验证成功并发送请求后
   * 判断是否有公众号二维码有就弹没有就关闭
   */

  // 判断是否在投票时间内
  let newTime = new Date();
  // 得到开始投票时间
  let start_time = $store.state.settings[50].value / 3600 + 8 > 
  newTime.getHours()
  if (start_time) {
    alert("投票未开始");
    // 得到结束投票时间
  } else if (
    $store.state.settings[51].value / 3600 + 8 < 
    newTime.getHours()
  ) {
    alert("投票已结束");
    // 在投票时间内
  } else {
    if ($store.state.settings[67].value) {
      returnPage1();
    } else {
      //   没有开启验证码弹窗时点击直接发送点赞请求
      let keys = await getKey();
      let sercet = await encryption(keys);
      const md = new Mobile(navigator.userAgent);
      let result = await fether("/support/", "post", {
        data: {
          open_id: `${$store.state.open_id}`,
          vote_target_id: props.data.pk,
          vote_id: $route.query.vote_id,
          phone_model: md.mobile(),
          system: md.os(),
          network: isNetWork(),
          key: sercet,
        },
      });
      if (!result) {
        $store.commit('chengePublicData', '点赞失败')
        props.data.close();
        return;
      };
      if ($store.state.settings[26].value) {
        returnPage();
      }
      returnPage2();
    }
  }
};
const encryption = async (key) => {
  return base64.encode(key + "vote");
};

// 请求key
const getKey = () => {
  return fetch(`${HOST}/keys/?open_id=${$store.state.open_id}`)
    .then((res) => res.json())
    .then((data) => {
      if (data.code === 200) {
        return data.key;
      }
    });
};
// 存储支持今日之星的人
const personList = reactive([])
// 获取支持今日之星的人
const getPerson = async () => {
  let result = await fether(`/recentfivevoterecord/?vote_id=${$route.query.vote_id}&vote_target_id=${props.data.pk}`)
  console.log(result);
  result.map(item => {
    personList.push(item.fields.voteuser.avator)
  })
}
getPerson()
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
    height: 60%;
    width: 80%;
    color: white;
    text-align: center;
    position: relative;
    display: inline-flex;
    vertical-align: top;
    justify-content: center;
    align-items: center;

    .titles {
      position: absolute;
      top: 25%;
      width: 60%;
    }
    .di {
      font-size: 30px;
      position: absolute;
      top: 35%;
    }
    .avaotr {
      width: 100px;
      height: 100px;
      position: absolute;
      top: 48%;
    }
    .username {
      font-weight: bold;
      position: absolute;
      top: 70%;
    }
    .suddenSupport {
      font-weight: bold;
      font-size: 20px;
      color: #444444;
      position: absolute;
      top: 81.5%;
    }
    .encourage {
      position: absolute;
      font-size: 10px;
      top: 94%;
    }
    .hint {
      position: absolute;
      font-size: 10px;
      top: 100%;
    }
    .sustain_person{
      height: 35px;
      position: absolute;
      top: 105%;
      display: flex;
      img{
        width: 35px;
        height: 35px;
        border-radius: 50%;
      }
    }
  }
}
</style>
