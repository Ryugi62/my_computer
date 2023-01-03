<template>
  <div class="advertisementBox">
    <ins
      class="kakao_ad_area advertisement"
      style="display: none"
      data-ad-unit="DAN-6U9FgS8SxjRyM0qS"
      data-ad-width="300"
      data-ad-height="250"
    ></ins>
  </div>
</template>

<script>
export default {
  name: "MyComputer_Advertisement",
};
</script>

<style scoped>
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
