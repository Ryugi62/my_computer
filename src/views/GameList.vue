<template>
  <div class="gameListBackground">
    <table class="table">
      <thead>
        <tr>
          <th v-for="(theadTitle, idx) of theadTitleArr" scope="col" :key="idx">
            {{ theadTitle }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(inf, idx) of gameInformationArr" :key="inf + idx">
          <th scope="row">{{ inf.game }}</th>
          <td>{{ inf.os }}</td>
          <td>{{ inf.cpu }}</td>
          <td>{{ inf.ram }}</td>
          <td>{{ inf.grapichCard }}</td>
          <td>{{ inf.mainboardManufacturer }}</td>
          <td>{{ inf.driveCapacity }}</td>
        </tr>
      </tbody>
    </table>
    <div class="shareButtonBox">
      <!-- share button -->
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
      // 게임 정보가 운영체제, CPU, RAM, GRAPHIC CARD, 바이오스 버전, 메인보드 제조사, 드라이브 용량 저장 to array

      // 게임 정보를 테이블로 출력
      theadTitleArr: [
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
}

.table {
  width: 100%;
  margin: 0;
  height: 90%;
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
