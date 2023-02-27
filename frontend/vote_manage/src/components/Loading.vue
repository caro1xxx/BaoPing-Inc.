<template>
  <div class="loading">
    <div class="loading_body"></div>
  </div>
</template>

<script setup></script>

<style lang="scss" scoped>
.loading {
  position: absolute;
  top: 0%;
  bottom: 0%;
  left: 0%;
  right: 0%;
  z-index: 5;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #e0e0e095;
}
.loading_body {
  width: 30px;
  height: 30px;
  border: 3px solid #2460e5;
  border-top-color: transparent;
  border-radius: 100%;

  animation: circle infinite 0.75s linear;
}
@keyframes circle {
  0% {
    transform: rotate(0);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
