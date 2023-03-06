<template>
  <div class="body">
    <div class="top">1</div>
    <div class="body">
      <div class="body_content">
        <div class="body_content_title"></div>
        <div class="body_content_search">
          <input placeholder="搜索名称或编号" type="text" />
          <div class="body_content_search_btn">搜索</div>
          <div class="body_content_track">追踪报道</div>
        </div>
      </div>
      <div class="body_item">
        <div>1</div>
      </div>
    </div>
  </div>
</template>

<script setup></script>

<style lang="scss" scoped>
.top {
  background-color: bisque;
  height: 200px;
}
.body {
  background-color: red;
}
.body_content {
  margin: 10px;
}
.body_content_title {
  height: 50px;
  background-color: yellow;
  border-radius: 20px;
}
.body_content_search {
  display: flex;
  margin: 20px 0px;
  input {
    height: 30px;
    padding: 10px;
    border: none;
    outline: none;
    border-radius: 5px;
    width: 50%;
  }
}
.body_content_search_btn {
  background-color: white;
  height: 50px;
  line-height: 50px;
  font-size: 17px;
  width: 15%;
  border-radius: 5px;
  margin: 0px 1%;
  text-align: center;
}
.body_content_track {
  width: 30%;
  margin-left: 3%;
  background-color: yellow;
}
.body_item {
  background-color: yellow;
  padding: 20px 0px;
}
</style>
