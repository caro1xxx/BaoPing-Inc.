<template>
  <div class="body">
    <div class="content">
      <div class="content_top"></div>
      <div class="content_body">
        <div class="content_body_persennum">
          <div class="content_body_persennum_item">访问数：<span>2.5w</span></div>
          <div class="content_body_persennum_item">报名数：<span>45</span></div>
        </div>
        <div class="content_body_search">
          <input type="text" placeholder="搜索名称或编号" />
          <div class="content_body_search_button">
            <div class="content_body_search_text">跟踪报道</div>
            <div class="content_body_search_status">已更新</div>
          </div>
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
    <div class="footer">
      <div>

      </div>
      <div></div>
      <div></div>
      <div></div>
    </div>
  </div>
</template>

<script setup></script>

<style lang="scss" scoped>
.body{
  width: 100%;
  height: 100%;
  display: flex;
}
.content{
  flex: 1;
  overflow-y: scroll;
}
.content_top{
  height: 200px;
  background-color: red;
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
  span{
    color: rgb(49, 60, 161);
    font-weight: 50px;
  }
}
.content_body_search{
  display: flex;
  margin-top: 10px;
  justify-content: space-between;
  background-color: #f3f3f3;
  padding: 15px;
}
.content_body_search_text{
  padding: 5px;
  border: 1px solid rgb(175, 109, 34);
}
.content_body_search_button{
  padding: 5px;
  position: relative;
  background-color: rgb(223, 189, 117);
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
