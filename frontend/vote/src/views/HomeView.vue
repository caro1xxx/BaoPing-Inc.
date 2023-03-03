<template>
  <div class="body">
    <div class="content">
      <div class="content_top"></div>
      <div class="content_body">
        <div class="content_body_persennum">
          <div class="content_body_persennum_item">入选企业：<span>458</span></div>
          <div class="content_body_persennum_item">访问数量：<span>4999</span></div>
        </div>
        <div class="content_body_time">
          <svg t="1677828286354" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2607" width="200" height="200">
          <path d="M511.333 127.333c51.868 0 102.15 10.144 149.451 30.15 45.719 19.337 86.792 47.034 122.078 82.321 35.287 35.286 62.983 76.359 82.321 122.078 20.006 47.3 30.15 97.583 30.15 149.451s-10.144 102.15-30.15 149.451c-19.337 45.719-47.034 86.792-82.321 122.078-35.286 35.287-76.359 62.983-122.078 82.321-47.3 20.006-97.583 30.15-149.451 30.15s-102.15-10.144-149.451-30.15c-45.719-19.337-86.792-47.034-122.078-82.321-35.287-35.286-62.983-76.359-82.321-122.078-20.006-47.3-30.15-97.583-30.15-149.451s10.144-102.15 30.15-149.451c19.337-45.719 47.034-86.792 82.321-122.078 35.286-35.287 76.359-62.983 122.078-82.321 47.301-20.006 97.583-30.15 149.451-30.15m0-64c-247.424 0-448 200.576-448 448s200.576 448 448 448 448-200.576 448-448-200.576-448-448-448z" fill="#dbdbdb" p-id="2608">
          </path><path d="M702.856 543.333H511.333c-17.673 0-32-14.326-32-32v-286.73c0-17.673 14.327-32 32-32s32 14.327 32 32v254.73h159.522c17.673 0 32 14.327 32 32s-14.326 32-31.999 32z" fill="#dbdbdb" p-id="2609"></path></svg>
          <div class="content_body_time_label">倒计时结束</div>
          <div class="content_body_time_num">
            <span>00</span>天<span>00</span>时<span>00</span>分<span>00</span>秒
          </div>
        </div>
        <div class="content_body_search">
          <input type="text" placeholder="请输入选手名称或编号查询" />
          <button>搜素</button>
        </div>
        <div class="content_body_information">
          <div class="content_body_information_item">
            <div class="content_body_information_title">四川世代建筑工程有限公司</div>
            <div class="content_body_information_body">
              <div class="content_body_information_left">
                <img src="" alt="">
              </div>
              <div class="content_body_information_center">
                <div>编号：8号</div>
                <div>票数：<span>455</span>票</div>
              </div>
              <div class="content_body_information_right">支持他</div>
            </div>
          </div>
          <div class="content_body_information_item">
            <div class="content_body_information_title">四川德友建工集团有限公司</div>
            <div class="content_body_information_body">
              <div class="content_body_information_left">
                <img src="" alt="">
              </div>
              <div class="content_body_information_center">
                <div>编号：8号</div>
                <div>票数：<span>455</span>票</div>
              </div>
              <div class="content_body_information_right">支持他</div>
            </div>
          </div>
          <div class="content_body_information_item">
            <div class="content_body_information_title">广安万达建筑工程有限公司</div>
            <div class="content_body_information_body">
              <div class="content_body_information_left">
                <img src="" alt="">
              </div>
              <div class="content_body_information_center">
                <div>编号：8号</div>
                <div>票数：<span>455</span>票</div>
              </div>
              <div class="content_body_information_right">支持他</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer"></div>
  </div>
</template>

<script setup></script>

<style lang="scss" scoped>
.body{
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  background-color: #f3f3f3;
}
.content{
  flex: 1;
  overflow-y: scroll;
}
.content_top{
  height: 200px;
  background-color: red;
}
.content_body{
  padding: 20px;
}
.content_body_persennum{
  display: flex;
  justify-content: space-between;
}
.content_body_persennum_item{
  text-align: center;
  border-radius: 10px;
  width: 41%;
  padding: 15px;
  font-size: 20px;
  background-color: #ffffff;
  span{
    color: rgb(61, 129, 61);
  }
}
.content_body_time{
  width: 94%;
  padding: 10px 10px;
  margin-top: 10px;
  background-image: linear-gradient(to right, red , orange);
  display: flex;
  align-items: center;
}
.content_body_time_num{
  margin-left: 10px;
  flex: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #ffffff;
  font-size: 12px;
  span{
    background-color: yellow;
    padding: 5px 10px;
    border-radius: 10px;
    color: #000000;
  }
}
svg{
  width: 20px;
  height: 20px;
  margin-right: 10px;
}
.content_body_time_label{
  font-size: 12px;
  border: 2px solid #f3f3f3;
  border-radius: 5px;
  color: #f3f3f3;
  padding: 2px 3px;
}
.content_body_search{
  display: flex;
  margin-top: 10px;
  justify-content: space-between;
}
input{
  width: 70%;
}
button{
  width: 15%;
  background-color: orange;
  color: #000000;
}
input,button{
  padding: 10px;
  border-radius: 10px;
  outline: none;
  border: 1px solid #f3f3f3;
}
.content_body_information{
  display: flex;
  flex-direction: column;
  .content_body_information_item{
    padding: 10px;
    text-align: center;
  }
}
.content_body_information_body{
  display: flex;
  align-items: center;
  margin-top: 10px;
}
.content_body_information_center{
  flex: 1;
  text-align: left;
}
.content_body_information_left{
  width: 100px;
  height: 80px;
  padding: 10px;
  img{
    width: 100%;
    height: 100%;
    background-size: 100%;
    background-repeat: no-repeat;
  }
}
.content_body_information_right{
  height: 25%;
  font-size: 20px;
  color: #ffffff;
  font-weight: 50px;
  border-radius: 10px;
  padding: 10px 15px;
  background-color: orange;
}
.footer{
  height: 50px;
  background-color: aquamarine;
}
</style>
