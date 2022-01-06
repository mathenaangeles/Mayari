<template>
  <div class="dashboard">
  </div>
</template>
<style scoped></style>
<script>
export default {
  name: "Dashboard",
  components: {},
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
  },
};
</script>
