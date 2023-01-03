<template>
  <div class="buttonBackground">
    <button
      type="button"
      class="checkButton btn btn-primary"
      @click="goListPage"
    >
      내 PC 사양 확인하기 <br />
      (버튼을 눌러 프로그램을 설치 후 실행해주세요.)
    </button>

    <DownloadButton />
  </div>
</template>

<script>
import DownloadButton from "@/components/DownloadProgramButton.vue";

export default {
  name: "CheckMyComputerButton",

  components: {
    DownloadButton,
  },

  methods: {
    goListPage() {
      this.$router.push("/myHardware");
    },
  },
};
</script>

<style scoped>
.buttonBackground {
  width: 100%;
  color: #4472c4;
  height: 100%;
  display: flex;
  flex-direction: column;
  background-color: #f0f0f0;
}

.downloadButton {
  width: 50%;
  color: #4472c4;
  height: 100px;
  cursor: pointer;
  margin: 0 auto auto auto;
  display: flex;
  max-width: 455px;
  align-items: center;
  justify-content: center;
}

.checkButton {
  width: 50%;
  max-width: 455px;
  color: white;
  margin: auto auto 0 auto;
  height: 100px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #4472c4;
}
</style>
