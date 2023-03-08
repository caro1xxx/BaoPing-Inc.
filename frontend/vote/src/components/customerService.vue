<template>
    <div class="body">
        <div class="body_content">
            <div class="body_content_config">
                <div class="body_content_config_top">
                    <div></div>
                </div>
                <div class="body_content_config_botton">{{ customerData.data }}</div>
            </div>
        </div>
        <img @click="returnPage" class="downImg" style="width: 30px;height: 30px;" src="../assets/images/39.png" alt="">
    </div>
</template>

<script setup>
import { defineEmits, reactive, computed } from 'vue'
import { useStore } from "vuex";
const emit = defineEmits(['returnPage'])

const $store = new useStore()

const customerData = reactive({
    data: ''
})

const returnPage = (value) => {
    let params = {
        status: value
    }
    emit('returnPage', params)
}



let result = computed(() => {
return $store.state.settings[82]
})
customerData.data = result.value.value

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
  z-index: 6;
}
.body_content{
    width: 80%;
    height: 60%;
    background-color: #f3f3f3;
    border-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.body_content_config{
    width: calc(100% - 20px);
    height: calc(100% - 20px);
    border-radius: 10px;
    background-color: #ffffff;
}
.body_content_config_top{
    height: 40px;
    display: flex;
    justify-content: center;
    div{
        width: 60%;
        height: 100%;
        background-color: red;
        border-radius: 0px 0px 35px 35px;
    }
}
.body_content_config_botton{
    padding: 10px;
}
.downImg{
    position: absolute;
    top: 155px;
    left: 365px;
}
</style>