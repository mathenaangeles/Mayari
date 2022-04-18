<template>
  <div class="blog"></div>
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
