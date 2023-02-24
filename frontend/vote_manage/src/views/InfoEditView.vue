<template>
    <div class="InfoEdit_main">
      <div class="InfoEdit_main_body">
        <Search />
        <div class="title_style">信息修改</div>
        <div class="InfoEdit_table">
          <div class="InfoEdit_table_head">
            <div v-for="item in InfoEditheated" :key="item.name">{{ item.name }}</div>
          </div>
          <div class="InfoEdit_table_body_wrap">
            <div class="InfoEdit_table_body" v-for="item in InfoEditdata" :key="item.id">
              <div>{{ item.id }}</div>
              <div><img :src="item.imgUrl" alt=""></div>
              <div>{{ item.username }}</div>
              <div>{{ item.activeid }}</div>
              <div>{{ item.userid }}</div>
              <div>{{ item.addtime }}</div>
              <div>{{ item.feedbackcontent }}</div>
              <div>{{ item.ishandle }}</div>
              <div class="InfoEdit_table_operatebox">
                <span>删除</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import Search from "@/components/Search.vue";
  import { reactive } from "vue";
  
  // 反馈信息表格头部
  const InfoEditheated = reactive([
    { name: 'id' },
    { name: '图片' },
    { name: '名称' },
    { name: '活动id' },
    { name: '选手id' },
    { name: '添加时间' },
    { name: '反馈内容' },
    { name: '是否处理' },
    { name: '操作' }
  ])
  
  const InfoEditdata = reactive([
    { id: '124', imgUrl: '', username: '小明', activeid: '43', userid: 'satejgssndsa', addtime: '2023-01-13 10:00:00',  feedbackcontent:'熙增的', ishandle: true},
    { id: '124', imgUrl: '', username: '小明', activeid: '43', userid: 'satejgssndsa', addtime: '2023-01-13 10:00:00',  feedbackcontent:'熙增的', ishandle: true},
    { id: '124', imgUrl: '', username: '小明', activeid: '43', userid: 'satejgssndsa', addtime: '2023-01-13 10:00:00',  feedbackcontent:'熙增的', ishandle: true},
    { id: '124', imgUrl: '', username: '小明', activeid: '43', userid: 'satejgssndsa', addtime: '2023-01-13 10:00:00',  feedbackcontent:'熙增的', ishandle: true},
    { id: '124', imgUrl: '', username: '小明', activeid: '43', userid: 'satejgssndsa', addtime: '2023-01-13 10:00:00',  feedbackcontent:'熙增的', ishandle: true},
    { id: '124', imgUrl: '', username: '小明', activeid: '43', userid: 'satejgssndsa', addtime: '2023-01-13 10:00:00',  feedbackcontent:'熙增的', ishandle: true},
    { id: '124', imgUrl: '', username: '小明', activeid: '43', userid: 'satejgssndsa', addtime: '2023-01-13 10:00:00',  feedbackcontent:'熙增的', ishandle: true},
  ])
  
  </script>
  
  <style lang="scss" scoped>
  .InfoEdit_main {
    width: calc(100vw - 200px);
    height: calc(100vh);
    font-size: 20px;
    font-weight: 50px;
  }
  .InfoEdit_main_body {
    margin: 20px 20px;
  }
  .InfoEdit_table {
    border: 1px solid #b5c3d178;
    border-radius: 10px;
    height: calc(100vh - 180px);
    margin-top: 20px;
  }
  .InfoEdit_table_head {
    user-select: none;
    border-radius: 10px 10px 0px 0px;
    height: 40px;
    border-bottom: 1px solid #b5c3d178;
    box-shadow: 0 4px 4px 0 #bababa21;
    display: flex;
    div {
      flex: 1;
      text-align: center;
      line-height: 40px;
      font-size: 15px;
      font-weight: lighter;
    }
    cursor: pointer;
      user-select: none;
  }
  .InfoEdit_table_body {
    display: flex;
    div {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      font-weight: lighter;
      color: #585858;
      margin: 10px 0px;
    }
    img{
      width: 40px;
      height: 40px;
      background-size: 100%;
      background-repeat: no-repeat;
    }
    .InfoEdit_table_operatebox{
      display: flex;
      justify-content: center;
      color: #188CFF;
      span{
        cursor: pointer;
      user-select: none;
        margin: 0px 10px;
      }
    }
  }
  .InfoEdit_table_body_wrap {
    height: calc(100vh - 230px);
    overflow-y: scroll;
  }
  .InfoEdit_table_body_wrap::-webkit-scrollbar {
    display: none;
  }
  </style>
  