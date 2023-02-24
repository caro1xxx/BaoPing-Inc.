<template>
  <div class="navbar">
    <div class="navbar_logo">
      <div class="navbar_logo_text">Vote</div>
    </div>
    <div class="navbar_midd">
      <div class="navbar_midd_body">
        <div class="navbar_midd_body_excuteing">
          <img
            src="../assets/img/16.png"
            alt=""
            class="icon_style navbar_icon"
          />
          <div>执行中</div>
          <img
            src="../assets/img/15.png"
            alt=""
            class="icon_style navbar_notify"
          />
        </div>
        <div class="navbar_midd_body_line"></div>
        <div class="navbar_midd_body_itemparent">
          <div
            v-for="item in navItme"
            :key="item"
            class="navbar_midd_body_itemFor"
            @click="SureMenu(item.path, item.type, item.name)"
            :style="{
              backgroundColor:
                item.type === 'child' && item.isClick ? '#4597e8' : '#fff',
            }"
          >
            <div v-if="item.img">
              <img
                v-if="!item.isClick"
                :src="item.img"
                alt=""
                class="icon_style"
              />
              <img v-else :src="item.clickImg" alt="" class="icon_style" />
            </div>
            <div
              v-if="item.type === 'parent'"
              class="navbar_midd_body_item"
              :style="{
                color: item.isClick ? '#4597e8' : '#b5c3d1',
              }"
            >
              {{ item.name }}
            </div>
            <div
              v-else
              class="navbar_midd_body_item"
              :style="{
                color: item.isClick ? '#fff' : '#b5c3d1',
              }"
            >
              {{ item.name }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from "vue";
import { useRouter } from "vue-router";
const router = useRouter();
// 记录上一次点击时的父菜单的子菜单信息
const prevSubNavBar = reactive({
  startIndex: 0,
  endIndex: 0,
});

// 导航项
let navItme = reactive([
  {
    name: "数据信息",
    img: require("../assets/img/2.png"),
    clickImg: require("../assets/img/9.png"),
    path: "/",
    isClick: false,
    type: "parent",
  },
  {
    name: "系统管理",
    img: require("../assets/img/5.png"),
    clickImg: require("../assets/img/12.png"),
    path: "/system",
    isClick: false,
    type: "parent",
  },
  {
    name: "消息管理",
    img: require("../assets/img/7.png"),
    clickImg: require("../assets/img/14.png"),
    path: "/news",
    isClick: false,
    type: "parent",
  },
  {
    name: "投票管理",
    img: require("../assets/img/3.png"),
    clickImg: require("../assets/img/10.png"),
    path: "/vote",
    isClick: false,
    type: "parent",
  },
  {
    name: "订单管理",
    img: require("../assets/img/4.png"),
    clickImg: require("../assets/img/11.png"),
    path: "/order",
    isClick: false,
    type: "parent",
  },
  {
    name: "粉丝管理",
    img: require("../assets/img/6.png"),
    clickImg: require("../assets/img/13.png"),
    path: "/vermicelli",
    isClick: false,
    type: "parent",
  },
  {
    name: "自动任务",
    img: require("../assets/img/1.png"),
    clickImg: require("../assets/img/8.png"),
    path: "/assignment",
    isClick: false,
    type: "parent",
  },
]);

// 二级菜单
const subNavItem = reactive([
  {
    name: "系统账户",
    path: "/systemuser",
    isClick: false,
    parentPath: "/system",
    type: "child",
  },
  {
    name: "系统设置",
    path: "/systemsetting",
    isClick: false,
    parentPath: "/system",
    type: "child",
  },
  {
    name: "全局域名",
    path: "/globaldomain",
    isClick: false,
    parentPath: "/system",
    type: "child",
  },
  {
    name: "权限分组",
    path: "/authgroup",
    isClick: false,
    parentPath: "/system",
    type: "child",
  },
  {
    name: "反馈信息",
    path: "/feedback",
    isClick: false,
    parentPath: "/news",
    type: "child",
  },
  {
    name: "信息修改",
    path: "/infoedit",
    isClick: false,
    parentPath: "/news",
    type: "child",
  },
  {
    name: "奖品申请",
    path: "/prizeapply",
    isClick: false,
    parentPath: "/news",
    type: "child",
  },
  {
    name: "活动管理",
    path: "/activemanage",
    isClick: false,
    parentPath: "/vote",
    type: "child",
  },
  {
    name: "投票记录",
    path: "/voterecord",
    isClick: false,
    parentPath: "/vote",
    type: "child",
  },
  {
    name: "礼物设置",
    path: "/giftsettingws",
    isClick: false,
    parentPath: "/vote",
    type: "child",
  },
  {
    name: "网友评论",
    path: "/netizencomment",
    isClick: false,
    parentPath: "/vote",
    type: "child",
  },
  {
    name: "支付记录",
    path: "/payrecod",
    isClick: false,
    parentPath: "/order",
    type: "child",
  },
]);

// 跳转路由
const SureMenu = (value, type, childName) => {
  if (value === "/") {
    router.push(`${value}`);
  }
  onClickNavbarItem(value, type, childName);
};

// 判断点击类型
const onClickNavbarItem = (path, type, childName) => {
  if (type === "child") {
    onClickChild(path, type, childName);
  } else onclickParent(path);
};

// 点击子菜单
const onClickChild = (path, type, childName) => {
  for (let i = 0; i < navItme.length; i++) {
    if (navItme[i].path === path && navItme[i].name === childName) {
      router.push(`${path}`);
      navItme[i].isClick = true;
    } else if (navItme[i].path !== path && type === navItme[i].type) {
      navItme[i].isClick = false;
    }
  }
};

// 点击父菜单
const onclickParent = (path) => {
  // 用于标识的变量
  let currentClickflag = 0;
  let sumChild = [];
  let isAppend = false;
  // 将父菜单中不存在parentPath属性的item返回
  navItme = navItme.filter((item) => !item.parentPath);
  // 循环判断点击的哪个菜单,并且记录
  for (let i = 0; i < navItme.length; i++) {
    if (navItme[i].path === path && !navItme[i].isClick) {
      currentClickflag = i;
      navItme[i].isClick = true;
      isAppend = navItme[i].isClick;
    } else {
      navItme[i].isClick = false;
    }
  }
  // 循环判断刚才点击的菜单所对应的所以子菜单
  for (let i = 0; i < subNavItem.length; i++) {
    if (subNavItem[i].parentPath === path) {
      sumChild.push(subNavItem[i]);
    }
  }

  // 记录起始index,结束index
  prevSubNavBar.startIndex = currentClickflag + 1;
  prevSubNavBar.endIndex = currentClickflag + sumChild.length;
  // 将二级菜单中起始index到结束index之间的元素push到父菜单中
  isAppend ? navItme.splice(currentClickflag + 1, 0, ...sumChild) : null;
};
</script>

<style lang="scss" scoped>
.navbar {
  user-select: none;
  width: 200px;
  height: calc(100vh);
  background-color: #fafdff;
  font-size: 10px;
  color: #b5c3d1;
}
.navbar_logo {
  font-size: 40px;
  font-weight: 700;
  font-style: italic;
  color: #4597e8;
  height: 72px;
  width: 100%;
  position: relative;
}
.navbar_logo_text {
  position: absolute;
  top: 36px;
  left: 32px;
}
.navbar_midd {
  width: 100%;
  height: calc(100vh - 102px);
}
.navbar_midd_body {
  margin: 0px 25px;
}
.navbar_midd_body_excuteing {
  display: flex;
  justify-content: center;
  position: relative;
  .navbar_icon {
    position: absolute;
    left: 10px;
    top: 71px;
  }
  padding-top: 76px;
}
.navbar_midd_body_line {
  height: 1px;
  padding-top: 22px;
  border-bottom: 1px solid #b5c3d17a;
}
.navbar_midd_body_item {
  margin: 10px 0px;
  cursor: pointer;
}
.navbar_midd_body_itemparent {
  padding-top: 63px;
}
.navbar_midd_body_itemFor {
  margin: 10px 0px;
  display: flex;
  justify-content: center;
  position: relative;
  border-radius: 5px;
  img {
    position: absolute;
    left: 10px;
    top: 5px;
  }
}
.navbar_notify {
  position: absolute;
  right: 10px;
  top: 75px;
  width: 20px;
  height: 20px;
}
</style>
