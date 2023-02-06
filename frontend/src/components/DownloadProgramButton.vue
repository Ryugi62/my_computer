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
        link.setAttribute("download", "my_computer.zip");
        document.body.appendChild(link);
        link.click();
      });
    },
  },
};
</script>

<style scoped>
.downloadButton {
  width: fit-content;
  color: #4472c4;
  margin: 0 auto;
  cursor: pointer;
  text-align: center;
}
.downloadButton:hover {
  text-decoration: underline;
  background-color: #e5e5e5;
}
</style>
