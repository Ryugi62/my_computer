<template>
  <div class="adminBackground">
    <div class="adminBox">
      <div class="boxHead">
        <div class="goRoutButton">
          <router-link to="/">
            <!-- fontawsome 집 아이콘 -->
            <i class="fas fa-home goHome"></i>
          </router-link>
        </div>
        <h3>관리자 페이지</h3>
      </div>
      <div class="boxBody">
        <div v-if="isAdmin()" class="tagBox">
          <div class="tagHead tagGroup">
            <div
              class="goWritePostTag tag"
              :class="{ online: onlineTag === 'writePost' }"
              @click="onlineTag = 'writePost'"
            >
              공지사항 작성
            </div>
            <div
              class="goAddGameListTag tag"
              :class="{ online: onlineTag === 'addGameList' }"
              @click="onlineTag = 'addGameList'"
            >
              게임 추가
            </div>
          </div>
          <div class="tagBody">
            <WritePost v-if="onlineTag === 'writePost'" />
            <AddGameList v-if="onlineTag === 'addGameList'" />
          </div>
        </div>
        <div v-else>
          <h1 class="noAdmin">관리자만 접근 가능합니다.</h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import WritePost from "../components/WritePost.vue";
import AddGameList from "../components/AddGameList.vue";

export default {
  name: "MyComputer_Admin",

  components: {
    WritePost,
    AddGameList,
  },

  data() {
    return {
      onlineTag: "writePost",
    };
  },

  mounted() {
    if (!this.isAdmin()) {
      this.$router.push("/adminLogin");
    }
  },

  methods: {
    isAdmin() {
      if (this.$store.state.isAdmin) {
        return true;
      } else {
        return false;
      }
    },
  },
};
</script>

<style scoped>
* {
  /* border: 1px solid white; */
}

.adminBackground {
  top: 0;
  left: 0;
  width: 100vw;
  color: white;
  height: 100vh;
  z-index: 10;
  position: fixed;
  background: #1f3964;
}

.adminBox {
  width: 100%;
  height: 100%;
  border-radius: 10px;
}

.boxHead {
  width: 100%;
  height: 50px;
  border-radius: 10px 10px 0 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.goRoutButton {
  position: absolute;
  left: 10px;
  top: 10px;
}

.goHome {
  color: white;
  font-size: 30px;
}

.boxBody {
  width: 100%;
  height: calc(100% - 50px);
  border-radius: 0 0 10px 10px;
}

.tagBox {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.tagHead {
  width: 100%;
  height: 50px;
  border-radius: 10px 10px 0 0;
  display: flex;
  justify-content: left;
  align-items: left;
}

.tag {
  padding: 0 10px;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  cursor: pointer;
}
.tag:hover,
.online {
  background: #071833;
}

.tagBody {
  width: 100%;
  height: 100%;
  border-radius: 0 0 10px 10px;
  background: #071833;
}
</style>
