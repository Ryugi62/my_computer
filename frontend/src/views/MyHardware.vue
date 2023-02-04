<template>
  <div class="myHardwareBackground">
    <ins
      class="kakao_ad_area advertisement"
      style="display: none"
      data-ad-unit="DAN-6U9FgS8SxjRyM0qS"
      data-ad-width="300"
      data-ad-height="250"
    ></ins>

    <div class="hardwareTableBox">
      <!-- thead left tbody right table, border 1px black-->
      <table class="table table-bordered table-hover">
        <!-- thead width -->
        <thead>
          <tr>
            <th scope="col" class="tableHeader">컴퓨터 부품</th>
            <th scope="col" class="tableHeader">내 PC사양</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(value, key) in computerParts" :key="key">
            <!-- th width is short than td -->
            <th scope="row" class="tableBody">{{ value }}</th>
            <td class="tableBody">{{ computerInformation[key] }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <DownloadButton />

    <div class="hardwareButtonBox">
      <div class="mb1">
        <button class="btn btn-primary shareButton" @click="clickedShareButton">
          내 PC사양 공유하기
        </button>
      </div>

      <div class="mb1">
        <button
          class="btn btn-light goGameListButton"
          @click="this.$router.push('/gameList')"
        >
          가능한 게임 확인하기
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import DownloadButton from "@/components/DownloadProgramButton.vue";
import axios from "axios";

export default {
  name: "MyHardware",

  data() {
    return {
      computerParts: {
        cpu: "CPU (시피유)",
        mainboard: "M/B 메인보드",
        external_vga: "외장 VGA (외장그래픽카드)",
        internal_vga: "내장 VGA (내장그래픽카드)",
        ram: "RAM (메모리)",
        drive: "Drive (하드용량)",
        os: "OS (운영체제)",
      },

      computerInformation: {
        cpu: "X",
        mainboard: "X",
        external_vga: "X",
        internal_vga: "X",
        ram: "X",
        drive: "X",
        os: "X",
      },
    };
  },

  components: {
    DownloadButton,
  },

  mounted() {
    this.getMyIP();
  },

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

    setComputerData() {
      let cookieObj = this.getCookie();
      if (
        cookieObj.cpu === "" ||
        cookieObj.drive_capacity === "" ||
        cookieObj.graphic_card === undefined ||
        cookieObj.os === "" ||
        cookieObj.ram === ""
      ) {
        console.log("쿠키가 없어서 서버에서 정보를 가져옵니다.");
        this.getComputerInfo(this.getMyIP);
      } else {
        this.setComputerInfo(cookieObj);
      }
    },

    setComputerInfo(data) {
      // cpu, mainboard, external_vga, internal_vga, ram, drive, os
      this.computerInformation.cpu = data.cpu;
      this.computerInformation.mainboard = data.mainboard;
      this.computerInformation.external_vga = data.external_vga;
      this.computerInformation.internal_vga = data.internal_vga;
      this.computerInformation.ram = data.ram;
      this.computerInformation.drive = data.drive;
      this.computerInformation.os = data.os;
    },

    getMyIP() {
      let ip = "";
      axios
        .get("https://api.ipify.org?format=json")
        .then((response) => {
          ip = response.data.ip;
          console.log(ip);
          this.getComputerInfo(ip);
        })
        .catch((error) => {
          console.log(error);
        });
      return ip;
      k;
    },

    getComputerInfo(ip) {
      axios
        .post("/api/getHardware", {
          headers: {
            "Content-Type": "application/json",
          },
          json: {
            ip: ip,
          },
        })
        .then((response) => {
          const { cpu, mainboard, external_vga, internal_vga, ram, drive, os } =
            response.data[response.data.length - 1];

          document.cookie = `cpu=${cpu};`;
          document.cookie = `mainboard=${mainboard};`;
          document.cookie = `external_vga=${external_vga};`;
          document.cookie = `internal_vga=${internal_vga};`;
          document.cookie = `ram=${ram};`;
          document.cookie = `drive_capacity=${drive};`;
          document.cookie = `os=${os};`;
          this.setComputerInfo(response.data[response.data.length - 1]);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    clickedShareButton() {
      window.Kakao.Share.sendDefault({
        objectType: "text",
        text: `내 PC사양은\n CPU: ${this.computerInformation.cpu},\n Drive: ${this.computerInformation.drive_capacity}\n VGA: ${this.computerInformation.graphic_card}\n OS: ${this.computerInformation.os}\n Ram: ${this.computerInformation.ram} 입니다.`,
        link: {
          mobileWebUrl: "https://developers.kakao.com",
          webUrl: "https://developers.kakao.com",
        },
      });
    },
  },
};
</script>

<style scoped>
.myHardwareBackground {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  text-align: center;
}

.advertisement {
  margin: auto;
}

.hardwareTableBox {
  width: 70%;
  height: fit-content;
  margin: auto auto 10px auto;
}

table {
  width: 100%;
  border-color: black;
  border-collapse: collapse;
}

thead {
  background-color: #000000c2;
  color: white;
}

/* th width is more short than td */
th {
  width: 30%;
}

td {
  width: 70%;
}

.hardwareButtonBox {
  margin: 10px auto auto auto;
  display: flex;
}

.hardwareButtonBox > div {
  margin: 0 20px;
}

.goGameListButton {
  border: 1px solid black;
}
</style>
