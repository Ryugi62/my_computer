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
            <td v-for="(info, idx2) in gameInformation" :key="idx2">
              <span v-if="idx2 === 'game'">{{ info }}</span>
              <i v-else-if="idx2" class="fa-solid fa-check okCheck"></i>
              <i v-else class="fa-solid fa-x notCheck"></i>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="shareButtonBox">
      <button type="button" class="shareButton btn btn-primary">
        내 PC 사양 공유하기
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
        bios: "X",
        cpu: "X",
        drive_capacity: "X",
        graphic_card: "X",
        mainboard_manufacturer: "X",
        os: "X",
        ram: "X",
      },

      theadTitleArr: [
        "게임",
        "운영체제",
        "CPU",
        "RAM",
        "그래픽카드",
        "바이오스 버전",
        "메인보드 제조사",
        "드라이브 용량",
      ],

      gameInformationArr: [
        {
          game: "리그오브레전드",
          os: "Windows 10",
          cpu: "Inter 9th Gen",
          ram: "16GB",
          grapichCard: "GTX 1660",
          biosVersion: "1.0.0",
          mainboardManufacturer: "MSI", // Mainboard manufacturer
          driveCapacity: "500GB", //
        },
        {
          game: "배틀그라운드",
          os: "Windows 10",
          cpu: "Inter 9th Gen",
          ram: "16GB",
          grapichCard: "GTX 1660",
          biosVersion: "1.0.0",
          mainboardManufacturer: "MSI", // Mainboard manufacturer
          driveCapacity: "500GB", //
        },
        {
          game: "크레이지아케이드",
          os: "Windows 10",
          cpu: "Inter 9th Gen",
          ram: "16GB",
          grapichCard: "GTX 1660",
          biosVersion: "1.0.0",
          mainboardManufacturer: "MSI", // Mainboard manufacturer
          driveCapacity: "500GB", //
        },
        {
          game: "카트라이더",
          os: "Windows 10",
          cpu: "Inter 9th Gen",
          ram: "16GB",
          grapichCard: "GTX 1660",
          biosVersion: "1.0.0",
          mainboardManufacturer: "MSI", // Mainboard manufacturer
          driveCapacity: "500GB", //
        },
      ],
    };
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
        cookieObj.bios === "" ||
        cookieObj.cpu === "" ||
        cookieObj.drive_capacity === "" ||
        cookieObj.graphic_card === undefined ||
        cookieObj.mainboard_manufacturer === "" ||
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
      const {
        bios,
        cpu,
        drive_capacity,
        graphic_card,
        mainboard_manufacturer,
        os,
        ram,
      } = data;

      this.computerInformation.bios = bios;
      this.computerInformation.cpu = cpu;
      this.computerInformation.drive_capacity = drive_capacity;
      this.computerInformation.graphic_card = graphic_card;
      this.computerInformation.mainboard_manufacturer = mainboard_manufacturer;
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
          document.cookie = `bios=${response.data[0].bios}`;
          document.cookie = `cpu=${response.data[0].cpu}`;
          document.cookie = `drive_capacity=${response.data[0].drive_capacity}`;
          document.cookie = `graphic_card=${response.data[0].graphic_card}`;
          document.cookie = `mainboard_manufacturer=${response.data[0].mainboard_manufacturer}`;
          document.cookie = `os=${response.data[0].os}`;
          document.cookie = `ram=${response.data[0].ram}`;

          this.setComputerInfo(response.data[0]);
        })
        .catch((err) => {
          console.log(err);
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
