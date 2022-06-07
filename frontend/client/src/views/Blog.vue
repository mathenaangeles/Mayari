<template>
  <div class="blog">
  <b-row class="px-5">
    <b-col md="9" class="d-flex justify-content-around">
      <b-button
        variant="light"
        >All Categories</b-button
       >
      <b-button
        variant="light"
        >Financial Literacy</b-button
        >
      <b-button
        variant="light"
        >Personal Finance</b-button
        >
      <b-button
        variant="light"
        >Financial Wellness</b-button
      >
      <b-button
        variant="light"
        >Financial Planning</b-button
      >
    </b-col>
    <b-col md="3">
      <b-row class="search-container">
        <b-col cols="10" class="pr-0">
          <b-form-input 
            placeholder="Search for keyword..."
            type="search"
            class="custom-search pr-0">
          </b-form-input>
        </b-col>
        <b-col cols="1" class="px-0">
          <b-button variant="light" class="search-button">
            <Magnify/>
          </b-button>
        </b-col>
      </b-row>
    </b-col>
  </b-row>
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
<style scoped>
.search-container {
  border: 2px solid #7070701c;
  border-radius: 10px

}
.custom-search {
  border: 0;
  outline: 0;
}
.custom-search:focus {
  box-shadow: none;
}

.search-button {
  background-color: white;
}
</style>
<script>
import Magnify from "vue-material-design-icons/Magnify";
import { mapState } from "vuex";
import BlogDashboardItem from "@/components/BlogDashboardItem.vue";
export default {
  name: "Blog",
  components: {
    BlogDashboardItem,
    Magnify
  },
  computed: mapState({
    articles: (state) => state.articles,
  }),
  beforeMount() {
    this.$store.dispatch("fetchArticles");
  },
};
</script>
