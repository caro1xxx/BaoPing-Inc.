<template>
  <div id="siderbar_statistical_chart"></div>
</template>

<script>
import * as echarts from "echarts";

export default {
  data() {
    return {};
  },
  mounted() {
    const chartDom = document.getElementById("siderbar_statistical_chart");
    const myChart = echarts.init(chartDom);
    var option;

    option = {
      xAxis: {
        type: "category",
        data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
      },
      yAxis: {
        type: "value",
      },
      series: [
        {
          data: [120, 200, 150, 80, 70, 110, 130],
          type: "bar",
        },
      ],
    };

    option && myChart.setOption(option);
  },
};
</script>

<style lang="scss" scoped>
#siderbar_statistical_chart {
  margin: 0px 20px;
  width: 300px;
  height: 300px;
}
</style>
