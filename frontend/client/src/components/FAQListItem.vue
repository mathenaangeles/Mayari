<template>
  <div>
    <b-row>
      <b-col cols="11">
        <span v-b-toggle="faqItem.id">{{ faqItem.question }}</span>
      </b-col>
      <b-col cols="1">
        <ChevronDown />
      </b-col>
    </b-row>
    <b-collapse v-bind:id="faqItem.id"> {{ faqItem.answer }} </b-collapse>
  </div>
</template>
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
