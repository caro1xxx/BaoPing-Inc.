<template>
  <div class="body">
    <div class="content">
      <div class="content_top">
        <div class="content_top_center">
          <div style="font-size: 20px;">新乡市消防技术公司</div>
          <div style="width: 50%;height: 2px;background-color: white;margin: 10px 0px;"></div>
          <div>优秀企业推荐</div>
        </div>
      </div>
      <div class="content_body">
        <div class="content_body_persennum">
          <div class="content_body_persennum_item"><img :style="{ width: '20px',height: '24px' }" src="../assets/images/3.png" alt="">访问数：<span>2.5w</span></div>
          <div class="content_body_persennum_item"><img :style="{ width: '20px',height: '24px' }" src="../assets/images/4.png" alt="">报名数：<span>45</span></div>
        </div>
        <div class="content_body_search">
          <input type="text" placeholder="搜索名称或编号" />
          <div class="content_body_search_button">
            <div class="content_body_search_text"></div>
            <div class="content_body_search_status">已更新</div>
          </div>
        </div>
        <div class="content_body_information">
          <div class="content_body_information_item"
            v-for="(item, index) in informationData" :key="index">
            <img class="content_body_information_background"
            :src="require(`../assets/images/${(index + 1) === 1 ? 6 : (index + 1) === 2 ? 10 : (index + 1) === 3 ? 14 : 21}.png`)" alt="">
            <div class="content_body_information_body">
              <div class="content_body_information_title">
                <div style="width: 80px;"></div>
                <div v-if="(index + 1) > 2" class="content_body_information_name">{{ item.informationName }}</div>
              </div>
              <div class="content_body_information_content">
                <div class="content_body_information_left">
                  <img :src="item.imgUrl" alt="">
                </div>
                <div class="content_body_information_center">
                  <div>编号：{{ item.informationNum }}号</div>
                  <div>支持：<span>{{ item.sustain }}</span>次</div>
                </div>
                <div class="content_body_information_right">
                  <div class="content_body_information_rightbox">
                    <img class="content_body_information_viod" v-if="(index + 1) < 4" :src="require(`../assets/images/${(index + 1) === 1 ? 9 : (index + 1) === 2 ? 13 : 17}.png`)" alt="">
                    <img class="content_body_information_solid" :src="require(`../assets/images/${(index + 1) === 1 ? 8 : 12}.png`)" alt="">
                  </div>
                </div>
              </div>
            </div>
            <img v-if="(index + 1 < 5)" style="width: 60px;height: 70px;" class="content_body_information_top"
            :src="require(`../assets/images/${(index + 1) === 1 ? 7 : (index + 1) === 2 ? 11 : (index + 1) === 3 ? 15 : 19}.png`)" alt="">
            <div v-else class="content_body_information_top1">
              <div class="content_body_information_square">{{ index + 1 }}</div>
              <div class="content_body_information_delta"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer">
      <div class="footer_item1">
        <img src="../assets/images/24.png" style="width: 35px; height:50px" alt="">
      </div>
      <div class="footer_item1">
        <img src="../assets/images/25.png" style="width: 35px; height:50px" alt="">
      </div>
      <div class="footer_item2 footer_color1">
        <button>活动规则</button>
      </div>
      <div class="footer_item2 footer_color2">
        <button>我要报名</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue';

// 数据
const informationData = reactive([
  {informationName: '河南扬程电力消防有限公司', informationNum: 8,sustain: 455,imgUrl: ''},
  {informationName: '河南扬程电力消防有限公司', informationNum: 8,sustain: 455,imgUrl: ''},
  {informationName: '河南扬程电力消防有限公司', informationNum: 8,sustain: 455,imgUrl: ''},
  {informationName: '河南扬程电力消防有限公司', informationNum: 8,sustain: 455,imgUrl: ''},
  {informationName: '河南扬程电力消防有限公司', informationNum: 8,sustain: 455,imgUrl: ''},
  {informationName: '河南扬程电力消防有限公司', informationNum: 8,sustain: 455,imgUrl: ''},
  {informationName: '河南扬程电力消防有限公司', informationNum: 8,sustain: 455,imgUrl: ''},
  {informationName: '河南扬程电力消防有限公司', informationNum: 8,sustain: 455,imgUrl: ''},
])

</script>

<style lang="scss" scoped>
.body{
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}
.content{
  flex: 1;
  overflow-y: scroll;
}
.content_top{
  height: 200px;
  background-image: url('../assets/images/2.png');
  background-size: 100% 100%;
  background-repeat: no-repeat;
  display: flex;
  justify-content: center;
  align-items: center;
}
.content_top_center{
  width: 80%;
  height: 80%;
  background-image: url('../assets/images/1.png');
  background-size: 100% 100%;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #FFFFFF;
}
.content_body_persennum{
  display: flex;
  justify-content: space-between;
}
.content_body_persennum_item{
  width: 41%;
  padding: 10px;
  display: flex;
  align-items: flex-end;
  font-size: 10px;
  img{
    margin-right: 10px;
  }
  span{
    color: rgb(49, 60, 161);
  }
}
.content_body_search{
  display: flex;
  justify-content: space-between;
  background-color: #f3f3f3;
  padding: 15px;
}
.content_body_search_button{
  width: 95px;
  background-image: url('../assets/images/5.png');
  background-size: 100%;
  position: relative;
}
.content_body_search_status{
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
input{
  width: 65%;
  padding: 10px;
  border: 1px solid #f3f3f3;
}
button{
  width: 100%;
  height: 100%;
  border: none;
  color: #FFFFFF;
  font-size: 14px;
}
.content_body_information_item{
  height: 175px;
  position: relative;
}
.content_body_information_top{
  position: absolute;
  z-index: 5;
  top: -5px;
  left: 20px;
}
// 绘制倒三角型
.content_body_information_top1{
  position: absolute;
  z-index: 5;
  top: -5px;
  left: 20px;
  .content_body_information_square{
    width: 60px;
    height: 30px;
    line-height: 30px;
    background-color: green;
    text-align: center;
    color: #FFFFFF;
  }
  .content_body_information_delta{
    width: 0px;
    height: 0px;
    border-top: 15px solid green;
    border-left: 30px solid transparent;
    border-right: 30px solid transparent;
    border-bottom: 30px solid transparent;
  }
}
.content_body_information_background{
  position: absolute;
}
.content_body_information_body{
  width: calc(100% - 40px);
  position: absolute;
  z-index: 5;
  padding: 20px;
}
.content_body_information_title{
  display: flex;
  align-items: center;
  height: 30px;
  .content_body_information_name{
    margin-left: 10px;
    font-size: 12px;
  }
}
.content_body_information_content{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  margin-top: 10px;
}
.content_body_information_center{
  grid-column: span 2 / auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  span{
    color: red;
    font-size: 17px;
  }
}
.content_body_information_left{
  height: 80px;
  padding: 10px;
}
.content_body_information_right{
  height: 100%;
  .content_body_information_rightbox{
    width: 100%;
    height: 100%;
    position: relative;
    .content_body_information_viod{
      height: 90%;
      position: absolute;
      z-index: -1;
      top: 0px;
    }
    .content_body_information_solid{
      height: 40px;
      padding-top: 25px;
    }
  }
}
.footer{
  height: 50px;
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  padding: 10px;
  border: 1px solid #f3f3f3;
}
.footer_item2{
  grid-column: span 2 / auto;
}
.footer_color1 > button{
  background-color: orange;
}
.footer_color2 > button{
  background-color: blue;
}
</style>
