<template>
  <div class="postListBox">
    <div class="listHead">공지사항</div>
    <div class="listBody">
      <!-- post -->
      <div class="postBox" v-if="postMode === 'List'">
        <div class="post" v-for="(post, idx) in postList" :key="idx">
          <div class="postListIdx">{{ idx }}</div>
          <div class="postListTitle" @click="showPostDetail(idx)">
            {{ post.title }}
          </div>
          <div class="postListEdit" @click="clickedEditButon(idx)">
            <i class="fas fa-edit"></i>
          </div>
          <div class="postListDelete" @click="clickedDeleteButon(idx)">
            <i class="fas fa-trash-alt"></i>
          </div>
        </div>
      </div>
      <div class="writeFormBox" v-else>
        <div class="formTitle">
          <input type="text" placeholder="제목을 입력하세요" v-model="title" />
        </div>
        <div class="formContent">
          <textarea
            name="content"
            id="content"
            cols="30"
            rows="10"
            placeholder="내용을 입력하세요"
            v-model="content"
          ></textarea>
        </div>
        <div class="formButton">
          <button @click="clickedSubmitButton">등록</button>
        </div>
      </div>
    </div>
    <div class="listFooter">
      <!-- add post button -->
      <div class="addPostButton">
        <button @click="clickedWriteButton()">글쓰기</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "WritePost",
  data() {
    return {
      postList: [],
      postMode: "List",
      nowIdx: 0,
      content: "",
      title: "",
    };
  },

  mounted() {
    this.getPostList();
  },

  methods: {
    getPostList() {
      axios
        .post("/api/getPostList")
        .then((res) => {
          this.postList = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    showPostDetail() {
      console.log("showPostDetail");
    },

    clickedEditButon(idx) {
      this.changeMode("Edit");

      this.nowIdx = idx;

      const { title, content } = this.postList[idx];

      this.title = title;
      this.content = content;
    },

    clickedDeleteButon(idx) {
      const isDelete = confirm("정말 삭제하시겠습니까?");
      if (!isDelete) {
        return;
      }

      const id = this.postList[idx].id;

      axios
        .post("/api/deletePost", {
          id,
        })
        .then((res) => {
          if (res.data === "success") {
            alert("글이 삭제되었습니다");
          } else {
            alert("글 삭제에 실패했습니다");
          }
        })
        .catch((err) => {
          console.log(err);
        });

      this.postList.splice(idx, 1);
    },

    clickedWriteButton() {
      const mode = this.postMode === "List" ? "Write" : "List";

      this.changeMode(mode);
    },

    changeMode(mode) {
      this.postMode = mode;

      if (mode === "List") {
        const titleInput = document.querySelector(".formTitle input");
        const contentInput = document.querySelector(".formContent textarea");

        titleInput.value = "";
        contentInput.value = "";
      }

      // change addPostButton text
      const addPostButton = document.querySelector(".addPostButton button");
      addPostButton.innerText = mode === "List" ? "글쓰기" : "취소";
    },

    clickedSubmitButton() {
      const title = this.title;
      const content = this.content;

      console.log(title, content);

      if (title === "" || content === "") {
        alert("제목과 내용을 입력해주세요");
        return;
      }

      if (this.postMode === "Edit") {
        this.requestEdit(title, content);
        return;
      }

      axios
        .post("/api/writePost", {
          title,
          content,
        })
        .then((res) => {
          if (res.data === "success") {
            alert("글이 등록되었습니다");
          } else {
            alert("글 등록에 실패했습니다");
          }
        })
        .catch((err) => {
          console.log(err);
        });

      this.changeMode("List");
    },

    requestEdit(title, content) {
      const id = this.postList[this.nowIdx].id;

      axios
        .post("/api/editPost", {
          id,
          title,
          content,
          date: new Date().toLocaleString(),
        })
        .then((res) => {
          console.log("res", res);
          if (res.data === "success") {
            alert("글이 수정되었습니다");

            this.postList[this.nowIdx].title = title;
            this.postList[this.nowIdx].content = content;
          } else {
            alert("글 수정에 실패했습니다");
          }
        })
        .catch((err) => {
          console.log(err);
        });

      this.changeMode("List");
    },

    requestAddPost(title, content) {
      axios
        .post("/api/writePost", {
          title,
          content,
        })
        .then((res) => {
          if (res.data === "success") {
            alert("글이 등록되었습니다");
          } else {
            alert("글 등록에 실패했습니다");
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },

  watch: {
    postMode() {
      if (this.postMode === "List") {
        this.getPostList();
      }
    },
  },
};
</script>

<style>
.postListBox {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.listHead {
  width: 100%;
  height: 50px;
  border-radius: 10px 10px 0 0;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
}

.listBody {
  width: 100%;
  height: calc(100% - 100px);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.postBox {
  width: 80%;
  height: 100%;
  border: 1px solid white;
  overflow-y: scroll;
}

.listFooter {
  width: 100%;
  height: 50px;
  border-radius: 0 0 10px 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
}

.post {
  width: 100%;
  height: 50px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid white;
}
.post:hover {
  background: #1f3964;
}

.postListIdx {
  width: 10%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.postListTitle {
  width: 60%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.postListEdit {
  width: 10%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.postListEdit:hover {
  color: greenyellow;
}

.postListDelete {
  width: 10%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.postListDelete:hover {
  color: red;
}

.writeFormBox {
  width: 80%;
  height: 100%;
  border: 1px solid white;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.formTitle {
  width: 100%;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.formTitle input {
  width: 80%;
  height: 80%;
  border: none;
  border-radius: 10px;
  padding: 0 10px;
  outline: none;
}

.formContent {
  width: 100%;
  height: calc(100% - 100px);
  display: flex;
  justify-content: center;
  align-items: center;
}

.formContent textarea {
  width: 80%;
  height: 80%;
  border: none;
  border-radius: 10px;
  padding: 10px;
  outline: none;
}

.formButton {
  width: 100%;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.formButton button {
  width: 80%;
  height: 80%;
  border: none;
  border-radius: 10px;
  background: #1f3964;
  color: white;
  cursor: pointer;
}

.addPostButton {
  width: 80%;
  height: 80%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.addPostButton button {
  width: 100%;
  height: 100%;
  border: none;
  border-radius: 10px;
  background: #1f3964;
  color: white;
  cursor: pointer;
}
</style>
