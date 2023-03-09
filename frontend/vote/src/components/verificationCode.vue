<template>
    <div class="body" @click="props.method()">
        <div class="body_content">
            <div class="body_content_top">
                <div class="body_content_top_time">{{ `${nowTime.year}.${nowTime.month}.${nowTime.day} ${nowTime.houers}:${nowTime.minute}:${nowTime.sercet}` }}</div>
                <div class="body_content_top_box">
                    <div class="body_content_top_item">
                        <img :src="`${HOST2}/media/${props.data.avator}`" alt="">
                    </div>
                    <div class="body_content_top_item1">
                        <div class="body_content_top_number">{{ props.data.pk }}号</div>
                        <div class="body_content_top_name">{{ props.data.name }}</div>
                    </div>
                </div>
            </div>
            <div class="body_botton">
                <span class="login">验证：</span>
                <input
                    style="width: 100px"
                    type="text"
                    placeholder="请输入验证码"
                    class="input-val"
                    v-model="yanzhen"
                    @change="enterCode"
                    @click="(e) => {sureInput(e)}"
                />
                <canvas id="canvas" style="width: 133px;height: 33px;" @click="(e) => {handleCanvas(e)}"> </canvas>
            </div>
            <div style="margin-top: 15px;text-align: center;">点击其他位置关闭</div>
            <div class="sureBotton" @click="(e)=>{close(e)}">确认支持他</div>
        </div>
    </div>
</template>

<script setup>
import { fether } from "@/utils/fether";
import { reactive, onMounted, defineProps } from 'vue';
import { HOST, HOST2 } from "../ENV";
import Mobile from "mobile-detect";
import { useRoute } from "vue-router";
import { isNetWork } from "../utils/network";
import base64 from "base-64";
const $route = useRoute();
let yanzhen = ''
//  保存正确验证码
  let true_code = ''
// /只用于传参
const yanzhen_arr = reactive([])

//判断验证码是否通过
let isCode = false

const props = defineProps({
  data: {
    verificationCodeData: Object,
  },
  method:{close:()=>{}}
});
const nowTime = reactive({
  // 年
  year: '',
  // 月
  month: '',
  // 天
  day: "",
  // 时
  houers: "",
  // 分
  minute: "",
  //秒
  second: "",
});



onMounted(() => {
    draw(yanzhen_arr)
})
// canvas绘图
const draw = async (show_num) => {
    let canvas_width =  document.querySelector("#canvas").clientWidth;
    let canvas_height = document.querySelector("#canvas").clientHeight;
    let canvas = document.getElementById("canvas"); //获取到canvas
    let context = canvas.getContext("2d"); //获取到canvas画图
    canvas.width = canvas_width;
    canvas.height = canvas_height;
    let sCode =
      "a,b,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,E,F,G,H,J,K,L,M,N,P,Q,R,S,T,W,X,Y,Z,1,2,3,4,5,6,7,8,9,0";
    let aCode = sCode.split(",");
    let aLength = aCode.length; //获取到数组的长度
    //4个验证码数
    for (let i = 0; i <= 3; i++) {
      let j = Math.floor(Math.random() * aLength); //获取到随机的索引值
      let deg = (Math.random() * 30 * Math.PI) / 180; //产生0~30之间的随机弧度
      let txt = aCode[j]; //得到随机的一个内容
      show_num[i] = txt;// 依次把取得的内容放到数组里面
      let x = 10 + i * 20; //文字在canvas上的x坐标
      let y = 20 + Math.random() * 8; //文字在canvas上的y坐标
      context.font = "bold 23px 微软雅黑";
      context.translate(x, y);
      context.rotate(deg);
      context.fillStyle = randomColor();
      context.fillText(txt, 0, 0);
      context.rotate(-deg);
      context.translate(-x, -y);
    }
    //验证码上显示6条线条
    for (let i = 0; i <= 5; i++) {
      context.strokeStyle = randomColor();
      context.beginPath();
      context.moveTo(
        Math.random() * canvas_width,
        Math.random() * canvas_height
      );
      context.lineTo(
        Math.random() * canvas_width,
        Math.random() * canvas_height
      );
      context.stroke();
    }
    //验证码上显示31个小点
    for (let i = 0; i <= 30; i++) {
      context.strokeStyle = randomColor();
      context.beginPath();
      let x = Math.random() * canvas_width;
      let y = Math.random() * canvas_height;
      context.moveTo(x, y);
      context.lineTo(x + 1, y + 1);
      context.stroke();
    }
    //最后把取得的验证码数组存起来，方式不唯一
    let num = show_num.join("");
    // console.log(num);
    true_code = num
}
//得到随机的颜色值
const randomColor = async () => {
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);
    return "rgb(" + r + "," + g + "," + b + ")";
}
//canvas点击刷新
const handleCanvas = async (e) => {
    e.stopPropagation()
    draw(yanzhen_arr);
}

// 输入框获取输入值比较验证码
const enterCode = async (e) => {
    if (true_code === e.target.value) {
        isCode = true
    }
}
const sureInput = async (e) => {
    e.stopPropagation()
}

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

// 实时获取现在时间
const getNowTime = async () => {
    setInterval(() => {
        let data = new Date()
        let year = data.getFullYear()
        let month = data.getMonth() + 1
        let day = data.getDate()
        let houers = data.getHours()
        let minute = data.getMinutes()
        let sercet = data.getSeconds()
        nowTime.year = year
        nowTime.month = zrron(month)
        nowTime.day = zrron(day)
        nowTime.houers = zrron(houers)
        nowTime.minute = zrron(minute)
        nowTime.sercet = zrron(sercet)
    }, 1000)
}
getNowTime()
// 补零
const zrron = (value) => {
    if (value < 10) {
        return `0${value}`
    } else {
        return value
    }
}

const close = async (e)=>{
    e.stopPropagation()
    if (isCode === true) {
        // 发送点赞请求
        let keys = await getKey();
        let sercet = await encryption(keys);
        const md = new Mobile(navigator.userAgent);
        let result = await fether("/support/", "post", {
            data: {
            open_id: "wxtest6",
            vote_target_id: props.data.pk,
            vote_id: $route.query.vote_id,
            phone_model: md.mobile(),
            system: md.os(),
            network: isNetWork(),
            key: sercet,
            },
        });
    } else {
        alert('验证码错误，请重新输入')
    }
}
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
  z-index: 6;
}
.body_content {
  width: 80%;
  height: 40%;
  background-image: url('../assets/img/4.png');
  background-size: 100% 100%;
  padding: 10px;
  position: relative;
}
.body_content_top{
    margin-top: 15%;
    text-align: center;
}
.body_content_top_box{
    height: 80px;
    display: flex;
    margin-top: 20px;
}
.body_content_top_item{
    width: 45%;
    height: 80px;
}
.body_content_top_item1{
    margin-left: 10px;
}
.body_content_top_number{
    padding: 2px 15px;
    border-radius: 10px;
    background-color: green;
    color: #ffffff;
    font-size: 15px;
    margin-top: 5px;
}
.body_content_top_name{
    margin-top: 10px;
    text-align: left;
}
.body_botton{
    margin-top: 10px;
    display: flex;
    align-items: center;
    justify-content: space-around;
}
#canvas {
  margin-right: 1%;
  display: block;
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
}

.input-val {
  width: 50%;
  background: #ffffff;
  border-radius: 5px;
  border: none;
  padding: 10px;
  border: 1px solid rgba(0, 0, 0, 0.2);
}
.sureBotton{
    position: absolute;
    bottom: 35px;
    left: 35%;
    font-size: 20px;
    font-weight: bold;
}
</style>