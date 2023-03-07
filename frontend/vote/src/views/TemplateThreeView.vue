<template>
    <div class="body"></div>
</template>

<script setup>
import { fether } from '@/utils/fether';
import { useRoute } from 'vue-router'
const $route = useRoute()

console.log($route.query);
</script>

<style lang="scss" scoped>

</style>