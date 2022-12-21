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
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CheckMyComputerButton",

  methods: {
    getCookie() {
      let cookieArr = document.cookie.split("; ");
      let cookieObj = {};
      cookieArr.forEach((cookie) => {
        let cookieSplit = cookie.split("=");
        cookieObj[cookieSplit[0]] = cookieSplit[1];
      });

      return cookieObj;
    },

    goListPage() {
      const {
        bios,
        cpu,
        drive_capacity,
        graphic_card,
        mainboard_manufacturer,
        os,
        ram,
      } = this.getCookie();

      if (
        bios === "" ||
        cpu === "" ||
        drive_capacity === "" ||
        graphic_card === undefined ||
        mainboard_manufacturer === "" ||
        os === "" ||
        ram === ""
      ) {
        axios({
          url: "http://localhost:3000/api/getProgram",
          method: "GET",
          responseType: "blob",
        }).then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute("download", "download.zip");
          document.body.appendChild(link);
          link.click();
        });
      } else {
        this.$router.push("/gameList");
      }
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
  width: 50%;
  max-width: 455px;
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
