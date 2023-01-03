<template>
  <div class="bodyBackground">
    <div class="bodyLeft"></div>
    <div class="bodyCenter">
      <router-view />
    </div>
    <div class="bodyRight">
      <advertisement style="width: 300px; height: 300px" />
    </div>
  </div>
</template>

<script>
import Advertisement from "@/components/Advertisement.vue";

export default {
  components: {
    Advertisement,
  },
};
</script>

<style scoped>
.bodyBackground {
  width: 100%;
  height: calc(100% - 50px);
  display: flex;
  background-color: #f0f0f0;
}

.bodyLeft {
  width: 250px;
  height: 100%;
}

.bodyCenter {
  width: calc(100% - 500px);
  height: 100%;
  overflow: scroll;
}

.bodyRight {
  width: 250px;
  height: 100%;
}
</style>
