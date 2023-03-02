<template>
    <div id="siderbar_statistical_chart2"></div>
  </template>
  
  <script setup>
  import * as echarts from "echarts"
  import { reactive, onMounted  } from "vue";
  onMounted(() => {
    const isBroken = reactive(['1月', '2月', '3月', '4月', '5月'])
    const isBrokenValue = reactive([20, 41, 15, 33, 25])
    const chartDom = document.getElementById('siderbar_statistical_chart2');
    var myChart = echarts.init(chartDom);
    var option;
    option = {
      title: {
        text: '标题'
      },
      tooltip: {
        trigger: 'axis'
      },
      xAxis: {
        type: 'category',
        data: isBroken
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          data: isBrokenValue,
          type: 'line'
        }
      ]
    };
    
    option && myChart.setOption(option);
  })
  </script>
  
  <style lang="scss" scoped>
  #siderbar_statistical_chart {
    margin: 0px 20px;
    width: 300px;
    height: 300px;
  }
  </style>
  