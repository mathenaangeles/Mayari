<template>
  <div>
    <b-row v-b-toggle="faqItem.id">
      <b-col>
        <span class="question">{{ faqItem.question }}</span>
        <span class="float-right"><ChevronDown /></span>
      </b-col>
    </b-row>
    <b-collapse v-bind:id="faqItem.id"> {{ faqItem.answer }} </b-collapse>
    <hr class="mt-1" />
  </div>
</template>
<style scoped>
.question {
  font-weight: bold;
}
hr {
  height: 2px;
  background-color: #000000;
  border: none;
}
</style>
<script>
import ChevronDown from "vue-material-design-icons/ChevronDown.vue";
export default {
  name: "FAQListItem",
  props: {
    faqItem: {
      type: Object,
      required: true,
    },
  },
  components: {
    ChevronDown,
  },
};
</script>
