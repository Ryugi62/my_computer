<template>
  <div class="gameListBackground">
    <div class="tableBox">
      <table class="table">
        <thead>
          <tr>
            <th
              scope="col"
              v-for="(theadTitle, idx) of theadTitleArr"
              :key="idx"
            >
              {{ theadTitle }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(gameInformation, idx1) in gameInformationArr" :key="idx1">
            <td v-for="(info, idx2, l) in gameInformation" :key="idx2">
              <span v-if="idx2 === 'name'">{{ info }}</span>
              <i
                v-else-if="
                  compareInfo(gameInformation[partList[l - 1]], partList[l - 1])
                "
                class="fa-solid fa-check okCheck"
              />
              <i v-else class="fa-solid fa-x notCheck" />
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
        // cpu: "AMD Ryzen 7 5800X3D 8-Core Pro",
        // drive: "931 GB",
        // vga: "NVIDIA GeForce RTX 3060 Ti",
        // os: "Window-10-10.0.19045-SPO",
        // ram: "32 GB",
        cpu: "X",
        drive: "X",
        vga: "X",
        os: "X",
        ram: "X",
      },

      theadTitleArr: [
        "게임",
        "CPU (시피유)",
        "Drive (하드용량)",
        "VGA (그래픽카드)",
        "OS (윈도우 버전)",
        "Ram (메모리)",
      ],

      partList: ["cpu", "drive", "vga", "os", "ram"],

      gameInformationArr: [],
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

    compareInfo(info, idx2) {
      if (info === "X") return false;

      if (idx2 === "cpu") {
        let userCpuName = "";
        const userCpu = this.computerInformation[idx2];
        const temp = userCpu.split(" ");

        if (userCpu.includes("AMD")) {
          // temp [ 0 ~ 3 ] : Amd Ryzen 7 5800X
          userCpuName = temp[0] + " " + temp[1] + " " + temp[2] + " " + temp[3];
        } else {
          // temp [ 0 ~ 2 ] : Intel Core i7-10700K
          userCpuName = temp[2];
        }
        return userCpuName.toLowerCase() >= info.toLowerCase();
      } else if (idx2 === "drive" || idx2 === "ram") {
        return (
          Number(this.computerInformation[idx2].split(" ")[0]) >=
          Number(info.split(" ")[0])
        );
      } else if (idx2 === "vga") {
        // 문자열의 첫번째 단어 삭제 (Nvidia, AMD)
        const vga = this.computerInformation[idx2].split(" ");
        vga.shift();
        this.computerInformation[idx2] = vga.join(" ");

        return (
          this.computerInformation[idx2].toLowerCase() >= info.toLowerCase()
        );
      } else if (idx2 === "os") {
        let temp = this.computerInformation[idx2].split("-");
        return Number(temp[1]) >= Number(info.split(" ")[1]);
      }
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

.table {
  margin: 0;
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
