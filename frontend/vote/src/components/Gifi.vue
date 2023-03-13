<template>
  <div class="gift" @click="props.method.close">
    <div class="gift_wrap">
      <div
        class="gift_body"
        @click="
          (e) => {
            e.stopPropagation();
          }
        "
      >
        <div class="title">为您支持的选手送出一份鼓励</div>
        <div class="item_wrap">
          <div
            v-for="item in giftList"
            class="gift_body_item"
            :style="{ backgroundColor: item.isClick ? '#cecece' : '' }"
            @click="selectPrize(item.name)"
          >
            <img class="img" :src="HOST2 + '/media/' + item.img" alt="" />
            <div style="width: 50%; padding-left: 10px">
              <div class="name">{{ item.name }}</div>
              <div class="description">价值{{ item.value }}个赞</div>
            </div>
            <div class="price">{{ item.price }}.00 元</div>
          </div>
        </div>
        <div class="checkout">
          <div class="total">
            <div style="width: 40%">总价:</div>
            <div style="width: 60%; text-align: end">
              {{ currentSelect.price }}.00
            </div>
          </div>
          <div class="sloder">
            <div style="width: 40%">价值:</div>
            <div style="width: 60%; text-align: end">
              {{ currentSelect.value }}
            </div>
          </div>
        </div>
        <div class="pay">
          <svg
            t="1678720522592"
            class="icon"
            viewBox="0 0 1228 1024"
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            p-id="1484"
            width="30"
            height="30"
          >
            <path
              d="M530.8928 703.1296a41.472 41.472 0 0 1-35.7376-19.8144l-2.7136-5.5808L278.272 394.752a18.7392 18.7392 0 0 1-2.048-8.1408 19.968 19.968 0 0 1 20.48-19.3536c4.608 0 8.8576 1.4336 12.288 3.84l234.3936 139.9296a64.4096 64.4096 0 0 0 54.528 5.9392L1116.2624 204.8C1004.9536 80.896 821.76 0 614.4 0 275.0464 0 0 216.576 0 483.6352c0 145.7152 82.7392 276.8896 212.2752 365.5168a38.1952 38.1952 0 0 1 17.2032 31.488 44.4928 44.4928 0 0 1-2.1504 12.3904l-27.6992 97.4848c-1.3312 4.608-3.328 9.3696-3.328 14.1312 0 10.752 9.216 19.3536 20.48 19.3536 4.4032 0 8.0384-1.536 11.776-3.584l134.5536-73.3184c10.1376-5.5296 20.7872-8.96 32.6144-8.96 6.2976 0 12.288 0.9216 18.0736 2.5088 62.72 17.0496 130.4576 26.5728 200.5504 26.5728C953.7024 967.168 1228.8 750.592 1228.8 483.6352c0-80.9472-25.4464-157.1328-70.0416-224.1024l-604.9792 436.992-4.4544 2.4064a42.1376 42.1376 0 0 1-18.432 4.1984z"
              fill="#fff"
              p-id="1485"
            ></path>
          </svg>
          微信支付
        </div>
      </div>
      <div class="close">点击其他位置关闭弹窗</div>
    </div>
  </div>
</template>

<script setup>
import { HOST2 } from "@/ENV";
import { fether } from "@/utils/fether";
import { reactive } from "vue";
import { useRoute } from "vue-router";
const $route = useRoute();

const props = defineProps({
  data: String,
  method: { close: () => {}, state: Boolean },
});

const currentSelect = reactive({ value: 0, price: 0 });

const giftList = reactive([]);

const getGiftList = async () => {
  let result = await fether(`/gift/?vote_id=${$route.query.vote_id}`);
  if (!result) return;
  result.forEach((item) => {
    giftList.push({ ...item.fields, isClick: false });
  });
};

// 选择礼物
const selectPrize = (target) => {
  for (let i = 0; i < giftList.length; i++) {
    if (giftList[i].name === target) {
      currentSelect.price = giftList[i].price;
      currentSelect.value = giftList[i].value;
      giftList[i].isClick = true;
    } else {
      giftList[i].isClick = false;
    }
  }
};

getGiftList();
</script>

<style lang="scss" scoped>
.checkout {
  border-top: 0.5px solid #aaa;
  padding-top: 10px;
  font-size: 13px;
  .total {
    display: flex;
    padding: 5px 20px;
    margin: 5px 0px;
  }
  .sloder {
    display: flex;
    padding: 5px 20px;
    margin: 5px 0px;
  }
}
.gift {
  position: absolute;
  top: 0px;
  right: 0;
  left: 0;
  bottom: 0;
  background-color: #00000074;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  z-index: 6;
}
.gift_wrap {
  background-color: #f3f3f3;
  width: 80%;
  border-radius: 5px;
  position: relative;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
}
.item_wrap {
  height: calc(30vh);
  overflow: scroll;
}
.gift_body {
  margin: 10px;
  background-color: white;
  border-radius: 5px;
  padding: 3px;
}
.item_wrap::-webkit-scrollbar {
  display: none;
}

.gift_body_item {
  display: flex;
  border-radius: 3px;
  .img {
    width: 40px;
    height: 40px;
    padding: 5px;
    border: 0.5px solid #d8d8d8;
    border-radius: 5px;
  }
  margin: 10px 0px;
  .name {
    font-size: 15px;
    font-weight: bold;
    line-height: 25px;
  }
  .description {
    font-size: 10px;
    color: #9f9f9f;
    line-height: 25px;
  }
  .price {
    width: 30%;
    text-align: end;
    line-height: 50px;
  }
}
.title {
  text-align: center;
  margin: 10px 0px 20px 0px;
}
.pay {
  height: 40px;
  background-color: #15ba11;
  border-radius: 5px;
  display: inline-flex;
  vertical-align: top;
  justify-content: center;
  align-items: center;
  width: calc(70vw - 10px);
  margin: 10px 15px 0px 15px;
  color: white;
}
.close {
  position: absolute;
  bottom: -30px;
  font-size: 10px;
  color: white;
  text-align: center;
}
</style>
