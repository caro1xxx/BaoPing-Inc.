<template>
  <!-- 礼物 -->
  <GifiVue :data="props.data" v-if="giftState.state" :method="giftState" />
  <!-- 选手页视频广告 -->
  <div
    class="stateAdv"
    @click="downStateAdv"
    v-if="$store.state.settings[15].value"
  >
    <video
      style="background-color: #000"
      class="state_img"
      :src="HOST2 + '/media/' + $store.state.settings[87].value"
      @click="(e) => e.stopPropagation()"
      autoplay
    >
      您的浏览器不支持 video 标签。
    </video>
  </div>
  <div class="body">
    <div class="body_top">
      <img :src="HOST2 + '/media/' + props.data.avator" alt="" />
    </div>
    <div class="body_top_mask">
      <div>
        <div class="name">{{ props.data.name }}</div>
        <div class="num">编号:{{ props.data.pk }}</div>
      </div>
    </div>
    <div class="body_content">
      <div class="body_content_wrap">
        <div class="top">
          <div>当前票数: {{ listIndex.Num }}</div>
          <div>当前排名: {{ props.data.index + 1 }}</div>
        </div>
        <div class="introduce">
          <div class="title">选手介绍</div>
          <div class="content" id="detail">{{ props.data.detail }}</div>
          <div class="more" @click="lookMore">
            {{ listIndex.clickNum % 2 === 0 ? "查看更多" : "收回" }}
          </div>
        </div>
        <div class="comment" v-if="$store.state.settings[66].value">
          <input
            type="text"
            ref="commtentData"
            v-model="commtentData.value"
            placeholder="请发表评论"
          />
          <button @click="check">评论</button>
        </div>
        <div class="footer" v-if="$store.state.settings[66].value">
          <div class="title">互动</div>
          <div class="content">
            <div v-for="item in comments.data" class="item">
              <div class="user">{{ item.vote_user }}</div>
              <div class="comment_content">{{ item.content }}</div>
              <div class="time">
                {{ parseStampTime(item.create_time) }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="btn">
      <div class="btn_wrap">
        <div class="home" @click="returnPage(false)">返回</div>
        <div
          class="like"
          :style="{
            width: $store.state.settings[68].value === 0 ? '75%' : '',
          }"
          @click="like"
        >
          点赞
        </div>
        <div
          class="pay"
          v-if="$store.state.settings[68].value"
          @click="Assistance"
        >
          助力
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { fether } from "@/utils/fether";
import { reactive, defineEmits, onMounted, ref, watch } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import { HOST, HOST2 } from "../ENV";
import Mobile from "mobile-detect";
import { isNetWork } from "../utils/network";
import { parseStampTime } from "../utils/times";
import GifiVue from "./Gifi.vue";
import base64 from "base-64";
const emit = defineEmits(["returnPage"]);

const $route = useRoute();
const $store = useStore();
const videoRef = ref("");

const giftState = reactive({
  close: () => {
    giftState.state = false;
  },
  state: false,
});

const props = defineProps({
  data: {
    informationKey: Object,
  },
});

const listIndex = reactive({
  // 支持数
  Num: props.data.count,
  // 查看更多/收回按钮点击次数
  clickNum: 0,
});

// 选手评论
const comments = reactive({ data: [] });

// 评论输入数据
let commtentData = ref("");

const returnPage = (value) => {
  let params = {
    status: value,
  };
  emit("returnPage", params);
};
const returnPage1 = () => {
  let params = {
    status: false,
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
const returnPage3 = () => {
  let params = {
    status: false,
    data: props.data,
  };
  emit("returnPage3", params);
};

// 点赞
const like = async () => {
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
    // 等待100毫秒后再执行避免页面未渲染完成拿不到数据
    if ($store.state.settings[67].value) {
      setTimeout(() => {
        // 刷新支持数
        // athleteInformation.count += 1
        returnPage2();
      }, 100);
    } else {
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
        $store.commit("chengePublicData", "点赞失败");
        return;
      }
      if ($store.state.settings[26].value) {
        setTimeout(() => {
          returnPage1();
        }, 100);
      }
      // 刷新支持数
      listIndex.Num = listIndex.Num + 1;
      props.data.count = props.data.count + 1;
      returnPage3();
    }
  }
};

// 加密
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

// 获取选手评论
const getUserComment = async () => {
  if ($store.state.settings[66].value === 0) return;
  let result = await fether(`/comment/?vote_target_id=${props.data.pk}`);
  console.log(result);
  if (!result) return;
  comments.data = [];
  result.forEach((item) => {
    comments.data.push({ ...item.fields });
  });
};

// 校验评论输入
const check = async () => {
  if (!commtentData.value.value) return;
  let result = await fether("/comment/", "post", {
    data: {
      vote_target_id: props.data.pk,
      vote_user_open_id: `${$store.state.open_id}`,
      content: commtentData._value.value,
    },
  });
  if (!result) {
    $store.commit("chengePublicData", "评论失败");
    return;
  }
  getUserComment();
  $store.commit("chengePublicData", "评论成功");
  setTimeout(() => {
    // 当评论成功时清空评论
    let input = document.getElementsByTagName("input");
    input[0].value = "";
  }, 1000);
};

const downStateAdv = () => {
  $store.state.settings[15].value = false;
};

onMounted(() => {
  getUserComment();
});

const Assistance = () => {
  giftState.state = true;
};

// 查看更多
const lookMore = () => {
  listIndex.clickNum = listIndex.clickNum + 1;
  if (props.data.detail === undefined) {
    $store.commit("chengePublicData", "暂无更多");
  }
  let detail = document.getElementById("detail");
  if (listIndex.clickNum % 2 === 0) {
    detail.style.display = "-webkit-box";
    detail.style.webkitLineClamp = 3;
    detail.style.overflow = "hidden";
  } else {
    detail.style.display = "block";
  }
};

watch(
  () => $store.state.currentClickAlht,
  (newVal) => {
    listIndex.Num = $store.state.currentClickAlht;
  }
);
</script>

<style lang="scss" scoped>
.body {
  height: 100%;
}
button {
  font-size: 17px;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 50px;
  border-radius: 10px;
  font-weight: bold;
}
.stateAdv {
  position: absolute;
  right: 0px;
  left: 0px;
  bottom: 0px;
  top: 0px;
  background-color: #00000074;
  z-index: 10;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  .state_img {
    width: 70%;
    height: 30%;
    border: 5px;
    border-radius: 5px;
  }
}
.body_top {
  position: absolute;
  z-index: 2;
  height: 35%;
  width: 100%;
  background-color: black;
}
.body_top_mask {
  position: absolute;
  z-index: 3;
  height: 35%;
  width: 100%;
  background-color: rgba(99, 99, 99, 0.529);
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  .name {
    font-size: 30px;
    font-weight: bold;
    color: white;
    padding: 0px 10px;
  }
  .num {
    font-size: 15px;
    border-radius: 15px;
    background-color: white;
    padding: 5px 10px;
    margin-top: 10px;
    text-align: center;
  }
}
.body_content {
  position: absolute;
  top: 30%;
  width: 100%;
  height: calc(70vh);
  z-index: 4;
  background-color: white;
  border-radius: 40px 40px 0px 0px;
}
.body_content_wrap {
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */

  padding: 30px 10px;
  margin: 10px;
  height: calc(60vh);
  overflow: scroll;
  .top {
    display: flex;
    font-size: 15px;
    color: black;
    div {
      width: 50%;
    }
  }
  .introduce {
    margin-top: 20px;
    .title {
      font-size: 15px;
      font-weight: bold;
    }
    .content {
      margin-top: 10px;
      font-size: 10px;
      display: -webkit-box;
      overflow: hidden;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      line-height: 20px;
      overflow-y: hidden;
    }
    .more {
      text-align: end;
      font-size: 10px;
      font-weight: bold;
      text-decoration: underline;
      cursor: pointer;
    }
  }
  .comment {
    display: flex;
    margin-top: 20px;
    justify-content: space-around;
    align-items: center;
    input {
      width: 70%;
      height: 30px;
      border: 1px solid rgb(99, 96, 96);
      padding-left: 10px;
    }
    button {
      width: 70px;
      height: 40px;
      background-color: green;
      color: #fff;
      font-size: 15px;
      border-radius: 10px;
      text-align: center;
      line-height: 30px;
    }
  }
  .footer {
    margin: 20px 0px;
    .title {
      font-size: 15px;
      font-weight: bold;
    }
    .item {
      margin: 10px 0px;
      border-bottom: 0.5px solid #dddddd96;
    }
    .comment_content {
      margin-top: 5px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-left: 20px;
    }
    .time {
      text-align: end;
      color: #cecece;
      font-size: 10px;
      margin-bottom: 10px;
    }
  }
}
.body_content_wrap::-webkit-scrollbar {
  display: none;
}
.btn {
  position: fixed;
  background-color: white;
  width: calc(100vw);
  padding: 5px;
  z-index: 5;
  bottom: 0;
  right: 0;
  left: 0;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  .btn_wrap {
    display: flex;
    border-radius: 30px;
    text-align: center;
    line-height: 50px;
    font-size: 15px;
    div {
      margin: 5px;
    }
    .home {
      height: 50px;
      width: 15%;
      line-height: 70px;
      font-weight: bold;
      display: inline-flex;
      vertical-align: top;
      justify-content: center;
      align-items: center;
      box-shadow: 0 4px 8px 0 rgba(157, 157, 157, 0.2),
        0 6px 20px 0 rgba(154, 154, 154, 0.19);
      border-radius: 5px;
    }
    .like {
      height: 50px;
      width: 50%;
      line-height: 70px;
      display: inline-flex;
      vertical-align: top;
      justify-content: center;
      align-items: center;
      box-shadow: 0 4px 8px 0 rgba(157, 157, 157, 0.2),
        0 6px 20px 0 rgba(154, 154, 154, 0.19);
      border-radius: 5px;
      background-color: #f78126;
      color: white;
    }
    .pay {
      height: 50px;
      width: 25%;
      line-height: 70px;
      display: inline-flex;
      vertical-align: top;
      justify-content: center;
      align-items: center;
      color: white;
      background-color: green;
      border-radius: 5px;
    }
  }
}
</style>
