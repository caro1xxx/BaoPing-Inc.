<template>
  <div class="feedback" @click="props.data.close">
    <div class="body" @click="(e) => e.stopPropagation()">
      <div class="content">
        <label>活动ID</label>
        <input type="text" :value="props.data.vote_id" disabled />
        <label>反馈内容</label>
        <textarea type="text" v-model="inputValue" rows="6"></textarea>
        <div class="save_btn" @click="(e) => check(e)">提交</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { fether } from "@/utils/fether";
import { ref } from "vue";

const props = defineProps({
  data: Object,
});

const inputValue = ref("");

const check = (e) => {
  e.stopPropagation();
  if (inputValue.value === "") return;
  save();
};

const save = async () => {
  let result = await fether("/feedback/", "post", {
    data: {
      vote_id: props.data.vote_id,
      vote_user_open_id: props.data.vote_user_openid,
      content: inputValue.value,
    },
  });
  if (!result) return;
  props.data.close();
};
</script>

<style lang="scss" scoped>
.feedback {
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
.body {
  background-color: #f3f3f3;
  width: 80%;
  border-radius: 5px;
}
.content {
  display: block;
  margin: 10px;
  padding: 10px;
  background-color: #ffffff;
  input {
    display: block;
    width: 96%;
    padding: 2%;
    margin: 5% 0px;
    border-radius: 5px;
    border: 0.5px solid #e1e1e1;
    outline: none;
  }
  textarea {
    display: block;
    width: 96%;
    padding: 2%;
    margin: 5% 0px;
    border-radius: 5px;
    border: 0.5px solid #e1e1e1;
    outline: none;
  }
}
.save_btn {
  background-color: #0d6efd;
  color: white;
  width: 100%;
  line-height: 30px;
  text-align: center;
  border-radius: 3px;
}
</style>
