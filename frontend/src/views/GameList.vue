<template>
  <div class="gameListBackground">
    <div class="tableBox">
      <table class="table table-bordered table-hover">
        <thead>
          <tr>
            <th scope="col">게임</th>
            <th scope="col">CPU (시피유)</th>
            <th scope="col">Drive (하드용량)</th>
            <th scope="col">외장 VGA (외장그래픽카드)</th>
            <th scope="col">내장 VGA (내장그래픽카드)</th>
            <th scope="col">OS (윈도우 버전)</th>
            <th scope="col">Ram (메모리)</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="game in gameInformationArr" :key="game.id">
            <td v-for="key in Object.keys(game)" :key="key">
              <template v-if="key !== 'game_name'">
                <!-- font-color green -->
                <i
                  class="fas fa-check okCheck"
                  v-if="compareInfo(key, game[key], computerInformation[key])"
                >
                </i>
                <i class="fas fa-times notCheck" v-else> </i>
              </template>
              <template v-else>
                {{ game[key] }}
              </template>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="shareButtonBox">
      <button class="btn btn-primary shareButton" @click="clickedShareButton">
        내 PC사양 공유하기
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      computerInformation: {
        cpu: "X",
        drive: "X",
        external_vga: "X",
        internal_vga: "X",
        os: "X",
        ram: "X",
      },

      theadTitleArr: [
        "게임",
        "CPU (시피유)",
        "Drive (하드용량)",
        "외장 VGA (외장그래픽카드)",
        "내장 VGA (내장그래픽카드)",
        "OS (윈도우 버전)",
        "Ram (메모리)",
      ],

      gameInformationArr: [
        {
          game_name: "League of Legends",
          cpu: "AMD Ryzen 5 3600",
          drive_capacity: "500GB",
          external_vga: "NVIDIA GeForce GTX 1660 SUPER",
          internal_vga: "AMD Radeon RX 5500 XT",
          os: "Windows 10",
          ram: "16GB",
        },
        {
          game_name: "Overwatch",
          cpu: "AMD Ryzen 5 3600",
          drive_capacity: "500GB",
          external_vga: "NVIDIA GeForce GTX 1660 SUPER",
          internal_vga: "AMD Radeon RX 5500 XT",
          os: "Windows 10",
          ram: "16GB",
        },
        {
          game_name: "World of Warcraft",
          cpu: "AMD Ryzen 5 3600",
          drive_capacity: "500GB",
          external_vga: "NVIDIA GeForce GTX 1660 SUPER",
          internal_vga: "AMD Radeon RX 5500 XT",
          os: "Windows 10",
          ram: "16GB",
        },
        {
          game_name: "Counter-Strike: Global Offensive",
          cpu: "AMD Ryzen 5 3600",
          drive_capacity: "500GB",
          external_vga: "NVIDIA GeForce GTX 1660 SUPER",
          internal_vga: "AMD Radeon RX 5500 XT",
          os: "Windows 10",
          ram: "16GB",
        },
        {
          game_name: "Grand Theft Auto V",
          cpu: "AMD Ryzen 5 3600",
          drive_capacity: "500GB",
          external_vga: "NVIDIA GeForce GTX 1660 SUPER",
          internal_vga: "AMD Radeon RX 5500 XT",
          os: "Windows 10",
          ram: "16GB",
        },
        {
          game_name: "PLAYERUNKNOWN'S BATTLEGROUNDS",
          cpu: "AMD Ryzen 5 3600",
          drive_capacity: "500GB",
          external_vga: "NVIDIA GeForce GTX 1660 SUPER",
          internal_vga: "AMD Radeon RX 5500 XT",
          os: "Windows 10",
          ram: "16GB",
        },
        {
          game_name: "Fortnite",
          cpu: "AMD Ryzen 5 3600",
          drive_capacity: "500GB",
          external_vga: "NVIDIA GeForce GTX 1660 SUPER",
          internal_vga: "AMD Radeon RX 5500 XT",
          os: "Windows 10",
          ram: "16GB",
        },
      ],
    };
  },

  mounted() {
    this.getMyIP();

    this.getGameList();
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
        // cpu: "X",
        // drive: "X",
        // external_vga: "X",
        // internal_vga: "X",
        // os: "X",
        // ram: "X",

        cookieObj.cpu === "X" ||
        cookieObj.drive === "X" ||
        cookieObj.external_vga === "X" ||
        cookieObj.internal_vga === "X" ||
        cookieObj.os === "X" ||
        cookieObj.ram === "X"
      ) {
        console.log("쿠키가 없어서 서버에서 정보를 가져옵니다.");
        this.getComputerInfo(this.getMyIP);
      } else {
        this.setComputerInfo(cookieObj);
      }
    },

    setComputerInfo(data) {
      const { cpu, drive, external_vga, internal_vga, os, ram } = data;

      this.computerInformation.cpu = cpu;
      this.computerInformation.drive = drive;
      this.computerInformation.external_vga = external_vga;
      this.computerInformation.internal_vga = internal_vga;
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
          const { cpu, drive, external_vga, internal_vga, os, ram } =
            response.data[response.data.length - 1];

          document.cookie = `cpu=${cpu};`;
          document.cookie = `drive=${drive};`;
          document.cookie = `external_vga=${external_vga};`;
          document.cookie = `internal_vga=${internal_vga};`;
          document.cookie = `os=${os};`;
          document.cookie = `ram=${ram};`;

          this.setComputerInfo(response.data[response.data.length - 1]);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    getGameList() {
      axios
        .post("/api/getGameList")
        .then((response) => {
          const tempArray = response.data;

          tempArray.forEach((game) => {
            game.cpu = this.computerInformation.cpu.includes("AMD")
              ? game.cpu.amd
              : game.cpu.intel;
          });

          this.gameInformationArr = new Array().concat(tempArray);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    compareInfo(key, game, com) {
      if (com === "X") return false;

      console.log(key, game, com);
      if (key === "cpu") {
        com = com.includes("AMD")
          ? com.split(" ").slice(0, 4).join(" ")
          : com.split(" ")[0];
        return com.toLowerCase() >= game.toLowerCase();
      } else if (key === "drive" || key === "ram") {
        return Number(com.split(" ")[0]) >= Number(game.split(" ")[0]);
      } else if (key.includes("vga")) {
        // 문자열의 첫번째 단어 삭제 (Nvidia, AMD)
        let vga = com.split(" ");
        vga = vga.slice(1, vga.length).join(" ");

        return vga.toLowerCase() >= game.toLowerCase();
      } else if (key === "os") {
        return Number(com.split("-")[1]) >= Number(game.split(" ")[1]);
      }
    },

    clickedShareButton() {
      window.Kakao.Share.sendDefault({
        objectType: "text",
        text: `내 PC사양은\n CPU: ${this.computerInformation.cpu},\n Drive: ${this.computerInformation.drive_capacity},\n EXTERNAL_VGA: ${this.computerInformation.external_vga},\n INTERNAL_VGA: ${this.computerInformation.internal_vga},\n OS: ${this.computerInformation.os},\n Ram: ${this.computerInformation.ram} 입니다.`,
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
.gameListBackground {
  width: 100%;
  height: 100%;
  min-width: 720px;
  border-left: 1px solid #dee2e6;
  border-right: 1px solid #dee2e6;
}

.tableBox {
  width: 100%;
  height: 90%;
}

table {
  border-color: black;
}

thead {
  background-color: #000000c2;
  color: white;
}

tbody {
  overflow-y: scroll;
  background-color: #f8f9fa;
}

td:not(:first-child),
thead:not(:first-child) {
  text-align: center;
}

.okCheck {
  color: green;
}

.notCheck {
  color: red;
}

.shareButtonBox {
  width: 100%;
  height: 10%;
  display: flex;
}

.shareButton {
  margin: auto;
  background: #4472c4;
}
</style>
