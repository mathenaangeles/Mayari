<template>
  <b-container fluid class="admin-article-form p-5">
    <b-card class="text-left p-4 edit-article-card">
      <b-row align-v="center" align-h="space-between">
        <b-col md="8">
          <b-row align-v="center">
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
            <h1 class="ml-3 bold">Article {{article.id && !isNew ? article.id : ""}} </h1>
          </b-row>
        </b-col>
      </b-row>
      <hr class="border-dark mb-4" style="border-width: 3px" />
      <div class="mt-4">
        <b-form>
          <b-form-group label="Author">
            <b-form-input v-model="form.author" placeholder="Enter author" required></b-form-input>
          </b-form-group>
          <b-form-group label="Title">
            <b-form-input v-model="form.title" placeholder="Enter title" required></b-form-input>
          </b-form-group>
          <b-form-group label="Preview">
            <b-form-input v-model="form.preview" placeholder="Enter preview"></b-form-input>
          </b-form-group>
          <b-form-group label="Body">
            <b-form-textarea v-model="form.body" placeholder="Enter body" rows=10></b-form-textarea>
          </b-form-group>
          <b-form-group label="Category">
            <b-form-input v-model="form.category" placeholder="Enter category"></b-form-input>
          </b-form-group>  
          <b-form-file
            class="mb-3"
            v-model="form.preview_image"
            placeholder="Choose a file or drop it here..."
            drop-placeholder="Drop file here..."
          ></b-form-file>
          <div class="custom-checkbox ml-4 mb-4">
            <input
              type="checkbox"
              id="checkbox_1"
              class="custom-control-input"
              v-model="form.is_published"
            />
            <label class="custom-control-label" for="checkbox_1"
              >&nbsp;Do you want to <b>publish</b> this article?</label
            >
          </div>
          <div class="custom-checkbox ml-4 mb-4">
            <input
              type="checkbox"
              id="checkbox_2"
              class="custom-control-input"
              v-model="form.is_featured"
            />
            <label class="custom-control-label" for="checkbox_2"
              >&nbsp;Do you want to <b>feature</b> this article?</label
            >
          </div>
          <b-form-group v-if="isNew">
            <b-button @click="onCreateArticle" variant="dark">Create</b-button>
          </b-form-group>
          <b-form-group v-else>
            <b-button @click="onUpdateArticle" variant="dark" class="mr-2">Save</b-button>
            <b-button @click="onDeleteArticle" variant="outline-dark"
              >Delete</b-button
            >
          </b-form-group>
        </b-form>
      </div>
    </b-card>
  </b-container>
</template>
<style scoped>
.edit-article-card {
  border-radius: 10px;
  box-shadow: 2px 4px 6px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  height: 100%;
}
.custom-checkbox .custom-control-input:checked ~ .custom-control-label::before {
  background-color: black !important;
}
.custom-checkbox
  .custom-control-input:checked:focus
  ~ .custom-control-label::before {
  box-shadow: 0 0 0 1px #fff, 0 0 0 0.2rem #e5eef7;
}
.custom-checkbox .custom-control-input:focus ~ .custom-control-label::before {
  box-shadow: 0 0 0 1px #fff, 0 0 0 0.2rem #e5eef7;
}
.custom-checkbox .custom-control-input:active ~ .custom-control-label::before {
  background-color: black;
}
</style>
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
      this.isNew = false;
      this.$store.dispatch("fetchArticle", {
        articleId: parseInt(this.$route.params.id),
      });
    } else {
      this.$store.dispatch("resetArticle")
    }
  },
  computed: {
    article() {
      return this.$store.state.article;
    },
  },
  watch: {
      article: function () {
        this.initializeForm()
      }
  },
  methods: {
    hasHistory() {
      return window.history.length > 2;
    },
    initializeForm(){
      let user = this.$store.state.user;
      if (user && this.$route.params.id == this.article.id) {
        try {
          this.form.author = this.article.author;
          this.form.title = this.article.title;
          this.form.preview = this.article.preview;
          this.form.body = this.article.body;
          this.form.category = this.article.category;
          this.form.is_published = this.article.is_published;
          this.form.is_featured = this.article.is_featured;
        } catch (error) {
          console.log("ERROR: User could not be found.", error);
        }
      }
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
      let article = new FormData();
      article.append("author", this.form.author);
      article.append("title", this.form.title);
      article.append("preview", this.form.preview);
      article.append("body", this.form.body);
      article.append("category", this.form.category);
      console.log(this.form.is_published);
      console.log(this.form.is_featured);
      article.append("is_published", this.form.is_published);
      article.append("is_featured", this.form.is_featured);
      article.append("preview_image", this.form.preview_image);
      this.$store
        .dispatch("updateArticle", {
          article: article,
          articleId: this.article.id,
        })
        .then(() => this.$router.push("/admin/blog"))
        .catch((error) => {
          console.log("ERROR: Article could not be updated.", error);
        });
    },
    onDeleteArticle(event) {
      event.preventDefault();
      this.$store
        .dispatch("deleteArticle", this.article.id)
        .then(() => this.$router.push("/admin/blog"))
        .catch((error) => {
          console.log("ERROR: Article could not be deleted.", error);
        });
    },
  },
};
</script>
