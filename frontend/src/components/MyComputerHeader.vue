<template>
  <div class="headerBackground">
    <div class="title" @click="goHome">내 컴퓨터.com</div>
    <div class="navBarBox">
      <div class="navBar">
        <span class="navBarIcon" @click="goNotice">공지사항</span>
        <span class="navBarIcon" @click="goInquiry">제작자에게 문의</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    goHome() {
      this.$router.push("/");
    },
    goNotice() {
      this.$router.push("/notice");
    },
    goInquiry() {
      window.open("https://www.facebook.com/profile.php?id=100088261527037");
    },
  },
};
</script>

<style scoped>
.headerBackground {
  color: white;
  width: 100%;
  height: 50px;
  display: flex;
  background-color: #1f3964;
}

.title {
  cursor: pointer;
  padding: 0 15px;
  font-size: 20px;
  align-self: center;
}

.navBarBox {
  min-width: 25%;
  display: flex;
  margin-left: auto;
}

.navBar {
  margin: auto;
  width: 100%;
  display: flex;
  align-items: center;
}

.navBarIcon {
  margin: auto;
  cursor: pointer;
  padding: 0 20px;
}
</style>
