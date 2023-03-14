<template>
  <div class="body">
    <div class="body_body">
      <div class="body_body_bar">
        <div
          v-for="item in head"
          :key="item.key"
          @click="onClickBar(item.key)"
          :style="{
            color: item.isClick ? '#2460e5' : '#000',
          }"
        >
          {{ item.name }}
        </div>
      </div>
      <div class="body_body_body" v-if="head[0].isClick">
        <div
          v-for="item in activitySettingOptions"
          :key="item.key"
          class="body_body_item"
        >
          <label>{{ item.label }}</label>
          <el-input
            v-if="item.type === 'text'"
            clearable
            v-model="item.value"
            placeholder="请输入"
          />
          <el-input-number
            v-else-if="item.type === 'number'"
            v-model="item.value"
            :min="0"
          />
          <el-date-picker
            v-else-if="item.type === 'date'"
            v-model="item.value"
            style="width: 95%"
            type="datetimerange"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
          />
          <el-time-picker
            v-else-if="item.type === 'time'"
            v-model="item.value"
            style="width: 95%"
            is-range
            range-separator="至"
            start-placeholder="开始时间"
            end-placeholder="结束时间"
          />
          <div v-else-if="item.type === 'limit'" style="margin: 5px 0px">
            <el-input
              class="limit"
              clearable
              v-model="item.value"
              placeholder="选手id"
            />
            <el-input
              class="limit"
              clearable
              v-model="item.value"
              placeholder="小时"
            />
            <el-input
              class="limit"
              clearable
              v-model="item.value"
              placeholder="达到票数"
            />
            <el-input
              class="limit"
              clearable
              v-model="item.value"
              placeholder="锁定分钟"
            />
          </div>
        </div>
      </div>
      <!-- 模板 -->
      <div class="body_body_body" v-else-if="head[1].isClick">
        <div class="body_body_item">
          <label>选择模板</label>
          <el-radio-group v-model="pageTemplate" class="ml-4">
            <el-radio label="1" size="large">模板1</el-radio>
            <el-radio label="2" size="large">模板2</el-radio>
          </el-radio-group>
          <div v-for="item in voteDetail" style="margin: 10px 0px">
            <label>{{ item.name }}</label>
            <div style="font-size: 13px; color: #cecece; position: relative">
              <div class="detailContent">{{ item.value }}</div>
              <span @click="showEidt(item.key)" class="editBtn">编辑</span>
            </div>
          </div>
        </div>
      </div>
      <div class="body_body_body" v-else-if="head[2].isClick">
        <div v-for="item in voteSetting" :key="item.key" class="body_body_item">
          <label>{{ item.label }}</label>
          <el-input
            v-if="item.type === 'text'"
            clearable
            v-model="item.value"
            placeholder="请输入"
          />
          <el-input-number
            v-else-if="item.type === 'number'"
            v-model="item.value"
            :min="1"
          />
          <el-date-picker
            v-else-if="item.type === 'date'"
            v-model="item.value"
            type="date"
            placeholder="选择日期"
          />
          <el-time-picker
            style="width: 95%"
            v-else-if="item.type === 'time'"
            v-model="item.value"
            placeholder="Arbitrary time"
          />
          <el-switch v-else-if="item.type === 'radio'" v-model="item.value" />
          <div v-else-if="item.type === 'limit'" style="margin: 5px 0px">
            <el-input
              class="limit"
              clearable
              v-model="item.value"
              placeholder="选手id"
            />
            <el-input
              class="limit"
              clearable
              v-model="item.value"
              placeholder="小时"
            />
            <el-input
              class="limit"
              clearable
              v-model="item.value"
              placeholder="达到票数"
            />
            <el-input
              class="limit"
              clearable
              v-model="item.value"
              placeholder="锁定分钟"
            />
          </div>
        </div>
      </div>
      <div class="body_body_body" v-else-if="head[3].isClick">
        <div v-for="item in autoMation" :key="item.key" class="body_body_item">
          <label>{{ item.label }}</label>
          <el-input
            v-if="item.type === 'text'"
            clearable
            v-model="item.value"
            placeholder="请输入"
          />
          <el-input-number
            v-else-if="item.type === 'number'"
            v-model="item.value"
            :min="1"
          />
          <el-date-picker
            v-else-if="item.type === 'date'"
            v-model="item.value"
            style="width: 95%"
            type="datetimerange"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
          />
          <el-time-picker
            v-else-if="item.type === 'time'"
            v-model="item.value"
            style="width: 95%"
            is-range
            range-separator="至"
            start-placeholder="开始时间"
            end-placeholder="结束时间"
          />
          <el-switch v-else-if="item.type === 'radio'" v-model="item.value" />
          <div v-else-if="item.type === 'limit'" style="margin: 5px 0px">
            <el-input
              class="limit"
              clearable
              v-model="item.value"
              placeholder="选手id"
            />
            <el-input
              class="limit"
              clearable
              v-model="item.value"
              placeholder="小时"
            />
            <el-input
              class="limit"
              clearable
              v-model="item.value"
              placeholder="达到票数"
            />
            <el-input
              class="limit"
              clearable
              v-model="item.value"
              placeholder="锁定分钟"
            />
          </div>
        </div>
      </div>
      <!-- 其他 -->
      <div class="body_body_body" v-else-if="head[4].isClick">
        <div
          v-for="(item, index) in others"
          :key="item.key"
          class="body_body_item"
        >
          <label>{{ item.label }}</label>
          <el-input
            v-if="item.type === 'text'"
            clearable
            :disabled="!item.value.state ? 'disabled' : null"
            v-model="item.value.value"
            :placeholder="
              item.value.state ? item.value.value : '全局设置已关闭该功能'
            "
          />
          <el-input-number
            v-else-if="item.type === 'number'"
            v-model="item.value.value"
            :min="1"
          />
          <el-date-picker
            v-else-if="item.type === 'date'"
            v-model="item.value.value"
            style="width: 95%"
            type="datetimerange"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
          />
          <el-time-picker
            v-else-if="item.type === 'time'"
            v-model="item.value.value"
            style="width: 95%"
            is-range
            range-separator="至"
            start-placeholder="开始时间"
            end-placeholder="结束时间"
          />
          <div v-else-if="item.type === 'file'" class="files">
            <div class="fileInput" @click="dipatchClick(item.key)">
              <input
                :id="'upload' + item.key"
                type="file"
                class="filebtn"
                @change="
                  uploadChange(item.mini, item.mini, item.key, item.name)
                "
              />
              <div style="width: 104px">+</div>
            </div>
            <div
              style="
                text-align: start;
                cursor: pointer;
                margin: 0px 10px;
                width: 60%;
              "
            >
              <div v-if="item.label !== '轮播图'" class="file_style">
                {{ item.value.value }}
                <svg
                  @click="deleteImg(item.key, index, '_')"
                  t="1678436892792"
                  class="icon"
                  viewBox="0 0 1024 1024"
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  p-id="1472"
                  width="15"
                  height="15"
                >
                  <path
                    d="M512 960c-247.039484 0-448-200.960516-448-448S264.960516 64 512 64 960 264.960516 960 512 759.039484 960 512 960zM512 128.287273c-211.584464 0-383.712727 172.128262-383.712727 383.712727 0 211.551781 172.128262 383.712727 383.712727 383.712727 211.551781 0 383.712727-172.159226 383.712727-383.712727C895.712727 300.415536 723.551781 128.287273 512 128.287273z"
                    fill="#d81e06"
                    p-id="1473"
                  ></path>
                  <path
                    d="M557.05545 513.376159l138.367639-136.864185c12.576374-12.416396 12.672705-32.671738 0.25631-45.248112s-32.704421-12.672705-45.248112-0.25631l-138.560301 137.024163-136.447897-136.864185c-12.512727-12.512727-32.735385-12.576374-45.248112-0.063647-12.512727 12.480043-12.54369 32.735385-0.063647 45.248112l136.255235 136.671523-137.376804 135.904314c-12.576374 12.447359-12.672705 32.671738-0.25631 45.248112 6.271845 6.335493 14.496116 9.504099 22.751351 9.504099 8.12794 0 16.25588-3.103239 22.496761-9.247789l137.567746-136.064292 138.687596 139.136568c6.240882 6.271845 14.432469 9.407768 22.65674 9.407768 8.191587 0 16.352211-3.135923 22.591372-9.34412 12.512727-12.480043 12.54369-32.704421 0.063647-45.248112L557.05545 513.376159z"
                    fill="#d81e06"
                    p-id="1474"
                  ></path>
                </svg>
              </div>
              <div v-else class="carooul">
                <div
                  v-for="(childItem, index) in item.value.value"
                  class="file_style"
                >
                  {{ childItem }}
                  <svg
                    @click="deleteImg(item.key, index, '轮播图')"
                    t="1678436892792"
                    class="icon"
                    viewBox="0 0 1024 1024"
                    version="1.1"
                    xmlns="http://www.w3.org/2000/svg"
                    p-id="1472"
                    width="15"
                    height="15"
                  >
                    <path
                      d="M512 960c-247.039484 0-448-200.960516-448-448S264.960516 64 512 64 960 264.960516 960 512 759.039484 960 512 960zM512 128.287273c-211.584464 0-383.712727 172.128262-383.712727 383.712727 0 211.551781 172.128262 383.712727 383.712727 383.712727 211.551781 0 383.712727-172.159226 383.712727-383.712727C895.712727 300.415536 723.551781 128.287273 512 128.287273z"
                      fill="#d81e06"
                      p-id="1473"
                    ></path>
                    <path
                      d="M557.05545 513.376159l138.367639-136.864185c12.576374-12.416396 12.672705-32.671738 0.25631-45.248112s-32.704421-12.672705-45.248112-0.25631l-138.560301 137.024163-136.447897-136.864185c-12.512727-12.512727-32.735385-12.576374-45.248112-0.063647-12.512727 12.480043-12.54369 32.735385-0.063647 45.248112l136.255235 136.671523-137.376804 135.904314c-12.576374 12.447359-12.672705 32.671738-0.25631 45.248112 6.271845 6.335493 14.496116 9.504099 22.751351 9.504099 8.12794 0 16.25588-3.103239 22.496761-9.247789l137.567746-136.064292 138.687596 139.136568c6.240882 6.271845 14.432469 9.407768 22.65674 9.407768 8.191587 0 16.352211-3.135923 22.591372-9.34412 12.512727-12.480043 12.54369-32.704421 0.063647-45.248112L557.05545 513.376159z"
                      fill="#d81e06"
                      p-id="1474"
                    ></path>
                  </svg>
                </div>
              </div>
            </div>
          </div>
          <el-switch
            v-else-if="item.type === 'radio'"
            v-model="item.value.switch"
            style="margin: 0px 10px"
          />
        </div>
      </div>
      <el-button style="color: #2460e5; width: 100%" @click="saveEditData"
        >保存</el-button
      >
      <img
        @click="
          () => {
            $store.dispatch('voteManagerActions', { target: '', state: 'put' });
          }
        "
        class="close"
        src="../assets/img/31.png"
        alt=""
      />
    </div>
    <Edit
      v-if="editValue.state"
      :data="{ value: editValue.value, close: editValue.close }"
    />
  </div>
</template>

<script setup>
import { HOST } from "@/ENV";
import { fether } from "@/utils/fether";
import jsCookie from "js-cookie";
import { reactive, ref, onMounted } from "vue";
import { useStore } from "vuex";
import { stampToUTCtime, timeToStamp } from "../utils/stampTime";
import Edit from "./Edit.vue";
const $store = new useStore();

// 获取localStorage内的活动数据
const getStorage = () => {
  let result = JSON.parse(localStorage.getItem("vote"));
  for (let i = 0; i < result.length; i++) {
    if (result[i].fields.vote_id === $store.state.voteManagePopup.target) {
      let obj = { ...result[i].fields };
      pageTemplate.value = obj.template_id + "";
      voteDetail[0].value = !obj.description ? "空" : obj.description;
      voteDetail[1].value = !obj.enterprises ? "空" : obj.enterprises;
      voteDetail[2].value = !obj.prize ? "空" : obj.prize;
      voteDetail[3].value = !obj.support ? "空" : obj.support;
      voteDetail[4].value = !obj.contact ? "空" : obj.contact;
      activitySettingOptions[0].value[0] = stampToUTCtime(obj.create_time);
      activitySettingOptions[0].value[1] = stampToUTCtime(obj.expire_time);
      activitySettingOptions[1].value[0] = stampToUTCtime(
        obj.vote_everyday_begin_time
      );
      activitySettingOptions[1].value[1] = stampToUTCtime(
        obj.vote_everyday_end_time
      );
      activitySettingOptions[2].value[0] = stampToUTCtime(
        obj.vote_enroll_begin_time
      );
      activitySettingOptions[2].value[1] = stampToUTCtime(
        obj.vote_enroll_end_time
      );
      activitySettingOptions[3].value = obj.name;
      activitySettingOptions[4].value = obj.allowed_vote_region
        ? obj.allowed_vote_region
        : "全国";
      activitySettingOptions[5].value = obj.visit_count;
      activitySettingOptions[6].value = obj.visit_count_multiple;
      // voteSetting[0].value = obj.vote_count_restrict;
      voteSetting[1].value = obj.today_start_voteuser
        ? obj.today_start_voteuser
        : "空";
      voteSetting[2].value = stampToUTCtime(obj.today_star_update_begin_time);
      voteSetting[3].value = obj.allowed_alone_everyday_vote_count;
      voteSetting[4].value = obj.allowed_alone_everyhour_vote_count;
      voteSetting[5].value = obj.open_today_star_with * 1000;
      voteSetting[6].value = obj.visible_no1_with === 1 ? true : false;
      voteSetting[7].value = obj.enable_vote_to_me === 1 ? true : false;
      voteSetting[8].value = obj.enable_comment === 1 ? true : false;
      voteSetting[9].value = obj.enable_vote_cert_code === 1 ? true : false;
      voteSetting[10].value = obj.enable_prize === 1 ? true : false;
      voteSetting[11].value = obj.enable_browser === 1 ? true : false;
      autoMation[0].value = obj.auto_comment_voteuser
        ? obj.auto_comment_voteuser
        : "空";
      autoMation[1].value[0] = stampToUTCtime(obj.auto_comment_begin_time);
      autoMation[1].value[1] = stampToUTCtime(obj.auto_comment_end_time);
      autoMation[2].value[0] = stampToUTCtime(
        obj.auto_comment_everyday_begin_time
      );
      autoMation[2].value[1] = stampToUTCtime(
        obj.auto_comment_everyday_end_time
      );
      autoMation[3].value = obj.auto_comment_space_minute;
      autoMation[4].value = obj.auto_comment_everyday_count_strict;
      others[0].value.value = obj.top_roll_text;
      others[1].value.value = obj.bottom_text;
      others[2].value.value = obj.bottom_support_text;
      others[3].value.value = obj.bottom_copyright;
      others[4].value.value = obj.popup;
      others[5].value.value = obj.vote_button_name;
      others[6].value.value = obj.vote_unit_name;
      others[7].value.value = obj.track_report;
      others[8].value.value = obj.video_adv;
      others[9].value.value = obj.target_video_adv;
      others[10].value.value = JSON.parse(obj.carousel_list);
      others[11].value.value = obj.start_adv_img;
      others[12].value.value = obj.officialcount_qrcode;
      break;
    }
  }
};

// bar
const head = reactive([
  { name: "活动设置", key: 1, isClick: true, label: "activity_settings" },
  { name: "页面设置", key: 2, isClick: false, label: "style" },
  { name: "投票设置", key: 3, isClick: false, label: "vote_settings" },
  { name: "自动化", key: 4, isClick: false, label: "auto_comment_settings" },
  { name: "其他", key: 5, isClick: false, label: "other" },
]);

// 活动设置
const activitySettingOptions = reactive([
  { label: "活动起始时间", key: 1, value: [], type: "date" },
  { label: "每天投票时间", key: 2, value: [], type: "time" },
  { label: "报名日期", key: 3, value: [], type: "date" },
  { label: "活动名称", key: 4, value: "", type: "text" },
  {
    label: "允许投票区域(如只允许重庆的投票,那么就输入重庆)",
    key: 5,
    value: "",
    type: "text",
  },
  { label: "浏览量", key: 8, value: "", type: "number" },
  { label: "浏览倍数", key: 9, value: "", type: "number" },
]);

// 投票设置
const voteSetting = reactive([
  {
    label: "",
    key: 1,
    value: "[]",
    type: "abc",
  },
  { label: "今日之星选手id(选手id)", key: 7, value: "", type: "text" },
  { label: "每日今日之星更新时间", key: 5, value: "", type: "time" },
  { label: "每人单日投票上限", key: 2, value: "", type: "number" },
  { label: "用户每小时投票上限", key: 3, value: "", type: "number" },
  { label: "开启今日之星日期", key: 4, value: "", type: "date" },
  { label: "第*天显示第一名", key: 6, value: "", type: "number" },
  { label: "给自己投票", key: 8, value: "", type: "radio" },
  { label: "留言", key: 9, value: "", type: "radio" },
  { label: "投票验证码", key: 10, value: "", type: "radio" },
  { label: "礼物", key: 11, value: "", type: "radio" },
  { label: "浏览器投票", key: 12, value: "", type: "radio" },
]);

// 模板
const pageTemplate = ref(1);

const voteDetail = reactive([
  { name: "活动说明", value: "空", key: 0 },
  { name: "荣入企业", value: "空", key: 1 },
  { name: "荣誉奖品", value: "空", key: 2 },
  { name: "支持方式", value: "空", key: 3 },
  { name: "联系方式", value: "空", key: 4 },
]);

const editValue = reactive({
  state: false,
  value: "",
  currentVoteOptionsKey: 0,
  close: (change) => {
    voteDetail[editValue.currentVoteOptionsKey].value = change ? change : "空";
    editValue.state = false;
    saveEditData();
  },
});

// 自动化
const autoMation = reactive([
  { label: "自动评论选手id(选手id)", key: 1, value: "", type: "text" },
  { label: "自动评论起始日期", key: 2, value: [], type: "date" },
  { label: "每日评论起始时间", key: 2, value: [], type: "time" },
  { label: "每*分钟1条评论", key: 2, value: "", type: "number" },
  { label: "每日评论上限", key: 3, value: "", type: "number" },
]);

// 其他
const others = reactive([
  {
    label: "设置顶部滚动文字",
    key: 1,
    value: { state: false, value: "" },
    type: "text",
  },
  {
    label: "设置底部附加文字",
    key: 3,
    value: { state: false, value: "" },
    type: "text",
  },
  {
    label: "底部技术支持信息",
    key: 6,
    value: { state: false, value: "" },
    type: "text",
  },
  {
    label: "设置底部版权",
    key: 8,
    value: { state: false, value: "" },
    type: "text",
  },
  {
    label: "弹幕",
    key: 10,
    value: { state: false, value: "" },
    type: "text",
  },
  {
    label: "设置投票按钮名称",
    key: 11,
    value: { state: false, value: "" },
    type: "text",
  },
  {
    label: "设置票数单位",
    key: 12,
    value: { state: false, value: "" },
    type: "text",
  },
  {
    label: "追踪报道链接",
    key: 13,
    value: { state: false, value: "" },
    type: "text",
  },
  {
    label: "首页视频广告",
    key: 4,
    value: { state: false, value: "" },
    type: "file",
    mini: "video/mp4",
    name: "refone",
  },
  {
    label: "选手页视频广告",
    key: 5,
    value: { state: false, value: "" },
    type: "file",
    mini: "video/mp4",
    name: "reftwo",
  },
  {
    label: "轮播图",
    key: 7,
    value: { state: false, value: "" },
    type: "file",
    mini: "image/png",
    name: "reffour",
  },
  {
    label: "开场广告图",
    key: 2,
    value: { state: false, value: "" },
    type: "file",
    mini: "image/png",
    name: "reffour",
  },
  {
    label: "投票结果展示公众号二维码",
    key: 9,
    value: { state: false, value: "" },
    type: "file",
    mini: "image/png",
    name: "reffive",
  },
]);

// 显示文本编辑器
const showEidt = (key) => {
  editValue.currentVoteOptionsKey = key;
  editValue.value = voteDetail[key].value;
  editValue.state = true;
};

// 点击head
const onClickBar = (key) => {
  head.forEach((item, index) => {
    if (item.key === key) {
      head[index].isClick = true;
    } else {
      head[index].isClick = false;
    }
  });
};

// 保存数据
const saveEditData = async () => {
  for await (let i of head) {
    if (i.isClick) {
      let data = {};
      if (i.label === "activity_settings") {
        data = {
          content: i.label,
          vote_id: $store.state.voteManagePopup.target,
          create_time: timeToStamp(
            activitySettingOptions[0].value[0]
          ),
          expire_time: timeToStamp(
            activitySettingOptions[0].value[1]
          ),
          name: activitySettingOptions[3].value,
          vote_everyday_begin_time: timeToStamp(
            activitySettingOptions[1].value[0]
          ),
          vote_everyday_end_time: timeToStamp(
            activitySettingOptions[1].value[1]
          ),
          vote_enroll_begin_time: timeToStamp(
            activitySettingOptions[2].value[0]
          ),
          vote_enroll_end_time: timeToStamp(activitySettingOptions[2].value[1]),
          allowed_vote_region: activitySettingOptions[4].value,
          visit_count: activitySettingOptions[5].value,
          visit_count_multiple: activitySettingOptions[6].value,
        };
      } else if (i.label === "vote_settings") {
        data = {
          content: "vote_settings",
          vote_id: $store.state.voteManagePopup.target,
          vote_count_restrict: voteSetting[0].value,
          today_start_voteuser_open_id:
            voteSetting[1].value === "空" ? "" : voteSetting[1].value,
          today_star_update_begin_time: timeToStamp(voteSetting[2].value),
          today_star_update_end_time: 123123213,
          allowed_alone_everyday_vote_count: voteSetting[3].value,
          allowed_alone_everyhour_vote_count: voteSetting[4].value,
          open_today_star_with: new Date(voteSetting[5].value).getTime() / 1000,
          visible_no1_with: voteSetting[6].value ? 1 : 0,
          enable_vote_to_me: voteSetting[7].value ? 1 : 0,
          enable_comment: voteSetting[8].value ? 1 : 0,
          enable_vote_cert_code: voteSetting[9].value ? 1 : 0,
          enable_prize: voteSetting[10].value ? 1 : 0,
          enable_browser: voteSetting[11].value ? 1 : 0,
        };
      } else if (i.label === "auto_comment_settings") {
        data = {
          content: "auto_comment_settings",
          vote_id: $store.state.voteManagePopup.target,
          auto_comment_voteuser_open_id:
            autoMation[0].value === "空" ? "" : autoMation[0].value,
          auto_comment_begin_time: timeToStamp(autoMation[1].value[0]),
          auto_comment_end_time: timeToStamp(autoMation[1].value[1]),
          auto_comment_everyday_begin_time: timeToStamp(autoMation[2].value[0]),
          auto_comment_everyday_end_time: timeToStamp(autoMation[2].value[1]),
          auto_comment_space_minute: autoMation[3].value,
          auto_comment_everyday_count_strict: autoMation[4].value,
        };
      } else if (i.label === "style") {
        data = {
          content: "template",
          template_id: pageTemplate.value,
          vote_id: $store.state.voteManagePopup.target,
          description: voteDetail[0].value ? voteDetail[0].value : "空",
          enterprises: voteDetail[1].value ? voteDetail[1].value : "空",
          prize: voteDetail[2].value ? voteDetail[2].value : "空",
          support: voteDetail[3].value ? voteDetail[3].value : "空",
          contact: voteDetail[4].value ? voteDetail[4].value : "空",
        };
      } else {
        data = {
          content: "other",
          vote_id: $store.state.voteManagePopup.target,
          top_roll_text: others[0].value.value,
          bottom_text: others[1].value.value,
          bottom_support_text: others[2].value.value,
          bottom_copyright: others[3].value.value,
          vote_button_name: others[5].value.value,
          vote_unit_name: others[6].value.value,
          popup: others[4].value.value,
          track_report: others[7].value.value,
          video_adv: others[8].value.value,
          target_video_adv: others[9].value.value,
          officialcount_qrcode: others[12].value.value,
          carousel_list: JSON.stringify(others[10].value.value),
          start_adv_img: others[11].value.value,
        };
      }
      let result = await fether("/voteactivity/", "put", {
        token: jsCookie.get("token"),
        data: data,
      });
      if (result.code === 200) {
        // 保存成功提醒
        await $store.dispatch("GlobalMessageActions", "操作成功");
        let localData = JSON.parse(localStorage.getItem("vote"));
        for (let i = 0; i < localData.length; i++) {
          if (
            localData[i].fields.vote_id === $store.state.voteManagePopup.target
          ) {
            localData[i].fields = { ...localData[i].fields, ...data };
            localStorage.setItem("vote", JSON.stringify(localData));
            break;
          }
        }
      } else {
        // 请求发送错误
        await $store.dispatch("GlobalMessageActions", "操作失败,请重试");
      }
    }
  }
};

// 获取全局设置
const getGlobalSettings = async () => {
  let result = await fether(`/settings/?token=${jsCookie.get("token")}`);
  if (result.code === 200) {
    let JSONResult = JSON.parse(result.data);
    others.forEach((item, index) => {
      for (let i = 0; i < JSONResult.length; i++) {
        if (JSONResult[i].fields.name === item.label) {
          others[index].value.state =
            JSONResult[i].fields.value === "1" ? true : false;
          break;
        }
      }
    });
  } else {
    await $store.dispatch("GlobalMessageActions", result.msg);
  }
};

// 传递click事件给input
const dipatchClick = (index) => {
  let box = document.getElementById("upload" + index);
  box.click();
};

// 上传改变
const uploadChange = (type, typeStr, index, name) => {
  let file = document.getElementById("upload" + index).files[0];
  if (file.type !== type) {
    $store.dispatch("GlobalMessageActions", `请上传${type}类型的文件`);
    return;
  }
  const reads = new FileReader();
  reads.readAsDataURL(file);
  reads.onload = function (e) {
    uploaderFIles(typeStr, index, file);
  };
};

// 上传临时文件
const uploaderFIles = async (type, key, files) => {
  let form = new FormData();
  form.append("file", files);
  form.append("category", type.split("/")[0] === "image" ? "img" : "video");
  fetch(`${HOST}/uploadfile/`, { method: "post", body: form })
    .then((res) => res.json())
    .then((data) => {
      if (data.code === 200) {
        others.forEach((item, index) => {
          if (item.key === key) {
            if (key === 7) others[index].value.value.push(data.data.filename);
            else others[index].value.value = data.data.filename;
          }
        });
      }
    });
};

// 删除图片
const deleteImg = (key, no, type) => {
  others.forEach((item, index) => {
    if (item.key === key) {
      if (type === "轮播图") {
        others[index].value.value.splice(no, 1);
      } else {
        others[index].value.value = "";
      }
    }
  });
};

getStorage();
onMounted(() => {
  getGlobalSettings();
});
</script>

<style lang="scss" scoped>
.body {
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
.body_body {
  width: calc(30vw);
  background-color: white;
  border-radius: 3px;
  padding: 20px;
  position: relative;
}
.body_body_bar {
  display: flex;
  div {
    font-size: 15px;
    width: 20%;
    margin-bottom: 10px;
    cursor: pointer;
  }
  border-bottom: 2px solid #d4d4d474;
}
.body_body_body {
  margin: 10px 0px;
  height: calc(80vh - 120px);
  overflow: scroll;
}
.body_body_body::-webkit-scrollbar {
  display: none;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}
.body_body_item {
  margin: 10px 0px;
  label {
    display: block;
    font-size: 13px;
    margin-bottom: 5px;
  }
  input {
    outline: none;
    border: 1px solid #e6e6e6;
    border-radius: 3px;
    width: 99%;
    height: 25px;
  }
}
.limit {
  width: 20%;
  margin: 0px 5px;
}
.close {
  position: absolute;
  right: -50px;
  top: 0;
  width: 30px;
  height: 30px;
  z-index: 5;
}
.detailContent {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 80%;
}
.editBtn {
  position: absolute;
  color: #3f9eff;
  cursor: pointer;
  top: 0px;
  right: 10px;
}
.fileInput {
  width: 100px;
  height: 100px;
  border: 2px dashed #cecece;
  border-radius: 3px;
  text-align: center;
  line-height: 100px;
  font-size: 20px;
  color: #cecece;
  cursor: pointer;
}
.filebtn {
  display: none;
}
.files {
  display: flex;
  color: #cecece;
}
.file_style {
  border-radius: 5px;
  line-height: 20px;
  font-size: 10px;
  padding: 0px 10px;
  margin: 5px;
  position: relative;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  box-shadow: 0 4px 4px 0 rgba(191, 191, 191, 0.2),
    0 4px 4px 0 rgba(183, 183, 183, 0.19);
  svg {
    position: absolute;
    right: 5px;
    top: 2px;
  }
}
.carooul {
  height: 100px;
  overflow: scroll;
}
</style>
