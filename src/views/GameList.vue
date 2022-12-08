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
          <tr v-for="idx1 in gameInformationArr.length" :key="idx1 - 1">
            <td
              v-for="(gameInformation, idx2) of gameInformationArr[idx1 - 1]"
              :key="idx2"
            >
              <i v-if="idx1 - 1" class="fa-solid fa-check okCheck"></i>
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
export default {
  data() {
    return {
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
          game: "리그오브레전드",
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
};
</script>

<style scoped>
.gameListBackground {
  width: 100%;
  height: 100%;
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
