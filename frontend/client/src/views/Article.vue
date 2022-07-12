<template>
  <b-container class="article my-5 px-4">
    <b-row>
      <b-col lg="4" class="image-col px-0">
        <b-img class="article-image" fluid alt="article image" :src="article.preview_image"/>
      </b-col>
      <b-col lg="6" class="details-col px-0">
        <h5 class="purple-text">{{ article.category }}</h5>
        <h1 class="article-title">{{ article.title }}</h1>  
        <p class="article-preview">{{ article.preview }}</p>  
        <b-row>
          <b-col>
            <div class="purple-text">Written by</div>
            <p>{{ article.author }}</p>
          </b-col>
          <b-col>
            <div class="purple-text">Published on</div>
            <p>{{ article.updated_at | dateOnly }}</p>
          </b-col>
          <b-col>
             <b-row align-v="center">
              <ShareNetwork
                network="facebook"
                :url="link"
                :title="article.title"
                :description="article.preview"
                hashtags="mayari"
              >
                <b-button class="p-2 mt-1" variant="outline-secondary"><facebook :size="30" /></b-button>
              </ShareNetwork>    
              <ShareNetwork
                network="twitter"
                :url="link"
                :title="article.title"
                hashtags="mayari"
              >
                <b-button class="mx-2 p-2 mt-1" variant="outline-secondary"><twitter :size="30" /></b-button>
              </ShareNetwork>
              <ShareNetwork
                network="linkedin"
                :url="link"
                :title="article.title"
              >
                <b-button class="p-2 mt-1" variant="outline-secondary"><linkedin :size="30" /></b-button>
              </ShareNetwork>
            </b-row>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
    <b-row class="mt-4">
      <p>{{ article.body }}</p>
    </b-row>
  </b-container>
</template>
<style scoped>
.article {
  text-align: left;
  font-size: 18px;
}
@media (min-width: 992px) {
  .image-col {
    margin-right: 1.5rem;
  }
}
@media (max-width: 992px) {
  .details-col {
    margin-top: 3rem;
  }
}
.article-image {
  border-radius: 10px;
}
.purple-text {
  color: #ca4de5;
  font-weight: bold;
}
.article-title {
  font-size: 60px;
  font-weight: bold;
}
.article-preview {
  font-size: 20px;
}
</style>
<script>
import moment from "moment";
import { mapState } from "vuex";
import Facebook from "vue-material-design-icons/Facebook.vue";
import Twitter from "vue-material-design-icons/Twitter.vue";
import Linkedin from "vue-material-design-icons/Linkedin.vue";
export default {
  name: "Article",
  components: {
    Facebook,
    Twitter,
    Linkedin
  },
  beforeMount() {
    this.$store.dispatch("fetchArticle", {
      articleId: parseInt(this.$route.params.id),
    });
  },
  computed: {
    ...mapState({
      article: (state) => state.article
    }),
    link() {
      return "www.mayari.com/article/" + this.article.id; 
    }
  },
  filters: {
    dateOnly: function (value) {
      if (!value) return;
      return moment(String(value)).format("MMMM DD, YYYY");
    },
  },
};
</script>
