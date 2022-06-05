<template>
  <div class="blog">
    <div v-if="!articles || articles.length === 0">
      <h2>Oops, there's nothing here!</h2>
    </div>
    <BlogDashboardItem
      v-for="article in articles"
      :key="article.id"
      :article="article"
    >
    </BlogDashboardItem>
  </div>
</template>
<style scoped></style>
<script>
import { mapState } from "vuex";
import BlogDashboardItem from "@/components/BlogDashboardItem.vue";
export default {
  name: "Blog",
  components: {
    BlogDashboardItem,
  },
  computed: mapState({
    articles: (state) => state.articles,
  }),
  beforeMount() {
    this.$store.dispatch("fetchArticles");
  },
};
</script>
