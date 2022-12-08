<template>
  <div class="homeBox">
    <div class="homeLeft">
      <div class="advertisementBackground">
        <advertisement />
      </div>
      <div class="advertisementBackground">
        <advertisement />
      </div>
    </div>
    <div class="homeCenter">
      <checkMyComputerButton />
    </div>
    <div class="homeRight">
      <div class="advertisementBackground">
        <advertisement />
      </div>
    </div>
  </div>
</template>

<script>
import Advertisement from "@/components/Advertisement.vue";
import CheckMyComputerButton from "@/components/CheckMyComputerButton.vue";

export default {
  name: "MyComputer_Home",

  components: {
    Advertisement,
    CheckMyComputerButton,
  },
};
</script>

<style scoped>
.homeBox {
  width: 100%;
  height: 100%;
  display: flex;
}

.homeLeft {
  width: 300px;
  height: 100%;
  background-color: #f0f0f0;
}

.advertisementBackground {
  width: 100%;
  height: 300px;
  object-fit: cover;
  background-color: #f0f0f0;
}

.homeCenter {
  width: calc(100% - 600px);
  height: 100%;
  background-color: #f0f0f0;
}

.homeRight {
  width: 300px;
  height: 100%;
  background-color: #f0f0f0;
}

.checkMyComputerButtonBackground {
  width: 100px;
  height: 100px;
  background-color: #f0f0f0;
}
</style>
