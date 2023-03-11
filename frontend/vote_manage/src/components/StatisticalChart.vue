<template>
  <div id="siderbar_statistical_chart"></div>
</template>

<script setup>
import * as echarts from "echarts";
import { reactive, watch } from "vue";
import { parseStampTime } from "../utils/stampTime.js";

// 接收数据
const props = defineProps({
  data: {
    width: Number,
    height: Number,
  },
  chartData: { income: Number, time: Number },
});

const isBroken = reactive([]);
const isBrokenValue = reactive([]);

watch(
  () => props.chartData,
  (newVal) => {
    props.chartData.forEach((item) => {
      isBroken.push(parseStampTime(item.time).replace("0:0", ""));
      isBrokenValue.push(item.income);
    });
    const chartDom = document.getElementById("siderbar_statistical_chart");
    var myChart = echarts.init(chartDom);
    var option;
    option = {
      title: {
        text: "近五日",
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
  },
  {
    deep: true,
  }
);
</script>

<style lang="scss" scoped>
#siderbar_statistical_chart {
  width: 100%;
  height: 100%;
}
</style>
