<template>
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
          <div style="font-size: 20px">新乡市消防技术公司</div>
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
      </div>
      <div class="content_body">
        <div class="content_body_persennum">
          <div class="content_body_persennum_item">
            <img
              :style="{ width: '20px', height: '22px' }"
              src="../assets/images/3.png"
              alt=""
            />访问数：<span>2.5w</span>
          </div>
          <div class="content_body_persennum_item">
            <img
              :style="{ width: '20px', height: '22px' }"
              src="../assets/images/4.png"
              alt=""
            />报名数：<span>45</span>
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
                    支持：<span>{{ item.count }}</span
                    >次
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
                    <img
                      @click="like(item)"
                      class="content_body_information_solid"
                      :src="
                        require(`../assets/images/${
                          index + 1 === 1 ? 8 : 12
                        }.png`)
                      "
                      alt=""
                    />
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
        <div ref="activeRules" v-html="activeRules"></div>
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
import isQrcode from '@/components/isQrcode.vue'
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

const fileData = new FormData();

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
  isOpenQscode: false
});

//我要报名
const goEnroll = () => {
  enrollStatus.isEnrollProp = !enrollStatus.isEnrollProp;
  //清除图片
  headerImg.value = "";
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
  enrollStatus.isOpenQscode = false
}

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
  activeRules = $store.state.settings.get("description");
};

// 点赞
const like = async (target) => {
  // 开启二维码弹幕
  enrollStatus.isOpenQscode = true
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

const athleteConfig = (e, value) => {
  if (e.target.tagName === "DIV") {
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

onMounted(() => {
  isSupportCarouselAndStart();
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
  span {
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
      padding-top: 15px;
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
</style>
