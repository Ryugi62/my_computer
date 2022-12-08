<template>
  <div class="bodyBackground">
    <router-view></router-view>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.bodyBackground {
  width: 100%;
  height: calc(100% - 50px);
  background-color: #f0f0f0;
}
</style>
