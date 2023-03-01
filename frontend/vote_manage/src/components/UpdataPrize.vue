<template>
    <div class="body">
        <div class="body_content">
            <div class="body_content_head">编辑</div>
            <div class="body_content_body">
                <div class="body_content_item">
                    <label>openid(用户名)</label>
                    <el-input v-model="prizeData.wx_username" placeholder="请输入" />
                </div>
                <div class="body_content_item">
                    <label>姓名</label>
                    <el-input v-model="prizeData.name" placeholder="请输入" />
                </div>
                <div class="body_content_item">
                    <label>手机号</label>
                    <el-input v-model="prizeData.phone_number" placeholder="请输入" />
                </div>
                <div class="body_content_item">
                    <label>申请时间</label>
                    <el-date-picker
                        v-model="prizeData.create_time"
                        type="datetime"
                        placeholder="请选择时间"
                        format="YYYY/MM/DD HH:mm:ss"
                    />
                </div>
                <div class="body_content_item">
                    <label>状态</label>
                    <el-select v-model="prizeData.status" class="m-2" placeholder="请选择状态">
                        <el-option
                            v-for="item in statusData"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value"
                        />
                    </el-select>
                </div>
                <div class="body_content_button">
                    <button class="body_content_button_item1" @click="closePopup">取消</button>
                    <button class="body_content_button_item2" @click="sureRealmData">确认</button>
                </div>
            </div>
            <img @click="closePopup" class="body_content_close" src="../assets/img/31.png" alt="">
        </div>
    </div>
</template>

<script setup>
import { reactive } from "vue"
import {  useStore } from "vuex"
import { fether } from "@/utils/fether"
import Cookies from 'js-cookie'
const $store = new useStore()
const closePopup = ()=>{
  $store.commit('changePrizeStatus')
}

// 需要编辑的数据
const prizeData = reactive({
    wx_username: $store.state.prizeData.wx_username,
    name: $store.state.prizeData.name,
    status: $store.state.prizeData.status,
    phone_number: $store.state.prizeData.phone_number,
    create_time: $store.state.prizeData.create_time,
    index: $store.state.prizeData.index,
    pk: $store.state.prizeData.pk
})

// 状态数据
const statusData = reactive([
    {
        value: 0,
        label: '0'
    },
    {
        value: 1,
        label: '1'
    }
])

// 点击确认按钮
const sureRealmData = async () => {
    // 开启加载loading
    await $store.dispatch("NoticifyActions", true);
    // 判断值是否输入
    if (!prizeData.wx_username) {
        await $store.dispatch("GlobalMessageActions", '用户名未输入');
    } else if (!prizeData.phone_number) {
        await $store.dispatch("GlobalMessageActions", '手机号未输入');
    } else {
        if (typeof prizeData.create_time === 'object') {
            prizeData.create_time = new Date(prizeData.create_time).getTime() / 1000
        }
        let result = await fether(`/applyprize/`, `put`, {
            token: Cookies.get("token"),
            wx_username: prizeData.wx_username,
            name: prizeData.name,
            phone_number: prizeData.phone_number,
            pk: prizeData.pk,
            status: prizeData.status,
            create_time: prizeData.create_time
        })
        if (result.code === 200) {
            $store.commit('changePrizeStatus', prizeData)
        }
        await $store.dispatch("GlobalMessageActions", result.msg);
        // 关闭加载loading
        $store.commit("noticifyLoading", false);
    }
}
</script>

<style lang="scss" scoped>
.body{
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
.body_content{
  width: calc(25vw - 40px);
  height: calc(50vh - 40px);
  background-color: white;
  border-radius: 3px;
  padding: 20px;
  position: relative;
}
.body_content_head{
    font-size: 15px;
    cursor: pointer;
    border-bottom: 2px solid #d4d4d474;
    margin-bottom: 10px;
}
.body_content_close{
    position: absolute;
    right: -60px;
    top: 0px;
    width: 30px;
    height: 30px;
    cursor: pointer;
}
.body_content_item{
    margin-bottom: 10px;
    label{
        display: block;
        font-size: 13px;
        margin-bottom: 5px;
    }
    :deep(.el-date-editor),
    :deep(.el-select) {
        width: 100%;
    }
}
.body_content_button{
    width: 100%;
    display: flex;
    justify-content: flex-end;
    position: absolute;
    bottom: 20px;
    left: 0px;
    button{
        margin-right: 20px;
        width: 20%;
        height: 100%;
        border: 1px solid #dcdfe6;
        outline: none;
        border-radius: 5px;
        padding: 5px 0px;
    }
    .body_content_button_item1{
      border: 1px solid #dcdfe6;
    }
    .body_content_button_item2{
        background-color: #409eff;
        color: #ffffff;
    }
}
</style>