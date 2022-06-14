<template>
  <div class="blog">
    <b-carousel
      v-if="featuredArticles.length > 0"
      v-model="slide"
      :interval="4000"
      indicators
      background="#ababab"
      img-width="1024"
      img-height="500"
      style="text-shadow: 1px 1px 2px #333"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <b-carousel-slide
        v-for="fArticle in featuredArticles"
        :key="fArticle.id"
        class="custom-carousel-slide"
      >
        <template #img>
          <img
            class="d-block img-fluid w-100"
            style="height: 40vh; object-fit: cover; object-position: right 20%"
            :src="fArticle.preview_image"
            alt="image slot"
          />
        </template>
        <div class="text-xs">
          {{ fArticle.created_at | dateOnly }} | {{ fArticle.author }}
        </div>
        <h1>{{ fArticle.title }}</h1>
        <div>
          {{ fArticle.preview }} <br />
          {{ fArticle.category }}
        </div>
      </b-carousel-slide>
    </b-carousel>
    <b-row class="px-5">
      <b-col md="9" class="d-flex justify-content-around">
        <b-button variant="light">All Categories</b-button>
        <b-button variant="light">Financial Literacy</b-button>
        <b-button variant="light">Personal Finance</b-button>
        <b-button variant="light">Financial Wellness</b-button>
        <b-button variant="light">Financial Planning</b-button>
      </b-col>
      <b-col md="3">
        <b-row class="search-container">
          <b-col cols="10" class="pr-0">
            <b-form-input
              placeholder="Search for keyword..."
              type="search"
              class="custom-search pr-0"
            >
            </b-form-input>
          </b-col>
          <b-col cols="1" class="px-0">
            <b-button variant="light" class="search-button">
              <Magnify />
            </b-button>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
    <div v-if="!articles || articles.length === 0">
      <h2>Oops, there's nothing here!</h2>
    </div>
    <b-row class="mt-2">
      <BlogDashboardItem
        v-for="article in articles"
        :key="article.id"
        :article="article"
      >
      </BlogDashboardItem>
    </b-row>
  </div>
</template>
<style scoped>
.search-container {
  border: 2px solid #7070701c;
  border-radius: 10px;
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

.custom-carousel-slide img {
  object-fit: cover !important;
}
</style>
<script>
import Magnify from "vue-material-design-icons/Magnify";
import { mapState } from "vuex";
import moment from "moment";
import BlogDashboardItem from "@/components/BlogDashboardItem.vue";
export default {
  name: "Blog",
  components: {
    BlogDashboardItem,
    Magnify,
  },
  computed: mapState({
    articles: (state) => state.articles,
    featuredArticles: (state) => state.articles.filter((x) => x.is_featured),
  }),
  beforeMount() {
    this.$store.dispatch("fetchArticles");
  },
  filters: {
    dateOnly: function (value) {
      if (!value) return;
      return moment(String(value)).format("MMM DD, YYYY");
    },
  },
};
</script>
