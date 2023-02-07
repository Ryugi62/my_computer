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
@font-face {
  font-family: "BMJUA";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/BMJUA.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

* {
  /* border: 1px solid red; */
}

html,
body,
#app {
  font-family: BMJUA;
  margin: 0;
  height: 100%;
}
</style>
