<template>
    <div class="container">
        <div class="row ">
            <div class="col-md-6 " style="font-family: 'Montserrat', sans-serif; ">
                <h1>Ezen Events</h1>

                <p>For more information about our products and services, you can contact us through:</p>

                <p><a href="http://www.facebook.com" target=blank class="social"><i class="fa fa-facebook social-icon"></i>Facebook</a></p>
                <p><a href="http://www.accounts.google.com" target=blank class="social"><i class="fa fa-google-plus social-icon" ></i>Google</a></p>
                <p><a href="http://www.linkedin.com" target=blank class="social"><i class="fa fa-linkedin social-icon"></i>LinkedIn</a></p>
                <p><a href="http://www.whatsapp.com" target=blank class="social"><i class="fa fa-whatsapp social-icon"></i>+254717423651</a></p>
                <p><a href="http://www.instagram.com" target=blank class="social"><i class="fa fa-instagram social-icon"></i>@samuel_stonique</a></p>
                <p><a href="http://www.gmail.com" target=blank class="social"><i class="fas fa-envelope social-icon"></i>ezenfinancialsevents@gmail.com</a></p>
            </div>

            <div class="col-md-6 contact-img">
                <img src="../static/images/pexels-serpstat-572056.jpg" height="350px" width="100%">

            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.container{
    margin-top: 60px;
    
}
h1,p{
    color:white;
    font-family: 'Montserrat', sans-serif;
}
.social{
text-decoration: none;
color:white;
font-family: 'Montserrat', sans-serif;
}
.social-icon{
padding-top:6px;
text-align:center;
border: 1px solid white;
background-color:white;
width:30px;
height:30px;
margin-right:20px;
}
.fa-facebook{
    color: blue !important;
}
.fa-google-plus{
    color: yellow !important;
}
.fa-linkedin{
    color: blueviolet !important;
}
.fa-whatsapp{
    color: green !important;
}
.fa-instagram{
    color: red !important;
}
.fa-envelope{
    color: red !important;
}
.contact-img{
    border: none;
    height:"350px" ;
    width:"200px";
}
</style>