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
      <!-- 投票页面样式 -->
      <div class="body_body_body" v-else-if="head[1].isClick">
        <div class="body_body_style">
          <div class="body_body_style_body">
            <div
              class="child_top"
              @click="onSelectStyle('topImg')"
              :style="{ border: voteStyle.topImg ? '2px dashed #2460e5' : '' }"
            >
              1
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
  </div>
</template>

<script setup>
import { fether } from "@/utils/fether";
import jsCookie from "js-cookie";
import { reactive } from "vue";
import { useStore } from "vuex";
import { stampToUTCtime, timeToStamp } from "../utils/stampTime";
const $store = new useStore();

// 获取localStorage内的活动数据
const getStorage = () => {
  let result = JSON.parse(localStorage.getItem("vote"));
  for (let i = 0; i < result.length; i++) {
    if (result[i].fields.vote_id === $store.state.voteManagePopup.target) {
      let obj = { ...result[i].fields };
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
      activitySettingOptions[5].value = obj.flow;
      activitySettingOptions[6].value = obj.visit_count_multiple;
      voteSetting[0].value = obj.vote_count_restrict;
      voteSetting[1].value = obj.today_start_voteuser
        ? obj.today_start_voteuser
        : "空";
      voteSetting[2].value[0] = stampToUTCtime(
        obj.today_star_update_begin_time
      );
      voteSetting[2].value[1] = stampToUTCtime(
        obj.today_star_update_begin_time
      );
      voteSetting[3].value = obj.allowed_alone_everyday_vote_count;
      voteSetting[4].value = obj.allowed_alone_everyhour_vote_count;
      voteSetting[5].value = obj.open_today_star_with;
      voteSetting[6].value = obj.visible_no1_with;
      voteSetting[7].value = obj.enable_vote_to_me;
      voteSetting[8].value = obj.enable_comment;
      voteSetting[9].value = obj.enable_vote_cert_code;
      voteSetting[10].value = obj.enable_prize;
      voteSetting[11].value = obj.enable_browser;
      autoMation[0].value = obj.auto_comment_voteuser
        ? auto_comment_voteuser
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
      break;
    }
  }
};

const clg = () => {
  console.log(
    new Date(Date.parse(activitySettingOptions[1].value[0].toString())),
    new Date(Date.parse(activitySettingOptions[1].value[1].toString()))
  );
};

// bar
const head = reactive([
  { name: "活动设置", key: 1, isClick: true, label: "activity_settings" },
  { name: "活动样式", key: 2, isClick: false, label: "style" },
  { name: "投票设置", key: 3, isClick: false, label: "vote_settings" },
  { name: "自动化", key: 4, isClick: false, label: "auto_comment_settings" },
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
    label: "票数限制(*选手票数在*小时内达到*票后锁定*分钟)",
    key: 1,
    value: "{}",
    type: "limit",
  },
  { label: "今日之星选手id(openid)", key: 7, value: "", type: "text" },
  { label: "每日今日之星更新时间", key: 5, value: [], type: "time" },
  { label: "每人单日投票上限", key: 2, value: "", type: "number" },
  { label: "用户每小时投票上限", key: 3, value: "", type: "number" },
  { label: "第*天开启今日之星", key: 4, value: "", type: "number" },
  { label: "第*天显示第一名", key: 6, value: "", type: "number" },
  { label: "给自己投票", key: 8, value: "", type: "radio" },
  { label: "留言", key: 9, value: "", type: "radio" },
  { label: "投票验证码", key: 10, value: "", type: "radio" },
  { label: "礼物", key: 11, value: "", type: "radio" },
  { label: "浏览器投票", key: 12, value: "", type: "radio" },
]);
// 自动化
const autoMation = reactive([
  { label: "自动评论选手id(openid)", key: 1, value: "", type: "text" },
  { label: "自动评论起始日期", key: 2, value: [], type: "date" },
  { label: "每日评论起始时间", key: 2, value: [], type: "time" },
  { label: "每*分钟1条评论", key: 2, value: "", type: "number" },
  { label: "每日评论上限", key: 3, value: "", type: "number" },
]);

const voteStyle = reactive({ topImg: false });

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

// 鼠标移入
const onSelectStyle = (target) => {
  for (let i in voteStyle) {
    if (i === target) {
      voteStyle[i] = !voteStyle[i];
    } else {
      voteStyle[i] = false;
    }
  }
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
          today_star_update_begin_time: timeToStamp(voteSetting[2].value[0]),
          today_star_update_end_time: timeToStamp(voteSetting[2].value[1]),
          allowed_alone_everyday_vote_count: voteSetting[3].value,
          allowed_alone_everyhour_vote_count: voteSetting[4].value,
          open_today_star_with: voteSetting[5].value,
          visible_no1_with: voteSetting[6].value ? 1 : 0,
          enable_vote_to_me: voteSetting[7].value ? 1 : 0,
          enable_comment: voteSetting[8].value ? 1 : 0,
          enable_vote_cert_code: voteSetting[9].value ? 1 : 0,
          enable_prize: voteSetting[10].value ? 1 : 0,
          enable_browser: voteSetting[11].value ? 1 : 0,
        };
      } else if (i.label === "auto_comment_settings") {
      } else {
      }
      let result = await fether("/voteactivity/", "put", {
        token: jsCookie.get("token"),
        data: data,
      });
      console.log(result);
    }
  }
};

getStorage();
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
  height: calc(80vh - 40px);
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
.body_body_style {
  display: flex;
  align-items: center;
  justify-content: center;
}
.body_body_style_body {
  width: 80%;
  height: 700px;
  background-color: green;
}
.child_top {
  height: 150px;
  background: rgb(252, 219, 11);
  background: linear-gradient(
    90deg,
    rgba(252, 219, 11, 1) 0%,
    rgba(238, 180, 47, 1) 35%,
    rgba(209, 255, 0, 1) 100%
  );
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  color: white;
}
.close {
  position: absolute;
  right: -50px;
  top: 0;
  width: 30px;
  height: 30px;
  z-index: 5;
}
</style>
