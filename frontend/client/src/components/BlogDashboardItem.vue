<template lang="">
  <div>
    <b-card
      :title="article.title"
      :img-src="article.preview_image"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem"
      class="mb-2"
    >
      <b-card-text>
        <router-link :to="`article/${article.id}`"> View Article </router-link>
      </b-card-text>
    </b-card>
  </div>
</template>
<script>
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
<style lang=""></style>
