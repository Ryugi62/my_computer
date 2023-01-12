<template>
  <div class="bodyBackground">
    <div class="bodyLeft">
      <ins
        class="kakao_ad_area"
        style="display: none"
        data-ad-unit="DAN-UFn2FTVzZaa5HgMa"
        data-ad-width="160"
        data-ad-height="600"
      ></ins>
    </div>
    <div class="bodyCenter">
      <router-view />
    </div>
    <div class="bodyRight">
      <!-- <div class="advertisementBox">
        <Advence />
      </div> -->
    </div>
  </div>
</template>

<script>
// import Advence from "@/components/Advence.vue";

export default {
  // components: { Advence },
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
  width: calc(100% - 550px);
  height: 100%;
  overflow: scroll;
}

.bodyRight {
  width: 300px;
  height: 100%;
}

.advertisementBox {
  border: 1px solid black;
  display: flex;
  overflow: hidden;
}

.advertisement {
  margin: auto;
}

.advertisement * {
  object-fit: contain;
}
</style>
