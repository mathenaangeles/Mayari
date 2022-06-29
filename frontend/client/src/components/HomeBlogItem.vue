<template>
  <b-card
    class="article-card mb-4"
    :img-src="article.preview_image"
    :img-alt="article.title"
    img-left
    img-height="100%"
    img-width="30%"
  >
    <router-link :to="`article/${article.id}`">
      <div class="article-category-text">
        {{ article.category }}
      </div>
      <div class="article-title-text">{{ article.title }}</div>
      <div>{{ article.preview }}</div>
      <div class="article-subtext">
        {{ article.author }} | {{ article.updated_at | dateOnly }}
      </div>
    </router-link>
  </b-card>
</template>
<style scoped>
a,
a:hover {
  color: inherit;
  text-decoration: none;
}
.article-card {
  border: 0px;
  border-radius: 10px;
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.2), 0 4px 16px 0 rgba(0, 0, 0, 0.19);
  min-width: 300px;
}
.article-category-text {
  color: #fe6f8e;
}
.article-title-text {
  font-weight: bold;
  font-size: 20px;
}
.article-subtext {
  font-size: 14px;
  color: #707070;
}
</style>
<script>
import moment from "moment";
export default {
  name: "HomeBlogItem",
  props: {
    article: {
      type: Object,
      required: true,
    },
  },
  filters: {
    dateOnly: function (value) {
      if (!value) return;
      return moment(String(value)).format("MMM DD, YYYY");
    },
  },
};
</script>
