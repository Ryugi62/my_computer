<template>
  <div>
    <div class="writePost">
      <div class="writePostHead">
        <div class="writePostTitle">공지사항 작성</div>
      </div>
      <div class="writePostBody">
        <div class="writePostTitleInput">
          <input type="text" placeholder="제목을 입력해주세요." />
        </div>
        <div class="writePostContentInput">
          <textarea
            name="content"
            id="content"
            cols="30"
            rows="10"
            placeholder="내용을 입력해주세요."
          ></textarea>
        </div>
        <div class="writePostSubmit">
          <button>작성하기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
