<template>
  <div class="siderbar">
    <div class="siderbar_heater">
      <img class="siderbar_img" src="../assets/img/header.webp" alt="" />
      <span class="siderbar_name">Admin</span>
    </div>
    <div class="siderbar_statistical_chart_box">
      <StatisticalChart />
    </div>
    <div class="siderbar_operation_log">
      <span class="siderbar_operation_log_name">操作日志</span>
      <div class="siderbar_operation_log_content">
        <div
          class="siderbar_operation_log_list"
          v-for="(item, index) in logList"
        >
          <img class="siderbar_img" :src="item.url" alt="" />
          <div>
            <div class="siderbar_operation_log_box">
              <span class="siderbar_operation_log_user">{{
                item.username
              }}</span>
              <span class="siderbar_operation_log_time">{{ item.time }}</span>
            </div>
            <span class="siderbar_operation_log_movement">
              <span class="siderbar_operation_log_time">{{ item.action }}</span>
              <span class="siderbar_operation_log_user">{{
                item.project
              }}</span>
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StatisticalChart from "./StatisticalChart.vue";
export default {
  data() {
    return {
      // 操作日志列表
      logList: [
        {
          username: "admin",
          time: "今天10:30",
          action: "admin增加了",
          project: "活动3",
          url: require("../assets/img/header.webp"),
        },
        {
          username: "admin",
          time: "今天10:30",
          action: "admin增加了",
          project: "活动3",
          url: require("../assets/img/header.webp"),
        },
        {
          username: "admin",
          time: "今天10:30",
          action: "admin增加了",
          project: "活动3",
          url: require("../assets/img/header.webp"),
        },
        {
          username: "admin",
          time: "今天10:30",
          action: "admin增加了",
          project: "活动3",
          url: require("../assets/img/header.webp"),
        },
        {
          username: "admin",
          time: "今天10:30",
          action: "admin增加了",
          project: "活动3",
          url: require("../assets/img/header.webp"),
        },
        {
          username: "admin",
          time: "今天10:30",
          action: "admin增加了",
          project: "活动3",
          url: require("../assets/img/header.webp"),
        },
        {
          username: "admin",
          time: "今天10:30",
          action: "admin增加了",
          project: "活动3",
          url: require("../assets/img/header.webp"),
        },
        {
          username: "admin",
          time: "今天10:30",
          action: "admin增加了",
          project: "活动3",
          url: require("../assets/img/header.webp"),
        },
        {
          username: "admin",
          time: "今天10:30",
          action: "admin增加了",
          project: "活动3",
          url: require("../assets/img/header.webp"),
        },
        {
          username: "admin",
          time: "今天10:30",
          action: "admin增加了",
          project: "活动3",
          url: require("../assets/img/header.webp"),
        },
        {
          username: "admin",
          time: "今天10:30",
          action: "admin增加了",
          project: "活动3",
          url: require("../assets/img/header.webp"),
        },
      ],
    };
  },
  components: {
    StatisticalChart,
  },
  methods: {},
};
</script>

<style lang="scss" scoped>
.siderbar {
  width: 400px;
  height: calc(100vh);
  padding-right: 20px;
}
.siderbar_heater {
  height: 40px;
  margin-top: 24px;
  display: flex;
  align-items: flex-end;
  padding-left: 20px;
}
.siderbar_name {
  margin-left: 20px;
  color: #000;
  font-size: 15px;
  font-weight: 20px;
}
.siderbar_statistical_chart_box {
  margin-top: 15px;
}
.siderbar_operation_log_name {
  padding-left: 20px;
  font-size: 15px;
  color: #b5c3d1;
}
.siderbar_operation_log_content {
  padding-left: 20px;
  margin-top: 20px;
  height: calc(100vh - 500px);
  overflow-y: scroll;
}
// 清除滚动条样式
.siderbar_operation_log_content::-webkit-scrollbar {
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
  display: none;
}
.siderbar_operation_log_list {
  display: flex;
  height: 59px;
  margin-bottom: 15px;
}
.siderbar_operation_log_box {
  width: 360px;
  height: 29px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.siderbar_operation_log_user {
  color: #000;
  font-size: 15px;
  font-weight: 20px;
}
.siderbar_operation_log_time {
  color: #b5c3d1;
  font-size: 15px;
}
.siderbar_operation_log_movement {
  height: 30px;
  display: flex;
  align-items:flex-end;
}
</style>
