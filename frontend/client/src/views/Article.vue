<template>
  <div class="article">
    <h1>{{ article.title }}</h1>
    <h1>{{ article.preview }}</h1>
    <h1>{{ article.author }}</h1>
    <h1>{{ article.body }}</h1>
  </div>
</template>
<style scoped></style>
<script>
import { mapState } from "vuex";
export default {
  name: "Article",
  components: {},
  methods: {},
  beforeMount() {
    this.$store.dispatch("fetchArticle", {
      articleId: parseInt(this.$route.params.id),
    });
  },
  computed: mapState({
    article: (state) => state.article,
  }),
};
</script>
