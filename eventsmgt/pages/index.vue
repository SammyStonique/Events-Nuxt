<template>
    <div>
        <Header/>
        <HomePage/>
        <Footer/>
    </div>
  
</template>

<script>
// import Header from '../components/Header.vue';
// import HomePage from '../components/HomePage.vue';
// import Footer from '../components/Footer.vue';
export default {
    middleware: 'guest',
    name: "IndexPage",
    // components: { Header, HomePage, Footer }
}
</script>

<style>
body {
    color: white;
    background: linear-gradient(to right, #FF416C, #FF4B2B);
    font-family: 'Montserrat', sans-serif;
}
</style>
