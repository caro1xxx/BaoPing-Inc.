<template>
  <WelcomeVue :data="welcomeState" v-if="welcomeState.state" />
  <athleteInformation
    v-if="enrollStatus.isAthleteConfig"
    @returnPage="getChild"
    :data="informationKey"
  />
  <customerService
    v-if="enrollStatus.iscustomerService"
    @returnPage="getCusrr"
  />
  <!-- 二维码弹窗 -->
  <isQrcode v-if="enrollStatus.isOpenQscode" @returnPage="downQscode" />
  <!-- 验证码弹窗 -->
  <verificationCode
    v-if="enrollStatus.isVerificationCode"
    @returnPage="downVerificationCode"
    :data="verificationCodeData"
    :method="enrollStatus.closeVerificationCode"
  />
  <div class="body" v-if="!enrollStatus.isAthleteConfig">
    <!-- 开场广告图 -->
    <div class="stateAdv" v-if="$store.state.settings[11].value">
      <img
        class="state_img"
        :src="HOST + '/media/' + $store.state.settings[84].value"
      />
    </div>
    <!-- 开场视频广告 -->
    <div class="stateAdv" v-if="$store.state.settings[11].value">
      <video
        style="background-color: #000"
        class="state_img"
        :src="HOST + '/media/' + $store.state.settings[86].value"
        controls="controls"
      >
        您的浏览器不支持 video 标签。
      </video>
    </div>
    <div class="content">
      <div class="content_top" id="Carousel">
        <div class="content_top_center">
          <!-- 最强企业评选 -->
          <div style="font-size: 20px">
            {{ $store.state.settings[49].value }}
          </div>
          <div class="content_top_titles"></div>
          <div>优秀企业推荐</div>
        </div>
        <!-- 设置顶部滚动文字 -->
        <div
          class="content_top_scroll_text"
          v-if="$store.state.settings[1].value"
        >
          <div class="scroll_text_content">
            <p>{{ $store.state.settings[83].value }}</p>
          </div>
        </div>
        <!-- 弹幕 -->
        <div
          style="text-align: end; overflow: hidden"
          class="content_top_popup"
          v-if="$store.state.settings[25].value && popupList.showState"
        >
          <div class="scroll_text_content">
            <p
              style="display: inline; color: #545c64"
              v-for="item in popupList.data"
              v-html="item"
            ></p>
          </div>
        </div>
      </div>
      <div class="content_body">
        <div class="content_body_persennum">
          <div class="content_body_persennum_item">
            <img
              :style="{ width: '20px', height: '22px' }"
              src="../assets/images/3.png"
              alt=""
            />访问数：
            <!-- 访问数量 -->
            <span>{{ $store.state.settings[42].value }}</span>
          </div>
          <div class="content_body_persennum_item">
            <img
              :style="{ width: '20px', height: '22px' }"
              src="../assets/images/4.png"
              alt=""
            />报名数：<span>45</span>
          </div>
        </div>
        <!-- 活动到期时间倒计时 -->
        <div class="expire_time">
          <div class="expire_time_label">倒计时距结束</div>
          <div class="expire_time_number">
            <div>{{ expireData.day }}</div>
            天
            <div>{{ expireData.houers }}</div>
            时
            <div>{{ expireData.minute }}</div>
            分
            <div>{{ expireData.second }}</div>
            秒
          </div>
        </div>
        <div class="content_body_search">
          <input type="text" placeholder="搜索名称或编号" />
          <div class="content_body_search_button">
            <div class="content_body_search_text"></div>
            <div class="content_body_search_status">已更新</div>
          </div>
        </div>
        <div class="content_body_information">
          <div
            class="content_body_information_item"
            @click="athleteConfig($event, item.pk)"
            v-for="(item, index) in informationData"
            :key="index"
          >
            <img
              class="content_body_information_background"
              :src="
                require(`../assets/images/${
                  index + 1 === 1
                    ? 6
                    : index + 1 === 2
                    ? 10
                    : index + 1 === 3
                    ? 14
                    : 21
                }.png`)
              "
              alt=""
            />
            <div class="content_body_information_body">
              <div class="content_body_information_title">
                <div style="width: 80px"></div>
                <div class="content_body_information_name">
                  {{ item.name }}
                </div>
              </div>
              <div class="content_body_information_content">
                <div class="content_body_information_left">
                  <img :src="`${HOST2}/media/${item.avator}`" alt="" />
                </div>
                <div class="content_body_information_center">
                  <div>编号：{{ item.pk }}号</div>
                  <div>
                    支持：<span class="count">{{ item.count }}</span>
                    <!-- 设置票数单位 -->
                    <span>{{
                      $store.state.settings[8].value
                        ? $store.state.settings[95].value
                        : "次"
                    }}</span>
                  </div>
                </div>
                <div class="content_body_information_right">
                  <div class="content_body_information_rightbox">
                    <img
                      class="content_body_information_viod"
                      v-if="index + 1 < 4"
                      :src="
                        require(`../assets/images/${
                          index + 1 === 1 ? 9 : index + 1 === 2 ? 13 : 17
                        }.png`)
                      "
                      alt=""
                    />
                    <!-- 点赞按钮 -->
                    <div
                      class="content_body_information_solid"
                      @click="like(item)"
                    >
                      {{
                        $store.state.settings[5].value
                          ? $store.state.settings[94].value
                          : "支持"
                      }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <img
              v-if="index + 1 < 5"
              style="width: 60px; height: 70px"
              class="content_body_information_top"
              :src="
                require(`../assets/images/${
                  index + 1 === 1
                    ? 7
                    : index + 1 === 2
                    ? 11
                    : index + 1 === 3
                    ? 15
                    : 19
                }.png`)
              "
              alt=""
            />
            <div v-else class="content_body_information_top1">
              <div class="content_body_information_square">{{ index + 1 }}</div>
              <div class="content_body_information_delta"></div>
            </div>
          </div>
        </div>
        <!-- 底部附加文字 -->
        <div class="copyright" v-if="$store.state.settings[2].value">
          {{ $store.state.settings[85].value }}
        </div>
        <!-- 隐藏底部技术支持信息 -->
        <div class="technicalsupport" v-if="$store.state.settings[6].value">
          {{ $store.state.settings[88].value }}
        </div>
        <div class="technicalsupport" v-if="$store.state.settings[39].value">
          {{ $store.state.settings[91].value }}
        </div>
      </div>
    </div>
    <div class="footer">
      <div class="footer_box">
        <div class="footer_item1">
          <img
            src="../assets/images/24.png"
            style="width: 35px; height: 50px"
            alt=""
          />
        </div>
        <div class="footer_item1">
          <img
            @click="customerSure"
            src="../assets/images/25.png"
            style="width: 35px; height: 50px"
            alt=""
          />
        </div>
        <div class="footer_item2 footer_color1">
          <button @click="activeRull">活动规则</button>
        </div>
        <div class="footer_item2 footer_color2">
          <button @click="goEnroll">我要报名</button>
        </div>
      </div>
    </div>
    <!-- 报名弹窗 -->
    <div class="enroll_prop" v-if="enrollStatus.isEnrollProp">
      <!-- 可以报名时 -->
      <div class="enroll_prop_form">
        <div>
          <h3>报名信息</h3>
          <div class="enroll_prop_form_item">
            <label>头像</label>
            <div style="display: flex">
              <input
                type="file"
                id="fileImage"
                ref="uploadImg"
                style="display: none"
                name="fileImage"
                @change="showImg"
              />
              <div @click="dispatchUpload" class="uploadReplace">
                <div>+</div>
              </div>
              <img
                id="headerImg"
                style="width: 104px; height: 104px"
                v-if="headerImg"
                :src="headerImg"
                alt=""
              />
            </div>
          </div>
          <div class="enroll_prop_form_item">
            <label>个人描述</label>
            <textarea
              name="textarea"
              @change="getDescribe"
              cols="50"
              rows="10"
            ></textarea>
          </div>
          <div class="enroll_prop_form_item">
            <label>选手名称</label>
            <input type="text" @change="athleteName" />
          </div>
          <div
            class="enroll_prop_form_item"
            v-if="$store.state.settings[7].value"
          >
            <label>手机号</label>
            <input type="text" @change="getPhone" />
          </div>
        </div>
        <div class="enroll_prop_form_button">
          <button style="color: black" @click="doenProp">取消</button>
          <button style="background-color: #409eff" @click="submit">
            确定
          </button>
        </div>
        <img
          class="downImg"
          @click="doenProp"
          style="width: 30px; height: 30px"
          src="../assets/images/39.png"
          alt=""
        />
      </div>
    </div>
    <div v-if="enrollStatus.isActiveRules" class="enroll_prop">
      <div class="enroll_prop_form">
        <div v-html="activeRules"></div>
        <img
          class="downImg"
          @click="doenProp"
          style="width: 30px; height: 30px"
          src="../assets/images/39.png"
          alt=""
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { fether } from "@/utils/fether";
import { reactive, ref, computed, onMounted } from "vue";
import base64 from "base-64";
import { useRoute, useRouter } from "vue-router";
import { useStore } from "vuex";
import { HOST, HOST2 } from "../ENV";
import athleteInformation from "@/components/athleteInformation.vue";
import customerService from "@/components/customerService.vue";
import isQrcode from "@/components/isQrcode.vue";
import WelcomeVue from "@/components/Welcome.vue";
import verificationCode from "@/components/verificationCode.vue";
import { isNetWork } from "../utils/network";
import Mobile from "mobile-detect";
const $route = useRoute();
const $router = useRouter();
const $store = useStore();
// 数据
const informationData = reactive([]);
const uploadImg = ref("");
const headerImg = ref("");
let activeRules = "";
let informationKey = 0;
let verificationCodeData = {};

const fileData = new FormData();

// 弹幕列表
const popupList = reactive({ data: [], showState: false });

// 表单数据
const enrollData = reactive({
  imgUrl: "",
  describe: "",
  athletename: "",
  file: fileData,
});

// 状态
const enrollStatus = reactive({
  isEnrollProp: false,
  isActiveRules: false,
  isAthleteConfig: false,
  iscustomerService: false,
  isOpenQscode: false,
  isVerificationCode: false,
  closeVerificationCode: () => {
    enrollStatus.isVerificationCode = false;
  },
});

// 是否显示欢迎回来页面
const welcomeState = reactive({
  state: false,
  value: "",
  ranking: 0,
  name: "",
  img: "",
  close: () => {
    welcomeState.state = false;
  },
});

//存储倒计时
const expireData = reactive({
  // 天
  day: "",
  // 时
  houers: "",
  // 分
  minute: "",
  //秒
  second: "",
});

//我要报名
const goEnroll = () => {
  //清除图片
  headerImg.value = "";
  // 获取现在时间
  let nowTime = new Date().getTime();
  // 获取报名开始时间
  let start_time = $store.state.settings[52].value * 1000;
  // 获取报名结束时间
  let end_time = $store.state.settings[53].value * 1000;
  // 判断是否在报名时间内
  // 未到报名时间
  if (nowTime < start_time) {
    alert("未到报名时间");
    // 报名结束
  } else if (nowTime > end_time) {
    alert("报名结束");
    // 可以报名
  } else {
    enrollStatus.isEnrollProp = !enrollStatus.isEnrollProp;
  }
};
// 取消弹窗
const doenProp = () => {
  if (enrollStatus.isEnrollProp === true) {
    enrollStatus.isEnrollProp = !enrollStatus.isEnrollProp;
  }
  if (enrollStatus.isActiveRules === true) {
    enrollStatus.isActiveRules = !enrollStatus.isActiveRules;
  }
};

// 客服
const customerSure = () => {
  console.log(1);
  enrollStatus.iscustomerService = true;
};

//获取子级传递过来的数据
const getChild = (value) => {
  enrollStatus.isAthleteConfig = value.status;
};
const getCusrr = () => {
  enrollStatus.iscustomerService = false;
};
const downQscode = () => {
  enrollStatus.isOpenQscode = false;
};
const downVerificationCode = () => {
  enrollStatus.isVerificationCode = false;
};

//获取选手列表
const getInformation = async () => {
  let result = await fether(`/votetarget/?vote_id=${$route.query.vote_id}`);
  result.map((item) => {
    informationData.push({ ...item.fields, pk: item.pk, model: item.model });
  });
  // 数组排序
  informationData.sort((a, b) => {
    return b.count - a.count;
  });
};
getInformation();

// 点击按钮分发到file click事件
const dispatchUpload = () => {
  let box = document.getElementById("fileImage");
  box.click();
};
//获取图片路径
const showImg = () => {
  let file = uploadImg.value.files[0];
  if (file.type !== "image/png") {
    alert("请上传图片类型文件");
    return;
  }
  const reads = new FileReader();
  reads.readAsDataURL(file);
  fileData.append("avator", file);
  reads.onload = function (e) {
    headerImg.value = e.target.result;
    enrollData.imgUrl = e.target.result;
  };
};

//获取描述数据
const getDescribe = (e) => {
  enrollData.describe = e.target.value;
};
//获取选手名称
const athleteName = (e) => {
  enrollData.athletename = e.target.value;
};
//获取手机号
const getPhone = (e) => {
  enrollData.phone_number = e.target.value;
};
//提交
const submit = async () => {
  let voteId = $route.query.vote_id;
  fileData.append("vote_id", voteId);
  if (enrollData.athletename.length) {
    fileData.append("name", enrollData.athletename);
  } else {
    alert("请输入选手名称");
  }
  if (enrollData.describe.length) {
    fileData.append("detail", enrollData.describe);
  } else {
    alert("请输入个人描述");
  }
  fetch(`${HOST}/votetarget/`, { method: "post", body: fileData })
    .then((res) => res.json())
    .then((data) => {
      if (data.code === 200) {
        enrollStatus.isEnrollProp = false;
      }
    });
};

const activeRull = async () => {
  enrollStatus.isActiveRules = !enrollStatus.isActiveRules;
  activeRules = $store.state.settings[78].value;
  console.log(activeRules);
};

// 点赞
const like = async (target) => {
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
    // 开启二维码弹幕
    if ($store.state.settings[26].value) {
      enrollStatus.isOpenQscode = true;
      // 开启验证码弹窗
    } else if ($store.state.settings[67].value) {
      enrollStatus.isVerificationCode = true;
      verificationCodeData.pk = target.pk;
      verificationCodeData.name = target.name;
      verificationCodeData.avator = target.avator;
    } else {
      // 没有开启验证码弹窗时点击直接发送点赞请求
      let keys = await getKey();
      let sercet = await encryption(keys);
      const md = new Mobile(navigator.userAgent);
      let result = await fether("/support/", "post", {
        data: {
          open_id: "wxtest6",
          vote_target_id: target.pk,
          vote_id: $route.query.vote_id,
          phone_model: md.mobile(),
          system: md.os(),
          network: isNetWork(),
          key: sercet,
        },
      });
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

const athleteConfig = (e, value) => {
  if (e.target.className === "content_body_information_center") {
    enrollStatus.isAthleteConfig = true;
    // $store.commit('changeAthlete', true)
    informationKey = value;
  }
};

// 支持轮播图
const isSupportCarouselAndStart = () => {
  if (!$store.state.settings[36].value) return;
  const JSONImgUrl = JSON.parse($store.state.settings[89].value);
  let flag = 0;
  let box = document.getElementById("Carousel");
  setInterval(() => {
    box.setAttribute(
      "style",
      `background-image: url(${HOST + "/media/" + JSONImgUrl[flag]});`
    );
    flag = flag + 1 > 2 ? 0 : flag + 1;
  }, 4000);
};

// 弹幕动画
const animating = () => {
  let JSONPopup = JSON.parse($store.state.settings[93].value);
  JSONPopup.forEach((item) => {
    popupList.data.push(
      JSONPopup[parseInt(Math.random(JSONPopup.length) * 10)]
    );
  });
  setInterval(() => {
    popupList.showState = !popupList.showState;
  }, 10000);
};

// 是否支持弹幕并且运行
const isPopupAndStart = () => {
  if (!$store.state.settings[26].value) return;
  // popupList.push()
  requestAnimationFrame(animating);
};

//获取活动倒计时
const getExpireTime = async () => {
  let result = $store.state.settings[48].value * 1000;
  // 获取现在正确时间
  let expireTimw = setInterval(() => {
    let nowTimw = new Date().getTime();
    // 时间差
    let D_value = result - nowTimw;
    // 当活动结束时停止定时器
    if (D_value === 0) {
      clearInterval(expireTimw);
    }
    expireData.day = Math.floor(D_value / 1000 / 60 / 60 / 24);
    expireData.houers = Math.floor((D_value / 1000 / 60 / 60) % 24);
    expireData.minute = Math.floor((D_value / 1000 / 60) % 60);
    expireData.second = Math.floor((D_value / 1000) % 60);
    // 补零
    if (expireData.day < 10) {
      expireData.day = `0${expireData.day}`;
    }
    if (expireData.houers < 10) {
      expireData.houers = `0${expireData.houers}`;
    }
    if (expireData.minute < 10) {
      expireData.minute = `0${expireData.minute}`;
    }
    if (expireData.second < 10) {
      expireData.second = `0${expireData.second}`;
    }
  }, 1000);
};

// 获取该投票用户最近一次投票时间
const getUserRecentVote = async () => {
  let result = await fether(`/recentvoterecord/?open_id=wxtest6`);
  if (result.length === 0) {
    welcomeState.state = false;
    return;
  }
  let currentStamp = new Date().getTime();
  let fromCurrentToLastTime =
    currentStamp - result[0].fields.create_time * 1000;
  console.log(fromCurrentToLastTime);
  if (fromCurrentToLastTime < 50000) return;
  for (let i = 0; i < informationData.length; i++) {
    if (result[0].fields.vote_target === informationData[i].pk) {
      welcomeState.ranking = i + 1;
      welcomeState.name = informationData[i].name;
      welcomeState.img = informationData[i].avator;
    }
  }
  console.log(fromCurrentToLastTime);
  welcomeState.value = parseInt(fromCurrentToLastTime / 60000);
  welcomeState.state = true;
};

onMounted(() => {
  getExpireTime();
  isSupportCarouselAndStart();
  isPopupAndStart();
  getUserRecentVote();
});
</script>

<style lang="scss" scoped>
.body {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}
.content {
  flex: 1;
  overflow-y: scroll;
}
.content_top {
  height: 200px;
  background-image: url("../assets/images/2.png");
  background-size: 100% 100%;
  background-repeat: no-repeat;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}
.content_top_center {
  width: 80%;
  height: 80%;
  background-image: url("../assets/images/1.png");
  background-size: 100% 100%;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #ffffff;
}
.content_body_persennum {
  display: flex;
  justify-content: space-between;
  padding: 0px 25px;
}
.content_body_persennum_item {
  width: 47%;
  padding: 10px 0px;
  display: flex;
  align-items: center;
  font-size: 10px;
  img {
    margin-right: 5px;
  }
  span {
    font-size: 15px;
    font-weight: 500;
    color: rgb(49, 60, 161);
  }
}
.content_body_search {
  display: flex;
  justify-content: space-between;
  background-color: #f3f3f3;
  padding: 15px;
  input {
    width: 65%;
    padding: 10px;
  }
}
.content_body_search_button {
  width: 95px;
  background-image: url("../assets/images/5.png");
  background-size: 100%;
  position: relative;
}
.content_body_search_status {
  position: absolute;
  z-index: 2;
  top: -9px;
  right: -10px;
  background-color: red;
  padding: 2px;
  color: #ffffff;
  border-radius: 5px 0px 5px 0px;
  font-size: 9px;
}
button {
  width: 100%;
  height: 100%;
  border: none;
  color: #ffffff;
  font-size: 14px;
}
.content_body_information_item {
  height: 175px;
  position: relative;
}
.content_body_information_top {
  position: absolute;
  z-index: 5;
  top: 5px;
  left: 20px;
}
// 绘制倒三角型
.content_body_information_top1 {
  position: absolute;
  z-index: 5;
  top: 15px;
  left: 30px;
  .content_body_information_square {
    width: 40px;
    height: 15px;
    line-height: 20px;
    background-color: green;
    text-align: center;
    color: #ffffff;
  }
  .content_body_information_delta {
    width: 0px;
    height: 0px;
    border-top: 10px solid green;
    border-left: 20px solid transparent;
    border-right: 20px solid transparent;
    border-bottom: 10px solid transparent;
  }
}
.content_body_information_background {
  position: absolute;
  height: 110%;
}
.content_body_information_body {
  width: calc(100% - 40px);
  position: absolute;
  z-index: 5;
  padding: 20px;
}
.content_body_information_title {
  display: flex;
  align-items: center;
  height: 35px;
  .content_body_information_name {
    margin-left: 10px;
    font-size: 20px;
  }
}
.content_body_information_content {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  margin-top: 10px;
}
.content_body_information_center {
  grid-column: span 2 / auto;
  display: flex;
  padding: 10px 0px;
  flex-direction: column;
  justify-content: space-around;
  .count {
    color: red;
    font-size: 20px;
    font-weight: 500;
  }
}
.content_body_information_left {
  height: 80px;
  padding: 10px;
}
.content_body_information_right {
  height: 100%;
  .content_body_information_rightbox {
    width: 100%;
    height: 100%;
    position: relative;
    .content_body_information_viod {
      height: 90%;
      position: absolute;
      z-index: -1;
      top: -25px;
    }
    .content_body_information_solid {
      height: 40px;
      margin-top: 15px;
      font-size: 16px;
      text-align: center;
      color: #ffffff;
      line-height: 40px;
      background-color: rgb(85, 85, 235);
    }
  }
}
.footer {
  padding: 10px;
}
.footer_box {
  height: 50px;
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  border: 1px solid #f3f3f3;
}
// 版权样式
.copyright {
  width: 100%;
  height: 30px;
  text-align: center;
  line-height: 30px;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
}
.footer_item2 {
  grid-column: span 2 / auto;
}
.footer_color1 > button {
  background-color: orange;
}
.footer_color2 > button {
  background-color: blue;
}

// 弹窗样式
.enroll_prop {
  position: absolute;
  top: 0px;
  right: 0;
  left: 0;
  bottom: 0;
  background-color: #00000074;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 5;
}
.enroll_prop_form {
  width: 80%;
  height: 80%;
  background-color: #ffffff;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.enroll_prop_form_item {
  display: flex;
  flex-direction: column;
  margin-bottom: 10px;
}
.enroll_prop_form_item > label {
  margin-bottom: 10px;
}
.enroll_prop_form_item > input {
  padding: 10px 0px;
}
.downImg {
  position: absolute;
  top: 5%;
  right: 5%;
}
.uploadReplace {
  height: 100px;
  width: 100px;
  border: 2px dashed #cecece;
  border-radius: 3px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  div {
    position: absolute;
    z-index: 2;
    font-size: 30px;
    color: #cecece;
  }
}
.enroll_prop_form_button {
  display: flex;
  justify-content: flex-end;
  button {
    width: 20%;
    height: 30px;
    margin-right: 10px;
  }
}

.content_top_titles {
  width: 50%;
  height: 2px;
  background-color: white;
  margin: 10px 0px;
}

.content_top_scroll_text {
  position: absolute;
  height: 30px;
  bottom: 8px;
  left: 0px;
  right: 0px;
  background-color: #cecece90;
  color: white;
  line-height: 30px;
  margin: 0 auto;
  width: calc(100vw);
  white-space: nowrap;
  overflow: hidden;
}
.scroll_text_content {
  font-size: 0;
  p {
    position: relative;
    display: inline-block;
    right: 100%;
    margin: 0;
    width: 100%;
    font-size: 16px;
    line-height: 20px;
    animation: scroll 10s infinite linear;
    overflow: hidden;
    white-space: nowrap;
    line-height: 30px;
  }
}
@keyframes scroll {
  0% {
    right: 100%;
  }
  100% {
    right: -200%;
  }
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

// 底部技术信息支持
.technicalsupport {
  height: 30px;
  line-height: 30px;
  text-align: center;
}
.content_top_popup {
  position: absolute;
  top: 0;
  bottom: 30px;
  left: 0;
  right: 0;
}

//活动倒计时样式
.expire_time {
  height: 50px;
  width: calc(100% - 40px);
  margin: 10px auto;
  border-radius: 10px;
  display: flex;
  align-items: center;
  //颜色渐变
  background-image: linear-gradient(
    to right,
    rgb(177, 13, 13),
    rgb(243, 103, 78)
  );
}
.expire_time_label {
  width: 25%;
  height: 20px;
  margin: 0px 5px;
  border: 1px solid #f3f3f3;
  text-align: center;
  color: #f3f3f3;
  font-size: 12px;
}
.expire_time_number {
  flex: 1;
  display: flex;
  color: #ffffff;
  font-size: 14px;
  div {
    padding: 0px 10px;
    background-color: yellow;
    border-radius: 5px;
    margin: 0px 5px;
    color: black;
  }
}
</style>
