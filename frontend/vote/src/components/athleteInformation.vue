<template>
  <!-- 选手页视频广告 -->
  <div class="stateAdv" v-if="!$store.state.settings[11].value">
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
      <div class="body_content_separate"></div>
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
          style="font-size: 17px; color: #33cc66"
        >
          {{ athleteInformation.count }}
        </div>
        <div
          class="body_content_ranking_item"
          style="font-size: 17px; color: #33cc66"
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
      <div class="footer_item2">
        <button style="background-color: orange; color: #ffffff" @click="like">
          投一票
        </button>
      </div>
      <div class="footer_item1">
        <button style="background-color: rgb(36, 105, 77); color: #ffffff">
          助力
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { fether } from "@/utils/fether";
import { reactive, defineEmits } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import { HOST, HOST2 } from "../ENV";
import Mobile from "mobile-detect";
import { isNetWork } from "../utils/network";
const emit = defineEmits(["returnPage"]);

const $route = useRoute();
const athleteInformation = reactive({});
const $store = useStore();
const props = defineProps({
  data: {
    informationKey: Number,
  },
});
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
.body_content_separate {
  width: 80%;
  height: 0px;
  border: 1px dashed black;
  margin: auto;
}
.body_content_ranking {
  display: grid;
  grid-template-columns: auto auto;
  grid-gap: 10px;
  padding: 10px;
}
.body_content_ranking_item {
  text-align: center;
  padding: 20px 0;
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
  margin-top: 20px;
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
</style>
