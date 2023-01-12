<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <div class="card">
          <div class="card-header">
            <h4 class="card-title">공지사항</h4>
            <!-- go list button home icon -->
            <div
              class="btn-group"
              role="group"
              aria-label="Basic example"
              v-if="mode === 'Detail'"
            >
              <button
                type="button"
                class="btn btn-secondary"
                @click="mode = 'List'"
              >
                <i class="fas fa-home"></i>
              </button>
            </div>
          </div>
          <div class="card-body listBox" v-if="mode === 'List'">
            <div class="table-responsive">
              <table class="table table-hover">
                <!-- text align center -->
                <thead class="text-primary">
                  <th>번호</th>
                  <th>제목</th>
                  <th>작성일</th>
                </thead>
                <tbody>
                  <tr
                    class="note"
                    @click="goToNoticeDetail(idx)"
                    v-for="(notice, idx) in noticeArr"
                    v-show="(pageNum - 1) * 14 <= idx && idx < pageNum * 14"
                    :key="idx"
                  >
                    <td>{{ idx + 1 }}</td>
                    <td>{{ notice.title }}</td>
                    <td>{{ notice.date }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <nav aria-label="Page navigation example">
              <ul class="pagination justify-content-center">
                <li
                  class="page-item"
                  @click="
                    if (pageNum > 4) {
                      pageNum -= 3;
                    } else {
                      pageNum = 1;
                    }
                  "
                >
                  <a class="page-link" href="#" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                    <span class="sr-only">Previous</span>
                  </a>
                </li>
                <li
                  class="page-item"
                  v-show="
                    idx2 >= 1 &&
                    idx2 <= Math.ceil(noticeArr.length / 14) &&
                    idx2 >= 1 &&
                    idx2 <= Math.ceil(noticeArr.length / 14) &&
                    pageNum - 2 <= idx2 &&
                    idx2 <= pageNum + 2
                  "
                  v-for="idx2 in Math.ceil(noticeArr.length / 14)"
                  :key="idx2"
                >
                  <a
                    class="page-link"
                    @click="pageNum = idx2"
                    :class="pageNum === idx2 ? 'active' : ''"
                    href="#"
                    >{{ idx2 }}</a
                  >
                </li>
                <li
                  class="page-item"
                  @click="
                    pageNum =
                      pageNum < Math.ceil(noticeArr.length / 14) - 4
                        ? pageNum + 3
                        : Math.ceil(noticeArr.length / 14)
                  "
                >
                  <a class="page-link" href="#" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                    <span class="sr-only">Next</span>
                  </a>
                </li>
              </ul>
            </nav>
          </div>
          <div class="card-body detailBox" v-else>
            <div class="table-responsive">
              <table class="table table-hover">
                <thead class="text-primary">
                  <th>제목</th>
                  <th>작성일</th>
                </thead>
                <tbody>
                  <tr>
                    <td>{{ detail.title }}</td>
                    <td>{{ detail.date }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="table-responsive">
              <table class="table table-hover">
                <thead class="text-primary">
                  <th>내용</th>
                </thead>
                <tbody>
                  <tr>
                    <td>
                      <textarea
                        class="form-control"
                        rows="10"
                        readonly
                        v-model="detail.content"
                      ></textarea>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MyComputer_Notice",

  data() {
    return {
      mode: "List",
      detail: {
        title: "",
        content: "",
        data: "",
      },
      pageNum: 1,
      noticeArr: [],
    };
  },

  mounted() {
    this.mode = "List";

    this.getNoticeList();
  },

  methods: {
    goToNoticeDetail(idx) {
      this.mode = "Detail";

      this.detail.title = this.noticeArr[idx].title;
      this.detail.content = this.noticeArr[idx].content;
      this.detail.date = this.noticeArr[idx].date;
    },

    getNoticeList() {
      axios
        .post("/api/getPostList")
        .then((res) => {
          this.noticeArr = res.data;
          console.log(this.noticeArr);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
.container {
  width: 100%;
  height: 100%;
}

.card {
  margin-top: 20px;
}

.card-header {
  display: flex;
  justify-content: space-between;
}

.card-body {
  padding: 0;
}

.detailBox {
  padding: 20px;
}
</style>
