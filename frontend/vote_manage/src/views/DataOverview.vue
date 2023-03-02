<template>
  <div class="home">
    <Search />
    <div class="home_title">数据概括</div>
    <div class="top">
      <div class="home_top_title">
        <div class="home_top_title_font">今日</div>
        <div class="home_top_title_content">
          ¥{{ OverviewData.today_income }}.00
        </div>
      </div>
      <div style="border-left: 0.5px solid #c5c5c565"></div>
      <div class="home_top_title">
        <div class="home_top_title_font">昨日</div>
        <div class="home_top_title_content">
          ¥{{ OverviewData.yesterday_income }}.00
        </div>
      </div>
    </div>
    <div class="botton">
      <div class="botton_box">
        <StatisticalChart :data="boxChange" />
      </div>
      <div class="botton_box">
        <StatisticalChartOne :data="boxChange" />
      </div>
      <div class="botton_box">
        <StatisticalChartTwo :data="boxChange" />
      </div>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue";
import { reactive, onMounted } from "vue";
import { fether } from "@/utils/fether";
import { useStore } from "vuex";
import jsCookie from "js-cookie";
import StatisticalChart from '../components/StatisticalChart.vue'
import StatisticalChartOne from '../components/StatisticalChartOne.vue'
import StatisticalChartTwo from '../components/StatisticalChartTwo.vue'
const $store = new useStore();
const OverviewData = reactive({
  today_income: "",
  yesterday_income: "",
});

let boxChange = reactive({
  width: 0,
  height: 0
})

// 获取数据
const getDataOverView = async () => {
  // 开启加载loading
  await $store.dispatch("NoticifyActions", true);
  let result = await fether(`/statics/?token=${jsCookie.get("token")}`);
  if (result.code === 200) {
    let JSONResult = JSON.parse(result.data)[0].fields;
    OverviewData.today_income = JSONResult.today_income;
    OverviewData.yesterday_income = JSONResult.yesterday_income;
  } else {
    // 请求发送错误
    await $store.dispatch("refreshErroActions");
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
  // 关闭加载loading
  $store.commit("noticifyLoading", false);
};

getDataOverView();

onMounted(() => {
  let boxs = document.getElementsByClassName('botton_box')
  // setInterval(() => {
  //   boxChange.width = boxs[0].offsetWidth
  //   boxChange.height = boxs[0].offsetHeight
  // }, 3000)
})
</script>

<style lang="scss" scoped>
.home {
  width: calc(100vw - 250px - 40px);
  height: calc(100vh - 40px);
  font-size: 20px;
  padding: 20px;
}
.home_title {
  font-size: 20px;
  font-weight: bold;
  margin: 20px 0px;
}
.top {
  display: flex;
  .home_top_title {
    width: 50%;
    margin-left: 20px;
    border-bottom: 0.5px solid #c5c5c565;
  }

  .home_top_title_content {
    height: calc(20vh);
    font-size: 100px;
    font-weight: bold;
    line-height: calc(20vh);
  }
}
.home_top_title_font {
  font-size: 15px;
}
.midd {
  display: flex;
}
.home_top_title_sum {
  width: 50%;
}
.home_top_title_order {
  width: 25%;
  margin-left: 20px;
}
.botton{
  height: calc(80vh - 168px);
  display: flex;
  div{
    flex: 1;
    padding: 10px;
  }
}
</style>
