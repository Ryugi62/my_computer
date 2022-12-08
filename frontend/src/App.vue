<template>
  <MyComputerHeader />
  <MyComputerBody />
</template>

<script>
import MyComputerHeader from "./components/MyComputerHeader.vue";
import MyComputerBody from "./page/MyComputerBody.vue";

export default {
  name: "MyComputer",
  components: {
    MyComputerHeader,
    MyComputerBody,
  },
};
</script>

<style>
* {
  /* border: 1px solid red; */
}

html,
body,
#app {
  margin: 0;
  height: 100%;
}
</style>
