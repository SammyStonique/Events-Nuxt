<template>
    <div class="container">
        <Header/>
        <About/>
        <Footer/>
    </div>
</template>

<script>
// import About from '../components/About.vue'
// import Footer from '../components/Footer.vue';
// import Header from '../components/Header.vue';
export default {
    head() {
        return {
            title: "About EM4U",
            meta: [
                {
                    hid: "description",
                    name: "description",
                    content: "Best event organizers"
                }
            ]
        };
    },
    data() {
        return {};
    },
    // components: { About, Footer, Header }
}
</script>

<style>
body {
    color: black;
    background: linear-gradient(to right, #FF416C, #FF4B2B);
    font-family: 'Source Code Pro', monospace;
}
</style>