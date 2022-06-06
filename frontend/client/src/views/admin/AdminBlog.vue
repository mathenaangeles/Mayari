<template>
  <div class="admin-blog">
    <b-container class="my-4">
      <b-row align-h="between">
        <b-col>
          <h1 class="float-left mb-2">Articles</h1>
        </b-col>
        <b-col class="new-text">
          <b-button variant="dark"
          ><b-link to="/admin/article">Create New Article</b-link></b-button
          >
        </b-col>
      </b-row>
      <b-table  striped bordered hover small :fields="fields" :items="articles">
        <template #cell(id)="data">
          {{ data.item.id }}
          <router-link
            :to="`article/${data.item.id}`"
            v-b-tooltip.hover
            title="Edit Article"
          >
            <Pencil />
          </router-link>
        </template>
      </b-table>
    </b-container>
  </div>
</template>
<style scoped>
.admin-blog {
  overflow: scroll;
}
svg {
  color: #f14f8c;
}
.new-text {
  text-align: right;
}
@media only screen and (max-width: 768px) {
  .new-text {
    text-align: left !important;
  }
}
a, a:hover {
  color: white;
  text-decoration: none;
}
</style>
<script>
import { mapState } from "vuex";
import Pencil from "vue-material-design-icons/Pencil.vue";
export default {
  name: "AdminBlog",
  components: {
    Pencil,
  },
  computed: mapState({
    articles: (state) => state.articles,
  }),
  data() {
    return {
      fields: [
        { key: "id", label: "ID"},
        { key: "title", label: "Title"},
        { key: "author", label: "Author"},
        { key: "category", label: "Category"},
        { key: "is_published", label: "Published"},
        { key: "is_featured", label: "Featured"},
      ],
    };
  },
  beforeMount() {
    this.$store.dispatch("fetchAllArticles");
  },
};
</script>
