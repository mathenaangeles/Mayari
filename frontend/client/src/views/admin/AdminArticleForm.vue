<template>
  <div class="admin-article-form">
    <h1>
      <button
        @click="hasHistory() ? $router.go(-1) : $router.push('/')"
        class="btn btn-link text-dark"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="32.709"
          height="23.069"
          viewBox="0 0 32.709 23.069"
        >
          <path
            id="Icon_ionic-ios-arrow-round-forward"
            data-name="Icon ionic-ios-arrow-round-forward"
            d="M28.734,11.693a1.635,1.635,0,0,0-.011,2.211l6.908,7.317H9.341a1.565,1.565,0,0,0,0,3.124H35.619l-6.908,7.317a1.647,1.647,0,0,0,.011,2.211A1.415,1.415,0,0,0,30.8,33.86l9.362-9.972h0a1.766,1.766,0,0,0,.307-.493,1.565,1.565,0,0,0,.114-.6,1.614,1.614,0,0,0-.42-1.093L30.8,11.729A1.393,1.393,0,0,0,28.734,11.693Z"
            transform="translate(40.584 34.321) rotate(180)"
          />
        </svg>
      </button>
      Article
    </h1>
    <b-form>
      <b-form-group label="Author">
        <b-form-input v-model="form.author"></b-form-input>
      </b-form-group>
      <b-form-group label="Title">
        <b-form-input v-model="form.title"></b-form-input>
      </b-form-group>
      <b-form-group label="Preview">
        <b-form-input v-model="form.preview"></b-form-input>
      </b-form-group>
      <b-form-group label="Body">
        <b-form-input v-model="form.body"></b-form-input>
      </b-form-group>
      <b-form-group label="Category">
        <b-form-input v-model="form.category"></b-form-input>
      </b-form-group>
      <b-form-group>
        <b-form-checkbox
          id="checkbox"
          v-model="form.is_published"
          @change="onPublish"
        >
          Publish
        </b-form-checkbox>
      </b-form-group>
      <b-form-group>
        <b-form-checkbox
          id="checkbox"
          v-model="form.is_featured"
          @change="onFeature"
        >
          Feature
        </b-form-checkbox>
      </b-form-group>
      <b-form-file
        v-model="form.preview_image"
        placeholder="Choose a file or drop it here..."
        drop-placeholder="Drop file here..."
      ></b-form-file>
      <b-form-group v-if="isNew">
        <b-button @click="onCreateArticle" variant="dark">Create</b-button>
      </b-form-group>
      <b-form-group v-else>
        <b-button @click="onUpdateArticle" variant="dark">Save</b-button>
        <b-button @click="onDeleteArticle" variant="outline-dark"
          >Delete</b-button
        >
      </b-form-group>
    </b-form>
  </div>
</template>
<style scoped></style>
<script>
export default {
  name: "AdminArticleForm",
  components: {},
  data: () => {
    return {
      form: {
        author: "",
        title: "",
        preview: "",
        body: "",
        category: "",
        is_published: false,
        is_featured: false,
        preview_image: null,
      },
      isNew: true,
    };
  },
  beforeMount() {
    if (this.$route.params.id) {
      this.$store.dispatch("fetchArticle", {
        articleId: parseInt(this.$route.params.id),
      });
      this.isNew = false;
    }
  },
  computed: {
    article() {
      if (this.isNew) {
        return this.$store.state.article;
      } else {
        return null;
      }
    },
  },
  created: function () {
    let user = this.$store.state.user;
    if (user && !this.isNew) {
      try {
        this.form.author = this.article.author;
        this.form.title = this.article.title;
        this.form.preview = this.article.preview;
        this.form.body = this.article.body;
        this.form.category = this.article.category;
        this.form.is_published = this.article.is_published;
        this.form.is_featured = this.article.is_featured;
        this.form.preview_image = this.article.preview_image;
      } catch (error) {
        console.log("ERROR: User could not be found.", error);
      }
    }
  },
  methods: {
    hasHistory() {
      return window.history.length > 2;
    },
    onFeature() {
      this.form.is_featured = !this.form.is_featured;
    },
    onPublish() {
      this.form.is_published = !this.form.is_published;
    },
    onCreateArticle(event) {
      event.preventDefault();
      let article = new FormData();
      article.append("author", this.form.author);
      article.append("title", this.form.title);
      article.append("preview", this.form.preview);
      article.append("body", this.form.body);
      article.append("category", this.form.category);
      article.append("is_published", this.form.is_published);
      article.append("is_featured", this.form.is_featured);
      article.append("preview_image", this.form.preview_image);
      this.$store
        .dispatch("postArticle", article)
        .then(() => this.$router.push("/admin/blog"))
        .catch((error) => {
          console.log("ERROR: Article could not be created.", error);
        });
    },
    onUpdateArticle(event) {
      event.preventDefault();
      this.$store
        .dispatch("updateArticle", {
          id: this.article.id,
          author: this.form.author,
          title: this.form.title,
          preview: this.form.preview,
          body: this.form.body,
          category: this.form.category,
          is_published: this.form.is_published,
          is_featured: this.form.is_featured,
          preview_image: this.form.preview_image,
        })
        .then(() => this.$router.push("/admin/blog"))
        .catch((error) => {
          console.log("ERROR: Article could not be updated.", error);
        });
    },
    onDeleteArticle(event) {
      event.preventDefault();
      this.$store
        .dispatch("deleteArticle")
        .then(() => this.$router.push("/admin/blog"))
        .catch((error) => {
          console.log("ERROR: Article could not be deleted.", error);
        });
    },
  },
};
</script>
