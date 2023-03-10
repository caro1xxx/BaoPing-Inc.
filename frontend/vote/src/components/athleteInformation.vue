<template>
  <!-- 礼物 -->
  <GifiVue :data="props.data" v-if="giftState.state" :method="giftState" />
  <!-- 选手页视频广告 -->
  <div class="stateAdv" v-if="$store.state.settings[11].value">
    <video
      style="background-color: #000"
      class="state_img"
      :src="HOST + '/media/' + $store.state.settings[87].value"
      controls="controls"
    >
      您的浏览器不支持 video 标签。
    </video>
  </div>
  <div class="body">
    <div class="body_content">
      <div class="body_content_brief">
        <div class="body_content_brief_item">
          <img
            v-if="athleteInformation.avator"
            :src="`${HOST2}/media/${athleteInformation.avator}`"
            alt=""
          />
        </div>
        <div class="body_content_brief_item">
          <div class="body_content_brief_number">编号：{{ props.data }}</div>
          <div class="body_content_brief_name">
            {{ athleteInformation.name }}
          </div>
        </div>
      </div>
      <div class="body_content_ranking">
        <div
          class="body_content_ranking_item"
          style="font-size: 20px; font-weight: bold"
        >
          当前票数
        </div>
        <div
          class="body_content_ranking_item"
          style="font-size: 20px; font-weight: bold"
        >
          当前排名
        </div>
        <div
          class="body_content_ranking_item"
          style="font-size: 30px; color: #33cc66"
        >
          {{ athleteInformation.count }}
        </div>
        <div
          class="body_content_ranking_item"
          style="font-size: 30px; color: #33cc66"
        >
          {{ props.data }}
        </div>
      </div>
      <div class="body_content_sign">
        <img
          style="width: 30px; height: 30px; margin-right: 10px"
          src=""
          alt=""
        />
        <span>你的付出我们有目共睹</span>
      </div>
      <div class="body_content_detail">{{ athleteInformation.detail }}</div>
      <!-- 评论 -->
      <div v-if="$store.state.settings[66].value">
        <div class="conment_body">
          <input v-model="commtentData" type="text" class="comment_input" />
          <div @click="check">评论</div>
        </div>
        <div style="font-size: 10px">提交评论后需审核后才能显示</div>
        <div v-for="item in comments" class="comment_item">
          <div class="comment_item_user">{{ item.vote_user }}</div>
          <div class="comment_item_content">
            <div class="comment_item_content_body">{{ item.content }}</div>
            <div class="comment_item_content_time">
              {{ parseStampTime(item.create_time) }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer">
      <div class="footer_item1">
        <button
          style="background-color: #ffffff; color: rgb(36, 105, 77)"
          @click="returnPage(false)"
        >
          首页
        </button>
      </div>
      <!-- 如果不显示助力那么将投一票宽度变大-->
      <div
        :class="
          $store.state.settings[68].value ? 'footer_item2' : 'footer_item3'
        "
      >
        <button style="background-color: orange; color: #ffffff" @click="like">
          投一票
        </button>
      </div>
      <!-- 是否显示助力 -->
      <div class="footer_item1" v-if="$store.state.settings[68].value">
        <button
          @click="
            (e) => {
              e.stopPropagation();
              giftState.state = true;
            }
          "
          style="background-color: rgb(36, 105, 77); color: #ffffff"
        >
          助力
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { fether } from "@/utils/fether";
import { reactive, defineEmits, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import { HOST, HOST2 } from "../ENV";
import Mobile from "mobile-detect";
import { isNetWork } from "../utils/network";
import { parseStampTime } from "../utils/times";
import GifiVue from "./Gifi.vue";
const emit = defineEmits(["returnPage"]);

const $route = useRoute();
const athleteInformation = reactive({});
const $store = useStore();

const giftState = reactive({
  close: () => {
    giftState.state = false;
  },
  state: false,
});

const props = defineProps({
  data: {
    informationKey: Number,
  },
});

// 选手评论
const comments = reactive([]);

// 评论输入数据
let commtentData = ref("");

// 获取选手详情
const getAthleteInformation = async () => {
  let Arr = [];
  let result = await fether(`/votetarget/?vote_id=${$route.query.vote_id}`);
  result.map((item) => {
    Arr.push({ ...item.fields, pk: item.pk, model: item.model });
  });
  let arr = [];
  arr = Arr.filter((item) => {
    return item.pk === props.data;
  });
  athleteInformation.avator = arr[0].avator;
  athleteInformation.name = arr[0].name;
  athleteInformation.detail = arr[0].detail;
  athleteInformation.count = arr[0].count;
};
getAthleteInformation();

const returnPage = (value) => {
  let params = {
    status: value,
  };
  emit("returnPage", params);
};

// 点赞
const like = async () => {
  // 判断是否在投票时间内
  let newTime = new Date();
  // 得到开始投票时间
  let start_time = Math.floor(86400 / $store.state.settings[50].value / 24);
  if (newTime.getHours() < start_time) {
    alert("投票未开始");
    // 得到结束投票时间
  } else if (newTime.getTime() > $store.state.settings[51].value * 1000) {
    alert("投票已结束");
    // 在投票时间内
  } else {
    let keys = await getKey();
    let sercet = await encryption(keys);
    const md = new Mobile(navigator.userAgent);
    let result = await fether("/support/", "post", {
      data: {
        open_id: "wxtest6",
        vote_target_id: props.data,
        vote_id: $route.query.vote_id,
        phone_model: md.mobile(),
        system: md.os(),
        network: isNetWork(),
        key: sercet,
      },
    });
  }
};

// 加密
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

// 获取选手评论
const getUserComment = async () => {
  if ($store.state.settings[66].value === 0) return;
  let result = await fether(`/comment/?vote_target_id=${props.data}`);
  if (!result) return;
  result.forEach((item) => {
    comments.push({ ...item.fields });
  });
};

// 校验评论输入
const check = async () => {
  if (!commtentData.value) return;
  let result = await fether("/comment/", "post", {
    data: {
      vote_target_id: props.data,
      vote_user_open_id: "wxtest6",
      content: commtentData.value,
    },
  });
  if (!result) return;
  getUserComment();
};

onMounted(() => {
  getUserComment();
});
</script>

<style lang="scss" scoped>
.body {
  height: 100%;
  display: flex;
  flex-direction: column;
}
.body_content {
  flex: 1;
  overflow-y: scroll;
  padding: 20px;
}
.body_content_brief {
  padding: 0px 0px 20px 0px;
  display: flex;
  justify-content: space-between;
  border-bottom: 1px dashed rgb(138, 135, 135);
}
.body_content_brief_item {
  width: 45%;
  height: 100px;
}
.body_content_brief_number {
  height: 40px;
  line-height: 40px;
  font-size: 25px;
  font-weight: bold;
  background-color: rgb(183, 247, 225);
}
.body_content_brief_name {
  height: 50px;
  margin-top: 10px;
}
.body_content_ranking {
  display: grid;
  grid-template-columns: auto auto;
  grid-gap: 10px;
  padding: 10px;
}
.body_content_ranking_item {
  text-align: center;
  padding: 10px 0;
}
.body_content_sign {
  height: 60px;
  border-radius: 5px 5px 15px 15px;
  background-color: rgb(36, 105, 77);
  display: flex;
  align-items: center;
  padding-left: 15px;
  color: #fff;
  font-size: 20px;
}
.body_content_detail {
  margin: 20px 0px;
}
.footer {
  height: 55px;
  display: grid;
  grid-template-columns: auto auto auto auto;
  grid-gap: 10px;
  font-size: 20px;
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
.footer_item2 {
  grid-column-start: 2;
  grid-column-end: 4;
}
.footer_item3 {
  grid-column-start: 2;
  grid-column-end: 6;
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
    width: 90%;
    height: 90%;
    border: 5px;
  }
}
.comment_input {
  border: 0.5px solid #cecece;
  padding: 10px 10px;
  width: 63%;
  border-radius: 5px;
}
.conment_body {
  display: flex;
  div {
    width: 25%;
    margin-left: 5%;
    background-color: green;
    border-radius: 5px;
    text-align: center;
    line-height: 35px;
    color: white;
  }
}
.comment_item {
  margin-top: 20px;
  border-bottom: 0.5px solid #cecece88;
  .comment_item_user {
    font-size: 20px;
    font-weight: bold;
  }
  .comment_item_content {
    display: flex;
    padding: 20px 0px;
    .comment_item_content_body {
      width: 60%;
    }
    .comment_item_content_time {
      width: 40%;
      font-size: 10px;
      color: #c3c3c3;
      text-align: end;
    }
  }
}
</style>
