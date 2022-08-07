<template>
    <div>
       <div class="container" id="body-content">
            <div class="row ">
                <div class="col-md-6 " style="font-family: 'Montserrat', sans-serif; ">
                    <h1>Event</h1>
                    <h1>Management</h1>
                    <h1>Software</h1>
                    <p>Our Events Management System helps you simplify event planning for all your virtual,hybrid and in-person events. It has the power and flexibility global enterprises need and the scalability that event organizers love.</p>
                    <a href=""><button id="book-now" class="btn btn-outline-info">View Upcoming Events</button></a>
                </div>

                <div class="col-md-6 ">
                    <!-- <img src="../static/images/pexels-serpstat-572056.jpg" height="300px " width="100%" style="border: none;"> -->
                    <iframe width="100%" height="300px" src="https://www.youtube-nocookie.com/embed/XbFfVwthbMc?autoplay=1&amp;mute=1"></iframe>
                </div>
            </div>
        </div> 
    </div>
</template>

<script>
export default {
    middleware: 'auth'
}
</script>

<style scoped>
#body-content {
    margin-top: 100px;
    margin-bottom: 50px;
   
}
h1, p {
    color:white;
}

#book-now {
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-left: 70px;
    margin-bottom: 20px;
    background-color: #FF4B2B;
    color: #fff;
    border-radius: 20px;
    padding: 10px 20px;
    border: 1px solid #fff;
    transition: transform 80ms ease-in;
}

#book-now button:active {
    transform: scale(0.95);
}

#book-now button:focus {
    outline: none;
}
iframe{
    border:none;
}
</style>