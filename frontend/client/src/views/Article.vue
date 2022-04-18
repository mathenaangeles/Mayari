<template>
  <div class="article"></div>
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
