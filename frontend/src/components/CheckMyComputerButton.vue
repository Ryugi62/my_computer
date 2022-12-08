<template>
  <div class="buttonBackground">
    <button
      type="button"
      class="checkButton btn btn-primary"
      @click="goListPage"
    >
      내 PC 사양 확인하기
    </button>
  </div>
</template>

<script>
export default {
  name: "CheckMyComputerButton",

  methods: {
    goListPage() {
      this.$router.push("/gameList");
    },
  },
};
</script>

<style scoped>
.buttonBackground {
  height: 100%;
  display: flex;
  background-color: #f0f0f0;
}

.checkButton {
  width: 80%;
  color: white;
  margin: auto;
  height: 100px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #4472c4;
}
</style>
