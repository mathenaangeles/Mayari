<template>
  <div class="admin-blog">
    <b-button variant="dark"
      ><b-link to="/admin/article">Create New Article</b-link></b-button
    >
    <b-table striped hover :fields="fields" :items="articles">
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
  </div>
</template>
<style scoped>
.admin-blog {
  overflow: scroll;
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
      fields: ["id", "title"],
    };
  },
  beforeMount() {
    this.$store.dispatch("fetchAllArticles");
  },
};
</script>
