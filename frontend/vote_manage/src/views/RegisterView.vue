<template>
  <div class="register"></div>
  <div class="register_mask">
    <!-- <div class="register_mask_body">1</div> -->
  </div>
</template>

<script setup></script>

<style lang="scss" scoped>
.register {
  width: calc(100vw - 150px - 400px);
  height: calc(100vh);
  background-color: #fff;
}
.register_mask {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 10;
  background-color: #3c3c3c62;
}
/* .register_mask_body {
  position: absolute;
  background-color: white;
} */
</style>
