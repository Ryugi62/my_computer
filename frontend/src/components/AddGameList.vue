<template>
  <div class="addGameList">
    <div class="addGameListHead">
      <div class="addGameListTitle">게임 추가</div>
    </div>
    <div class="addGameListBody">
      <!-- 게임 이름 -->
      <div class="addGameListNameInput inputBox">
        <input type="text" placeholder="게임 이름을 입력해주세요." ref="name" />
      </div>

      <!-- CPU -->
      <span class="addGameListCpuInput inputBox">
        <input
          ref="intelCpu"
          type="text"
          list="intelCpu"
          placeholder="Intel cpu를 입력해주세요."
        />
        <datalist id="intelCpu">
          <option value="i3-8100"></option>
          <option value="i5-9400"></option>
          <option value="i7-9700"></option>
          <option value="i9-9900"></option>
        </datalist>
        <input
          ref="amdCpu"
          type="text"
          list="amdCpu"
          placeholder="Amd cpu를 입력해주세요."
        />
        <datalist id="amdCpu">
          <option value="i3-8100"></option>
          <option value="i5-9400"></option>
          <option value="i7-9700"></option>
          <option value="i9-9900"></option>
        </datalist>
      </span>

      <!-- 저장 용량 -->
      <div class="addGameListDriveInput inputBox">
        <input
          ref="drive"
          type="text"
          list="driveList"
          placeholder="드라이브를 입력해주세요."
        />
        <datalist id="driveList">
          <option v-for="drive in driveArray" :value="drive" :key="drive" />
        </datalist>
      </div>

      <!-- 그래픽카드 -->
      <div class="addGameListGpuInput inputBox">
        <input
          ref="vga"
          type="text"
          list="gpuList"
          placeholder="gpu를 입력해주세요."
        />
        <datalist id="gpuList">
          <!-- option v-for vgaArray -->
          <option v-for="vga in vgaArray" :value="vga" :key="vga" />
        </datalist>
      </div>

      <!-- OS -->
      <div class="addGameListOsInput inputBox">
        <input
          ref="os"
          type="text"
          list="osList"
          placeholder="os를 입력해주세요."
        />
        <datalist id="osList">
          <option value="Windows 10"></option>
        </datalist>
      </div>

      <!-- RAM -->
      <div class="addGameListRamInput inputBox">
        <input
          ref="ram"
          type="text"
          list="ramList"
          placeholder="ram을 입력해주세요."
        />
        <datalist id="ramList">
          <option v-for="ram in ramArray" :value="ram" :key="ram" />
        </datalist>
      </div>

      <div class="addGameListSubmit inputBox" @click="clickedSubmitButton">
        <button>추가하기</button>
      </div>
    </div>
    {{ gameList }}
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AddGameList",

  data() {
    return {
      gameList: [],

      // name, cpu, drive, vga, os, ram
      name: "",

      cpuArray: [
        // intel cpu
        "Intel(R) Core(TM) i9-11900KF",
        "Intel(R) Core(TM) i9-11900T",
        "Intel(R) Core(TM) i9-11900TE",
        "Intel(R) Core(TM) i9-11900S",
        "Intel(R) Core(TM) i9-11900",
        "Intel(R) Core(TM) i9-11900K",
        "Intel(R) Core(TM) i9-11900F",
        "Intel(R) Core(TM) i9-11900T",
        "Intel(R) Core(TM) i9-11900TE",
        "Intel(R) Core(TM) i9-11900S",
        "Intel(R) Core(TM) i7-11700KF",
        "Intel(R) Core(TM) i7-11700T",
        "Intel(R) Core(TM) i7-11700TE",
        "Intel(R) Core(TM) i7-11700S",
        "Intel(R) Core(TM) i7-11700",
        "Intel(R) Core(TM) i7-11700K",
        "Intel(R) Core(TM) i7-11700F",
        "Intel(R) Core(TM) i5-11600KF",
        "Intel(R) Core(TM) i5-11600T",
        "Intel(R) Core(TM) i5-11600TE",
        "Intel(R) Core(TM) i5-11600S",
        "Intel(R) Core(TM) i5-11600",
        "Intel(R) Core(TM) i5-11600K",
        "Intel(R) Core(TM) i5-11600F",
        "Intel(R) Core(TM) i3-11100T",
        "Intel(R) Core(TM) i3-11100TE",
        "Intel(R) Core(TM) i3-11100S",
        "Intel(R) Core(TM) i3-11100",
        "Intel(R) Core(TM) i3-11100F",
        "Intel(R) Core(TM) i9-10900KF",
        "Intel(R) Core(TM) i9-10900T",
        "Intel(R) Core(TM) i9-10900TE",
        "Intel(R) Core(TM) i9-10900S",
        "Intel(R) Core(TM) i9-10900",
        "Intel(R) Core(TM) i9-10900K",
        "Intel(R) Core(TM) i9-10900F",
        "Intel(R) Core(TM) i7-10700KF",
        "Intel(R) Core(TM) i7-10700T",
        "Intel(R) Core(TM) i7-10700TE",
        "Intel(R) Core(TM) i7-10700S",
        "Intel(R) Core(TM) i7-10700",
        "Intel(R) Core(TM) i7-10700K",
        "Intel(R) Core(TM) i7-10700F",
        "Intel(R) Core(TM) i5-10600KF",
        "Intel(R) Core(TM) i5-10600T",
        "Intel(R) Core(TM) i5-10600TE",
        "Intel(R) Core(TM) i5-10600S",
        "Intel(R) Core(TM) i5-10600",
        "Intel(R) Core(TM) i5-10600K",
        "Intel(R) Core(TM) i5-10600F",
        "Intel(R) Core(TM) i3-10100T",
        "Intel(R) Core(TM) i3-10100TE",
        "Intel(R) Core(TM) i3-10100S",
        "Intel(R) Core(TM) i3-10100",
        "Intel(R) Core(TM) i3-10100F",
        "Intel(R) Core(TM) i9-10900KF",
        "Intel(R) Xeon(R) Gold 6248",
        "Intel(R) Xeon(R) Gold 6248R",
        "Intel(R) Xeon(R) Gold 6248Y",
        "Intel(R) Xeon(R) Gold 6248C",
        "Intel(R) Xeon(R) Gold 6248U",
        "Intel(R) Xeon(R) Gold 6248M",
        "Intel(R) Xeon(R) Gold 6248P",
        "Intel(R) Xeon(R) Gold 6248L",
        "Intel(R) Xeon(R) Gold 6248V",
        "Intel(R) Xeon(R) Gold 6248W",
        "Intel(R) Xeon(R) Platinum 8260",
        "Intel(R) Xeon(R) Platinum 8260L",
        "Intel(R) Xeon(R) Platinum 8260M",
        "Intel(R) Xeon(R) Platinum 8260Y",
        "Intel(R) Xeon(R) Platinum 8260C",
        "Intel(R) Xeon(R) Platinum 8260U",
        "Intel(R) Xeon(R) Platinum 8260P",
        "Intel(R) Xeon(R) Platinum 8260V",
        "Intel(R) Xeon(R) Platinum 8260W",
        "Intel(R) Xeon(R) Platinum 8270",
        "Intel(R) Xeon(R) Platinum 8270L",
        "Intel(R) Xeon(R) Platinum 8270M",
        "Intel(R) Xeon(R) Platinum 8270Y",
        "Intel(R) Xeon(R) Platinum 8270C",
        "Intel(R) Xeon(R) Platinum 8270U",
        "Intel(R) Xeon(R) Platinum 8270P",
        "Intel(R) Xeon(R) Platinum 8270V",
        "Intel(R) Xeon(R) Platinum 8270W",

        // amd cpu full name
        "AMD Ryzen 9 5950X",
        "AMD Ryzen 9 5900X",
        "AMD Ryzen 7 5800X",
        "AMD Ryzen 5 5600X",
        "AMD Ryzen 9 5900",
        "AMD Ryzen 7 5800G",
        "AMD Ryzen 7 5700X",
        "AMD Ryzen 5 5600",
        "AMD Ryzen 9 3950X",
        "AMD Ryzen 9 3900X",
        "AMD Ryzen 7 3800X",
        "AMD Ryzen 7 3700X",
        "AMD Ryzen 7 3700",
        "AMD Ryzen 5 3600X",
        "AMD Ryzen 5 3600",
        "AMD Ryzen 5 3500X",
        "AMD Ryzen 3 3300X",
        "AMD Ryzen 3 3100",
        "AMD Ryzen Threadripper 3970X",
        "AMD Ryzen Threadripper 3960X",
        "AMD Ryzen Threadripper 3960",
        "AMD Ryzen Threadripper 3950X",
        "AMD Ryzen Threadripper 3940X",
        "AMD Ryzen Threadripper 2970WX",
        "AMD Ryzen Threadripper 2950X",
        "AMD Ryzen Threadripper 2920X",
        "AMD Ryzen Threadripper 2970X",
      ],

      driveArray: [
        "8 GB",
        "16 GB",
        "32 GB",
        "64 GB",
        "128 GB",
        "256 GB",
        "512 GB",
        "1 TB",
        "2 TB",
        "4 TB",
        "8 TB",
        "16 TB",
        "32 TB",
        "64 TB",
      ],

      vgaArray: [
        "GeForce RTX 3090",
        "GeForce RTX 3080",
        "GeForce RTX 3070",
        "GeForce RTX 3060 Ti",
        "GeForce RTX 3060",
        "GeForce RTX 3050 Ti",
        "GeForce RTX 3050",
        "GeForce RTX 3040",
        "GeForce GTX 1660 Ti",
        "GeForce GTX 1660 Super",
        "GeForce GTX 1660",
        "GeForce GTX 1650 Super",
        "GeForce GTX 1650",
        "GeForce GTX 1080 Ti",
        "GeForce GTX 1080",
        "GeForce GTX 1070 Ti",
        "GeForce GTX 1070",
        "GeForce GTX 1060",
        "GeForce GTX 1050 Ti",
        "GeForce GTX 1050",
        "GeForce GTX 980 Ti",
        "GeForce GTX 980",
        "GeForce GTX 970",
        "GeForce GTX 960",
        "GeForce GTX 950",
        "GeForce GTX Titan X",
        "GeForce GTX Titan",
        "GeForce GTX 780 Ti",
        "GeForce GTX 780",
        "GeForce GTX 770",
        "GeForce GTX 760",
        "GeForce GTX 750 Ti",
        "GeForce GTX 750",
        "GeForce GTX 745",
        "GeForce GT 740",
        "GeForce GT 730",
        "GeForce GT 720",
        "GeForce GT 710",
        "GeForce GT 705",
        "GeForce GT 703",
        "GeForce GT 640",
        "GeForce GT 630",
        "GeForce GT 620",
        "GeForce GT 610",
        "GeForce 605",
        "GeForce GT 520",
        "GeForce GT 510",
        "GeForce GT 240",
        "GeForce GT 220",
        "GeForce GTS 450",
        "GeForce GTS 240",
        "GeForce GTS 150",
        "GeForce GTS 140",
        "GeForce GTS 130",
        "GeForce GT 130",
        "GeForce GT 120",
        "GeForce G100",

        "Intel(R) Iris Xe Max",
        "Intel(R) Iris Xe",
        "Intel(R) Iris Pro 580",
        "Intel(R) Iris Plus 655",
        "Intel(R) Iris Plus 650",
        "Intel(R) Iris Plus 640",
        "Intel(R) Iris Plus 645",
        "Intel(R) Iris Pro 6200",
        "Intel(R) HD P630",
        "Intel(R) HD P620",
        "Intel(R) HD P610",
        "Intel(R) HD P600",
        "Intel(R) HD P580",
        "Intel(R) HD P570",
        "Intel(R) HD P555",
        "Intel(R) HD P530",
        "Intel(R) HD P520",
        "Intel(R) HD P515",
        "Intel(R) HD P510",
        "Intel(R) HD P500",
        "Intel(R) HD P490",
        "Intel(R) HD P470",
        "Intel(R) HD P4600/4600",
        "Intel(R) HD P4500/4500",
        "Intel(R) HD P4400/4400",
        "Intel(R) HD Graphics",
        "Intel(R) HD Graphics P4600/4600",
        "Intel(R) HD Graphics P4500/4500",
        "Intel(R) HD Graphics P4400/4400",
        "Intel(R) HD Graphics P4000",
        "Intel(R) HD Graphics P4600/4600",
        "Intel(R) HD Graphics P4500/4500",
        "Intel(R) HD Graphics P4400/4400",
        "Intel(R) HD Graphics P4000",
        "Intel(R) HD Graphics P630",
        "Intel(R) HD Graphics P620",
        "Intel(R) HD Graphics P610",
        "Intel(R) HD Graphics P600",

        "AMD Radeon RX 6800 XT",
        "AMD Radeon RX 6800",
        "AMD Radeon RX 6700 XT",
        "AMD Radeon RX 6700",
        "AMD Radeon RX 6600 XT",
        "AMD Radeon RX 6600",
        "AMD Radeon RX 6900 XT",
        "AMD Radeon RX 6900",
        "AMD Radeon RX 6800 XT",
        "AMD Radeon RX 6800",
        "AMD Radeon RX 6700 XT",
        "AMD Radeon RX 6700",
        "AMD Radeon RX 6600 XT",
        "AMD Radeon RX 6600",
        "AMD Radeon RX 5700 XT",
        "AMD Radeon RX 5700",
        "AMD Radeon RX 5600 XT",
        "AMD Radeon RX 5600",
        "AMD Radeon RX 5500 XT",
        "AMD Radeon RX 5500",
        "AMD Radeon RX 550",
        "AMD Radeon R9 Fury X",
        "AMD Radeon R9 Fury",
        "AMD Radeon R9 Nano",
        "AMD Radeon R9 390X",
        "AMD Radeon R9 390",
        "AMD Radeon R9 380X",
        "AMD Radeon R9 380",
        "AMD Radeon R9 370X",
        "AMD Radeon R9 370",
        "AMD Radeon R9 360",
        "AMD Radeon R7 360",
        "AMD Radeon R7 350",
        "AMD Radeon R7 340",
      ],

      osArray: [
        "Windows 10",
        "Windows 8.1",
        "Windows 8",
        "Windows 7",
        "Windows Vista",
        "Windows XP",
      ],

      ramArray: [
        "4 GB",
        "6 GB",
        "8 GB",
        "16 GB",
        "32 GB",
        "64 GB",
        "128 GB",
        "256 GB",
        "512 GB",
        "1 TB",
        "2 TB",
        "4 TB",
        "8 TB",
        "16 TB",
        "32 TB",
        "64 TB",
      ],
    };
  },

  mounted() {
    this.updateGameList();
  },

  methods: {
    updateGameList() {
      axios
        .post("/api/getGameList")
        .then((response) => {
          this.gameList = new Array().concat(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    clickedSubmitButton() {
      // get input values
      const gameName = this.$refs.name.value;
      const intelCpu = this.$refs.intelCpu.value;
      const amdCpu = this.$refs.amdCpu.value;
      const drive = this.$refs.drive.value;
      const vga = this.$refs.vga.value;
      const os = this.$refs.os.value;
      const ram = this.$refs.ram.value;

      // check if input values are empty
      if (
        gameName === "" ||
        (intelCpu === "" && amdCpu === "") ||
        drive === "" ||
        vga === "" ||
        os === "" ||
        ram === ""
      ) {
        alert("Please fill out all fields");
        return;
      }

      // add game to database
      axios
        .post("/api/setGameList", {
          name: gameName,
          cpu: {
            intel: intelCpu,
            amd: amdCpu,
          },
          drive: drive,
          vga: vga,
          os: os,
          ram: ram,
        })
        .then((response) => {
          // if successful, update game list
          if (response.data === "success") {
            this.updateGameList();

            // clear input fields
            this.$refs.name.value = "";
            this.$refs.intelCpu.value = "";
            this.$refs.amdCpu.value = "";
            this.$refs.drive.value = "";
            this.$refs.vga.value = "";
            this.$refs.os.value = "";
            this.$refs.ram.value = "";
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
.addGameList {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.inputBox {
  width: fit-content;
  margin: auto;
}
</style>
