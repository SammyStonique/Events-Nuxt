<template>
    <div>
        <Header/>
        <CreateEvent/> 
        <Footer/>
    </div>
</template>

<script>
// import CreateEvent from '../components/CreateEvent.vue';
// import Header from '../components/Header.vue';
// import Footer from '../components/Footer.vue';

export default {
    head() {
        return {
            title: "Create An Event",
            meta: [
                {
                    hid: "description",
                    name: "description",
                    content: "Creating an event"
                }
            ]
        };
    },
    // components: { CreateEvent, Header, Footer }
}

</script>

<style>
body {
    color: black;
    background: linear-gradient(to right, #FF416C, #FF4B2B);
    font-family: 'Source Code Pro', monospace;
}

</style>