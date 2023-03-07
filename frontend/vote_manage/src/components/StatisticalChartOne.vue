<template>
  <div id="siderbar_statistical_chart1"></div>
</template>

<script setup>
import * as echarts from "echarts";
import { reactive, onMounted } from "vue";

// 接收数据
const props = defineProps({
  data: {
    width: Number,
    height: Number,
  },
});

console.log();
onMounted(() => {
  const isBroken = reactive(["1月", "2月", "3月", "4月", "5月"]);
  const isBrokenValue = reactive([20, 41, 15, 33, 25]);
  const chartDom = document.getElementById("siderbar_statistical_chart1");
  var myChart = echarts.init(chartDom);
  var option;
  option = {
    title: {
      text: "标题",
    },
    tooltip: {
      trigger: "axis",
    },
    xAxis: {
      type: "category",
      data: isBroken,
      name: "时间",
    },
    yAxis: {
      type: "value",
      name: "数量",
    },
    series: [
      {
        data: isBrokenValue,
        type: "line",
      },
    ],
  };

  option && myChart.setOption(option);
  // 监听浏览器页面缩放事件
  window.addEventListener("resize", function () {
    myChart.resize();
  });
});
</script>

<style lang="scss" scoped>
#siderbar_statistical_chart1 {
  width: 100%;
  height: 100%;
}
</style>
