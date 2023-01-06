<template>
  <div class="adminLoginBackground">
    <div class="loginForm">
      <h3 for="loginTitle">관리자 로그인</h3>
      <input type="text" class="idInput" placeholder="아이디를 입력하세요" />
      <br />
      <input
        type="password"
        class="passwordInput"
        placeholder="비밀번호를 입력하세요"
      />
      <br />
      <button class="loginButton" @click="login">로그인</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "MyComputer_AdminLogin",

  data() {
    return {
      loginCode: "",
    };
  },

  methods: {
    login() {
      axios
        .post("/api/login", {
          headers: {
            "Content-Type": "application/json",
          },
          json: {
            id: this.$el.querySelector(".idInput").value,
            password: this.$el.querySelector(".passwordInput").value,
          },
        })
        .then((response) => {
          if (response.data === "success") {
            this.$store.commit("setAdmin", true);
            this.$router.push("/admin");
          } else {
            alert("로그인에 실패하였습니다.");
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
.adminLoginBackground {
  top: 0;
  left: 0;
  width: 100vw;
  color: white;
  height: 100vh;
  z-index: 10;
  position: fixed;
  background: #1f3964;
  display: flex;
}

.loginForm {
  width: 40%;
  height: 30%;
  margin: auto;
  display: flex;
  background: #426097;
  border-radius: 10px;
  flex-direction: column;
}

.loginCodeForm * {
  margin: auto;
}
</style>
