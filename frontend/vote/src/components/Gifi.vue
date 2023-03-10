<template>
  <div class="gift" @click="props.method.close">
    <div class="gift_body">
      <div class="gift_body_wrap">
        <!-- <div class="title">为选手{{ props.data }}助力</div> -->
        <div class="gift_body_list">
          <div
            :style="{
              backgroundColor: item.isClick ? '#f5c85f' : '',
              borderRadius: '5px',
            }"
            v-for="item in giftList"
            @click="selectPrize(item.name)"
          >
            <img
              class="gift_body_list_img"
              :src="HOST + '/media/' + item.img"
              alt=""
            />
          </div>
        </div>
        <div class="pay">
          <div class="pay_body">
            <svg
              t="1678370002788"
              class="icon"
              viewBox="0 0 1228 1024"
              version="1.1"
              xmlns="http://www.w3.org/2000/svg"
              p-id="1126"
              width="30"
              height="30"
            >
              <path
                d="M530.8928 703.1296a41.472 41.472 0 0 1-35.7376-19.8144l-2.7136-5.5808L278.272 394.752a18.7392 18.7392 0 0 1-2.048-8.1408 19.968 19.968 0 0 1 20.48-19.3536c4.608 0 8.8576 1.4336 12.288 3.84l234.3936 139.9296a64.4096 64.4096 0 0 0 54.528 5.9392L1116.2624 204.8C1004.9536 80.896 821.76 0 614.4 0 275.0464 0 0 216.576 0 483.6352c0 145.7152 82.7392 276.8896 212.2752 365.5168a38.1952 38.1952 0 0 1 17.2032 31.488 44.4928 44.4928 0 0 1-2.1504 12.3904l-27.6992 97.4848c-1.3312 4.608-3.328 9.3696-3.328 14.1312 0 10.752 9.216 19.3536 20.48 19.3536 4.4032 0 8.0384-1.536 11.776-3.584l134.5536-73.3184c10.1376-5.5296 20.7872-8.96 32.6144-8.96 6.2976 0 12.288 0.9216 18.0736 2.5088 62.72 17.0496 130.4576 26.5728 200.5504 26.5728C953.7024 967.168 1228.8 750.592 1228.8 483.6352c0-80.9472-25.4464-157.1328-70.0416-224.1024l-604.9792 436.992-4.4544 2.4064a42.1376 42.1376 0 0 1-18.432 4.1984z"
                fill="#15BA11"
                p-id="1127"
              ></path>
            </svg>
            <div>微信支付</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { HOST } from "@/ENV";
import { fether } from "@/utils/fether";
import { reactive } from "vue";
import { useRoute } from "vue-router";
const $route = useRoute();

const props = defineProps({
  data: String,
  method: { close: () => {}, state: Boolean },
});

const giftList = reactive([]);

const getGiftList = async () => {
  let result = await fether(`/gift/?vote_id=${$route.query.vote_id}`);
  if (!result) return;
  result.forEach((item) => {
    giftList.push({ ...item.fields, isClick: false });
  });
  console.log(giftList);
};

// 选择礼物
const selectPrize = (target) => {
  for (let i = 0; i < giftList.length; i++) {
    if (giftList[i].name === target) {
      giftList[i].isClick = true;
    } else {
      giftList[i].isClick = false;
    }
  }
};

getGiftList();
</script>

<style lang="scss" scoped>
.gift {
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
.gift_body {
  background-color: #f3f3f3;
  border-radius: 5px;
  padding: 10px;
  width: 90%;
}
.gift_body_wrap{
  padding: 10px;
  background-color: white;
  border-radius: 10px;
}
.gift_body_list {
  margin: 10px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 10px;
  text-align: center;
}
.gift_body_list_img {
  width: 50px;
  height: 50px;
  margin: 10px 10px;
}
.title {
  background-color: rgb(170, 43, 43);
  border-radius: 5px 5px 0px 0px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  color: white;
  font-size: 20px;
  padding: 10px 0px;
}
.pay {
  background-color: green;
  border-radius: 0px 0px 5px 5px;
  height: 30px;
  line-height: 30px;
  padding: 10px 0px;
  font-size: 20px;
  text-align: center;
  color: white;
}
.pay_body {
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
}
</style>
