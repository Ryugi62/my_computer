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
      <table class="table">
        <thead>
          <tr>
            <th
              scope="col"
              v-for="(theadTitle, idx) of computerInformation"
              :key="idx"
            >
              {{ computerParts[idx] }}
            </th>
          </tr>
        </thead>
        <tbody>
          <td v-for="(info, idx2) in computerInformation" :key="idx2">
            {{ info }}
          </td>
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
  data() {
    return {
      computerInformation: {
        cpu: "X",
        drive_capacity: "X",
        graphic_card: "X",
        os: "X",
        ram: "X",
      },

      computerParts: {
        cpu: "CPU (시피유)",
        drive_capacity: "Drive (하드용량)",
        graphic_card: "VGA (그래픽카드)",
        os: "OS (윈도우 버전)",
        ram: "Ram (메모리)",
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
      const { cpu, drive_capacity, graphic_card, os, ram } = data;

      this.computerInformation.cpu = cpu;
      this.computerInformation.drive_capacity = drive_capacity;
      this.computerInformation.graphic_card = graphic_card;
      this.computerInformation.os = os;
      this.computerInformation.ram = ram;
    },

    getMyIP() {
      let ip = "";
      axios
        .get("https://api.ipify.org?format=json")
        .then((response) => {
          ip = response.data.ip;
          this.getComputerInfo(ip);
        })
        .catch((error) => {
          console.log(error);
        });
      return ip;
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
          document.cookie = `cpu=${response.data[0].cpu}`;
          document.cookie = `drive_capacity=${response.data[0].drive_capacity}`;
          document.cookie = `graphic_card=${response.data[0].graphic_card}`;
          document.cookie = `os=${response.data[0].os}`;
          document.cookie = `ram=${response.data[0].ram}`;

          this.setComputerInfo(response.data[0]);
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
  width: 80%;
  height: fit-content;
  margin: auto auto 10px auto;
}

table {
  text-align: center;
}

th {
  border: 1px solid black;
  padding: 10px;
}

td {
  border: 1px solid black;
  padding: 10px;
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
