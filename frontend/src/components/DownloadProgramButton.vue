<template>
  <div class="downloadButton" @click="downloadProgram()">
    PC사양 확인 프로그램 다운로드
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "download_program_button",

  methods: {
    downloadProgram() {
      axios({
        url: "/api/getProgram",
        method: "POST",
        responseType: "blob",
      }).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "my_computer.exe");
        document.body.appendChild(link);
        link.click();
      });
    },
  },
};
</script>

<style scoped>
.downloadButton {
  color: #4472c4;
  cursor: pointer;
  text-align: center;
}
</style>
