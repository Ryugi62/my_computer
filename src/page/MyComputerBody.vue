<template>
  <div class="bodyBackground">
    <div class="bodyLeft">
      <advertisement />
      <advertisement />
    </div>
    <div class="bodyCenter">
      <router-view />
    </div>
    <div class="bodyRight">
      <advertisement />
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
  width: 200px;
  height: 100%;
}

.bodyCenter {
  width: calc(100% - 400px);
  height: 100%;
}

.bodyRight {
  width: 200px;
  height: 100%;
}
</style>
