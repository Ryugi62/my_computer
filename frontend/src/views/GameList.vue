<template>
  <div class="gameListBackground">
    <div class="myPerformanceBox">
      <div class="myPerformanceTitle">내 PC 사양</div>
      <div class="myPerformanceContent">
        <div class="myPerformanceContentTitle">운영체제 : {{ os }}</div>
      </div>
      <div class="myPerformanceContent">
        <div class="myPerformanceContentTitle">CPU : {{ cpu }}</div>
      </div>
      <div class="myPerformanceContent">
        <div class="myPerformanceContentTitle">RAM : {{ ram }}</div>
      </div>
      <div class="myPerformanceContent">
        <div class="myPerformanceContentTitle">
          그래픽카드 : {{ graphic_card }}
        </div>
      </div>
      <div class="myPerformanceContent">
        <div class="myPerformanceContentTitle">바이오스 버전 : {{ bios }}</div>
      </div>
      <div class="myPerformanceContent">
        <div class="myPerformanceContentTitle">
          메인보드 제조사 : {{ mainboard_manufacturer }}
        </div>
      </div>
      <div class="myPerformanceContent">
        <div class="myPerformanceContentTitle">
          드라이브 용량 : {{ drive_capacity }}
        </div>
      </div>
    </div>
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
      bios: "",
      cpu: "",
      drive_capacity: "",
      graphic_card: "",
      mainboard_manufacturer: "",
      os: "",
      ram: "",

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
    this.setComputerData();
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
        this.getComputerInfo();
      } else {
        this.bios = cookieObj.bios;
        this.cpu = cookieObj.cpu;
        this.drive_capacity = cookieObj.drive_capacity;
        this.graphic_card = cookieObj.graphic_card;
        this.mainboard_manufacturer = cookieObj.mainboard_manufacturer;
        this.os = cookieObj.os;
        this.ram = cookieObj.ram;
      }
    },

    getComputerInfo() {
      axios
        .post("http://127.0.0.1:10000/get_info", {
          headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
          },
        })
        .then((response) => {
          console.log(response.data);
          // set cookie
          document.cookie = `bios=${response.data.bios}`;
          document.cookie = `cpu=${response.data.cpu}`;
          document.cookie = `drive_capacity=${response.data.drive_capacity}`;
          document.cookie = `graphic_card=${response.data.graphic_card}`;
          document.cookie = `mainboard_manufacturer=${response.data.mainboard_manufacturer}`;
          document.cookie = `os=${response.data.os}`;
          document.cookie = `ram=${response.data.ram}`;

          this.bios = response.data.bios;
          this.cpu = response.data.cpu;
          this.drive_capacity = response.data.drive_capacity;
          this.graphic_card = response.data.graphic_card;
          this.mainboard_manufacturer = response.data.mainboard_manufacturer;
          this.os = response.data.os;
          this.ram = response.data.ram;
        })
        .catch((err) => {
          console.log(err);
          this.$router.push("/home");
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
