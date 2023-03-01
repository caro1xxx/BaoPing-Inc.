<template>
  <div class="body">
    <div class="body_body">
      <div class="body_body_bar">
        <div>添加活动</div>
      </div>
      <div class="body_body_item" v-for="item in dataItem" :key="item.key">
        <label>{{ item.name }}</label>
        <el-input
          v-if="item.type === 'text'"
          v-model="item.value"
          clearable
          placeholder="请输入"
          :disabled="item.state"
        />
        <el-date-picker
          v-else-if="item.type === 'date'"
          v-model="item.value"
          style="width: 95%"
          type="datetimerange"
          range-separator="至"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
        />
        <div style="display: flex" v-else-if="item.type === 'upload'">
          <input
            @change="uploadChange"
            type="file"
            class="upload"
            id="upload"
            ref="uploadRef"
          />
          <div @click="dispatchUpload" class="uploadReplace">
            <div>+</div>
          </div>
          <img class="detailImg" v-if="imageUrl" :src="imageUrl" alt="" />
        </div>
      </div>
      <el-button style="color: #2460e5; width: 100%" @click="save"
        >保存</el-button
      >
      <img
        @click="
          () => {
            $store.dispatch('voteManagerActions', {
              type: 'post',
              target: '',
            });
          }
        "
        class="close"
        src="../assets/img/31.png"
        alt=""
      />
    </div>
  </div>
</template>

<script setup>
import jsCookie from "js-cookie";
import { reactive, ref } from "vue";
import { useStore } from "vuex";
import { Validator } from "../utils/validator";
import { HOST } from "@/ENV";
const $store = new useStore();

const dataItem = reactive([
  { name: "活动名称", value: "", type: "text", key: 1, state: false },
  {
    name: "创建者",
    value: jsCookie.get("username"),
    type: "text",
    key: 2,
    state: true,
  },
  { name: "活动起始日期", value: "", type: "date", key: 3, state: false },
  { name: "活动缩略图", value: "", type: "upload", key: 4, state: false },
]);

// 缩略图url
const imageUrl = ref("");
const uploadRef = ref("");

// 点击按钮分发到file click事件
const dispatchUpload = () => {
  let box = document.getElementById("upload");
  box.click();
};

// 上传改变
const uploadChange = () => {
  const file = uploadRef.value[0].files[0];
  if (file.type !== "image/png") {
    $store.dispatch("GlobalMessageActions", "请上传图片类型的文件");
    return;
  }
  const reads = new FileReader();
  reads.readAsDataURL(file);
  reads.onload = function (e) {
    imageUrl.value = e.target.result;
    dataItem[3].value = "1";
  };
};

//提交校验
const check = () => {
  let validator = new Validator();
  for (let i of dataItem) {
    validator.add(i.value, "isNonEmpty", `请输入${i.name}`);
  }
  let result = validator.start();
  if (result) $store.dispatch("GlobalMessageActions", result);
  else return true;
};

// 提交
const save = () => {
  if (!check) return;
  let d = new FormData();
  d.append("vote_name", dataItem[0].value);
  d.append("create_user_username", dataItem[1].value);
  d.append("create_time", dataItem[2].value[0].getTime() / 1000);
  d.append("expire_time", dataItem[2].value[1].getTime() / 1000);
  d.append("img", uploadRef.value[0].files[0]);
  d.append("token", jsCookie.get("token"));
  fetch(`${HOST}/voteactivity/`, {
    method: "post",
    body: d,
    // headers: { "Content-Type": "application/json" },
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
    });
};
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
  z-index: 5;
}
.body_body {
  height: calc(80vh - 40px);
  width: calc(30vw);
  background-color: white;
  border-radius: 3px;
  padding: 20px;
  position: relative;
}
.body_body_bar {
  display: flex;
  div {
    font-size: 15px;
    width: 20%;
    margin-bottom: 10px;
    cursor: pointer;
  }
  border-bottom: 2px solid #d4d4d474;
}
.close {
  position: absolute;
  right: -50px;
  top: 0;
  width: 30px;
  height: 30px;
  z-index: 5;
}
.body_body_item {
  margin: 10px 0px;
  label {
    display: block;
    font-size: 13px;
    margin-bottom: 5px;
  }
  input {
    outline: none;
    border: 1px solid #e6e6e6;
    border-radius: 3px;
    width: 99%;
    height: 25px;
  }
}
.upload {
  display: none;
}
.uploadReplace {
  height: 100px;
  width: 100px;
  border: 2px dashed #cecece;
  border-radius: 3px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  div {
    position: absolute;
    z-index: 2;
    font-size: 30px;
    color: #cecece;
  }
}
.detailImg {
  height: 104px;
  width: 104px;
}
</style>
