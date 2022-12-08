<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <div class="card">
          <div class="card-header">
            <h4 class="card-title">공지사항</h4>
          </div>
          <div class="card-body">
            <div class="table-responsive">
              <table class="table table-hover">
                <thead class="text-primary">
                  <th>번호</th>
                  <th>제목</th>
                  <th>작성자</th>
                  <th>작성일</th>
                  <th>조회수</th>
                </thead>
                <tbody>
                  <tr
                    class="note"
                    @click="goToNoticeDetail"
                    v-for="(notice, idx) in noticeArr"
                    v-show="(pageNum - 1) * 14 <= idx && idx < pageNum * 14"
                    :key="idx"
                  >
                    <td>{{ idx + 1 }}</td>
                    <td>{{ notice.title }}</td>
                    <td>{{ notice.writer }}</td>
                    <td>{{ notice.date }}</td>
                    <td>{{ notice.view }}</td>
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
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MyComputer_Notice",

  mounted() {},

  data() {
    return {
      pageNum: 1,
      noticeArr: [
        {
          title: "공지사항입니다",
          writer: "관리자",
          date: "2021-01-01",
          view: 0,
        },
      ],
    };
  },

  methods: {
    goToNoticeDetail() {
      this.$router.push("/noticeDetail");
    },
  },
};
</script>

<style>
.card-body {
  text-align: center;
}

.note {
  cursor: pointer;
}
</style>
