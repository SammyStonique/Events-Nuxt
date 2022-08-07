<template>
  <div>
    <Header />
    <ViewEvent :events="myEvents" />
    <Footer />
  </div>
</template>

<script>
import ViewEvent from "../components/ViewEvent.vue";
// import ViewEvent from '../components/ViewEvent.vue';
// import Header from '../components/Header.vue';
// import Footer from '../components/Footer.vue';

export default {
  data() {
    return {
      myEvents: [],
    };
  },
  methods: {},
  async created() {
    // await this.$axios.get("events_list/")
    await this.$axios
      .get("events_list/")
      .then((response) => {
        this.myEvents = response.data;
        console.log(this.myEvents);
      })
      .catch((error) => {
        console.log(error);
      });
  },
  mounted() {},
  components: { ViewEvent },
};
</script>

<style>
body {
  color: black;
  background: linear-gradient(to right, #ff416c, #ff4b2b);
  font-family: "Source Code Pro", monospace;
}
</style>
