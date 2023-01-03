<template>
  <div class="myHardwareBackground">
    <div class="hardwareTableBox">
      <table class="table">
        <thead>
          <tr>
            <th
              scope="col"
              v-for="(theadTitle, idx) of computerInformation"
              :key="idx"
            >
              {{ idx }}
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
        <button class="btn btn-primary shareButton">내 PC사양 공유하기</button>
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
        bios: "X",
        cpu: "X",
        drive_capacity: "X",
        graphic_card: "X",
        mainboard_manufacturer: "X",
        os: "X",
        ram: "X",
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
.myHardwareBackground {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  text-align: center;
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
