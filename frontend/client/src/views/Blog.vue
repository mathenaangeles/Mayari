<template>
  <div class="blog">
    <ul>
      <li v-for="article in articles" :key="article.id">
        {{ article.title }}
        <router-link :to="`article/${article.id}`"> View Article </router-link>
      </li>
    </ul>
  </div>
</template>
<style scoped></style>
<script>
import { mapState } from "vuex";
export default {
  name: "Blog",
  components: {},
  computed: mapState({
    articles: (state) => state.articles,
  }),
  beforeMount() {
    this.$store.dispatch("fetchArticles");
  },
};
</script>
