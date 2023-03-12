<template>
  <div class="body">
    <div class="body_body">
      <div class="body_body_bar">
        <div>添加礼物</div>
      </div>
      <div v-for="item in dataItem" style="margin: 10px 0px">
        <label style="font-size: 13px">{{ item.name }}</label>
        <el-input
          v-if="item.type === 'text'"
          v-model="item.value"
          style="margin-top: 10px"
          clearable
          placeholder="请输入"
          :disabled="item.state"
        />
        <el-input-number
          style="display: block; margin-top: 10px"
          v-else-if="item.type === 'number'"
          v-model="item.value"
          :min="1"
        />

        <el-switch v-model="item.value" v-else-if="item.type === 'switch'" />
        <div v-else style="display: flex">
          <div @click="dipatchEvent" class="uploadReplace">
            <div>+</div>
            <input
              @change="uploadFile"
              type="file"
              id="upload"
              style="display: none"
            />
          </div>
          <img
            v-show="imgRef"
            class="detailImg"
            :src="HOST + '/media/' + imgRef"
            alt=""
          />
        </div>
      </div>

      <el-button style="color: #2460e5; width: 100%" @click="save"
        >保存</el-button
      >
      <img
        @click="
          () => {
            $store.commit('changeGiftAdd');
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
import { HOST } from "@/ENV";
import { fether } from "@/utils/fether";
const $store = new useStore();

const dataItem = reactive([
  { name: "礼物名称", value: "", type: "text", key: 0, state: false },
  { name: "礼物价值", value: "", type: "number", key: 1, state: false },
  { name: "价格", value: "", type: "number", key: 2, state: false },
  { name: "开关", value: true, type: "switch", key: 3, state: false },
  { name: "礼物图片", value: true, type: "file", key: 3, state: false },
]);
const imgRef = ref("");

// 提交
const save = async () => {
  let data = {
    name: dataItem[0].value,
    value: dataItem[1].value,
    price: dataItem[2].value,
    status: dataItem[3].value ? 1 : 0,
    img: imgRef.value,
  };
  let result = await fether("/gift/", "post", {
    token: jsCookie.get("token"),
    data: data,
  });
  if (result.code === 200) {
    await $store.dispatch("GlobalMessageActions", result.msg);
    $store.commit("changeGiftAdd", data);
  } else {
    // 请求发送错误
    await $store.dispatch("refreshErroActions");
    await $store.dispatch("GlobalMessageActions", "操作失败,请刷新");
  }
};

// 分发事件
const dipatchEvent = () => {
  let box = document.getElementById("upload");
  box.click();
};

// 上传文件
const uploadFile = async () => {
  let form = new FormData();
  form.append("file", document.getElementById("upload").files[0]);
  form.append("cotegory", "img");
  form.append("token", jsCookie.get("token"));
  fetch(`${HOST}/uploadfile/`, { method: "post", body: form })
    .then((res) => res.json())
    .then((data) => {
      if (data.code === 200) {
        imgRef.value = data.data.filename;
      }
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
