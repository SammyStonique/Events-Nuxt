<template>
    <div>
        <Header/>
        <Login/>
        <Footer/>
    </div>
</template>

<script>
// import Header from '../components/Header.vue'
// import Footer from '../components/Footer.vue';
// import Login from '../components/Login.vue';
export default {
    middleware: 'guest',
    // components: { Header, Footer, Login }
}
</script>

<style>
body {
    color: black;
    background: linear-gradient(to right, #FF416C, #FF4B2B);
    font-family: 'Source Code Pro', monospace;
}
.login-container{
    width: 80%;
    background-color: white !important;
    margin-top: 50px;
}

</style>