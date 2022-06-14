<template lang="">
  <div class="mx-2">
    <b-card
      :img-src="article.preview_image"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem"
      class="mb-2"
    >
      <b-card-text>
        <div class="text-left">
          <h5>
            {{ article.title }}
          </h5>
          <p>
            {{ article.preview }}
          </p>
          <router-link :to="`article/${article.id}`" class="router-link">
            Read more
          </router-link>
        </div>
      </b-card-text>
    </b-card>
  </div>
</template>
<script>
/* <b-card-text class="card-img-overlay">
        <div class="card-text-container text-left">
          <h5>
            <router-link :to="`article/${article.id}`" class="router-link">
              {{ article.title }}
            </router-link>
          </h5>
        </div>
      </b-card-text> */
export default {
  name: "BlogDashboardItem",
  props: {
    article: {
      type: Object,
      required: true,
    },
  },
  components: {},
};
</script>
<style scoped>
.card {
  overflow: hidden;
}
.card img {
  height: 300px;
  width: 300px;
}
/* 
.card-footer:last-child {
  border-radius: 0 !important;
}

.card-footer {
  padding: 0 !important;
  background-color: unset !important;
  border-top: unset !important;
}

.text-center {
  color: #fff;
}
.card-img-overlay {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  height: 100%;
  padding: 0;
}
.card-text-container {
  background-color: rgba(0, 0, 0, 0.3);
  color: white;
} */

.router-link {
  color: #f14f8c;
}
</style>
