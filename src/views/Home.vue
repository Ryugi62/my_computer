<template>
  <div class="homeBox">
    <checkMyComputerButton />
  </div>
</template>

<script>
import CheckMyComputerButton from "@/components/CheckMyComputerButton.vue";

export default {
  name: "MyComputer_Home",

  components: {
    CheckMyComputerButton,
  },
};
</script>

<style scoped>
.homeBox {
  width: 100%;
  height: 100%;
}
</style>
