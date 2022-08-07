<template>
    <div>
       <Header/>
       <ViewGuests
       :guests="myGuests"
       />
       <Footer/> 
    </div>
</template>

<script>
// import Header from '../components/Header.vue';
// import ViewGuests from '../components/ViewGuests.vue';
// import Footer from '../components/Footer.vue';
export default {
    data(){
        return{
            myGuests: []
        }
    },
    // components: { Header, ViewGuests, Footer },
    methods:{
        
    },
    async created(){
        await this.$axios.get('view_guests_list/')
        .then((response)=>{
            console.log(response.data)
            this.myGuests = response.data;
        })
        .catch((error)=>{
            console.log(error)
        })
    }
}
</script>

<style>

</style>