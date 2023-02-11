<template>
  <div
    class="share-box"
    :style="{ display: share ? 'block' : 'none' }"
    @click.stop
  >
    <div class="share-over">
      <h3 class="share-title">공유하기</h3>
    </div>
    <div class="share-under">
      <!-- font awesome facebook color   -->
      <i
        class="fab fa-facebook-square fa-2x"
        style="color: #3b5998"
        @click="clicked_share('facebook')"
      ></i>
      <!-- font awesome twitter color skyblue-->
      <i
        class="fab fa-twitter-square fa-2x"
        style="color: #00acee"
        @click="clicked_share('twitter')"
      ></i>
      <!-- font awesome kakao-talk color yellow -->
      <i
        class="fas fa-comment-dots fa-2x"
        style="color: #ffeb00"
        @click="clicked_share('kakao')"
      ></i>
      <!-- font awesome url -->
      <i class="fas fa-link fa-2x" @click="clicked_share('url')"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: "MyHardware",

  props: {
    share: {
      type: Boolean,
      default: false,
    },

    computerInformation: {
      type: Object,
      default: () => {},
    },
  },

  methods: {
    clicked_share(type) {
      const url = "http://내컴퓨터.com/myhardware";
      const coment = `내 PC사양은 :
  CPU: ${this.computerInformation.cpu},
  메인보드: ${this.computerInformation.mainboard},
  외장 GPU: ${this.computerInformation.external_vga},
  내장 GPU: ${this.computerInformation.internal_vga},
  RAM: ${this.computerInformation.ram},
  저장: ${this.computerInformation.drive},
  OS: ${this.computerInformation.os} 입니다.\n\n`;

      if (type === "kakao") {
        window.Kakao.Share.sendDefault({
          objectType: "text",
          text: coment,
          link: {
            mobileWebUrl: "https://developers.kakao.com",
            webUrl: "https://developers.kakao.com",
          },
        });
      } else if (type === "twitter") {
        window.open(
          "https://twitter.com/share?url=" +
            encodeURIComponent(url) +
            "&text=" +
            encodeURIComponent(coment),
          "_blank"
        );
      } else if (type === "facebook") {
        const postTitle = "My Awesome Post";
        const postText = "This is the text of my awesome post.";
        const facebookShareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(
          url
        )}&t=${encodeURIComponent(postTitle)}&description=${encodeURIComponent(
          postText
        )}`;

        window.open(
          facebookShareUrl,
          "facebook-share-dialog",
          "width=800,height=600"
        );
      } else {
        const dummy = document.createElement("input");
        document.body.appendChild(dummy);
        dummy.value = url;
        dummy.select();
        document.execCommand("copy");
        document.body.removeChild(dummy);
        alert("URL이 복사되었습니다.");
      }
    },
  },

  watch: {
    share: function (newVal) {
      this.$el.style.display = newVal ? "block" : "none";
    },
  },
};
</script>

<style scoped>
* {
  /* border: 1px solid red; */
}

.share-box {
  z-index: 101;
  left: -50%;
  width: 280px;
  bottom: calc(100% + 10px);
  height: 100px;
  border: 1px solid #000;
  display: flex;
  position: absolute;
  background: #fff;
  flex-direction: column;
}

.share-title {
  margin: 5px 0;
  font-weight: bold;
  font-family: "Noto Sans KR", sans-serif;
}

.share-under {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
}
.share-under > i {
  margin: 0 10px;
  cursor: pointer;
}
</style>
