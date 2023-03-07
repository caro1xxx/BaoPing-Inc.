<template>
    <div class="body">
        <div class="body_title">
            <button @click="returnPage">返回</button>
            <span>选手详情</span>
        </div>
        <div class="grid-container">
            <div class="item">
                <label>头像</label>
                <div class="item_content">
                    <img style="width: 50px;" v-if="athleteInformation.avator" :src="`${HOST}/media/${athleteInformation.avator}`" alt="">
                </div>
            </div>
            <div class="item">
                <label>选手姓名</label>
                <div class="item_content">{{ athleteInformation.name }}</div>
            </div>
            <div class="item">
                <label>选手描述</label>
                <div class="item_content">{{ athleteInformation.detail }}</div>
            </div>  
        </div>
    </div>
</template>

<script setup>
import { fether } from '@/utils/fether';
import { reactive, defineEmits } from 'vue';
import { useRoute } from 'vue-router'
import { useStore } from "vuex";
import {HOST}from '../ENV'

const emit = defineEmits(['returnPage'])

const $route = useRoute()
const athleteInformation = reactive({})
const $store = useStore();
const props = defineProps({
  data: {
    informationKey: Number
  },
});

// 获取选手详情
const getAthleteInformation = async () => {
    let Arr = []
    let result = await fether(`/votetarget/?vote_id=${$route.query.vote_id}`)
    result.map(item => {
        Arr.push({...item.fields, pk: item.pk, model: item.model})
    })
    let arr = []
    arr = Arr.filter(item => { return item.pk === props.data })
    athleteInformation.avator = arr[0].avator;
    athleteInformation.name = arr[0].name;
    athleteInformation.detail = arr[0].detail;
}
getAthleteInformation()

const returnPage = () => {
    let params = {
        status: true
    }
    emit('returnPage', params)
}
</script>

<style lang="scss" scoped>
.body{
    height: 100%;
}
.body_title{
    height: 50px;
    padding: 0px 20px;
    display: flex;
    align-items: center;
    text-align: center;
}
.body_title > button{
    width: 50px;
    height: 20px;
}
.body_title > span{
    margin: auto;
}
.grid-container {
  display: grid;
  grid-template-columns: auto auto;
  grid-gap: 10px;
  padding: 10px;
}

.grid-container > .item {
  text-align: center;
  font-size: 15px;
}
.item_content{
    height: 50px;
}
</style>