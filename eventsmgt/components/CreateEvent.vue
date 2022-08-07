<template>
    <div class="container">
            <div class="create-event-container">
                <h3>Create Event</h3>
                <form action="" @submit.prevent="createEvent">
                    <div class="row">
                        <div class="col-md-6 input-labels">
                            <label for="">Event Type</label>
                            <select name="eventtype" class="form-control" v-model="eventtype">
                                <option value="" disabled="true">--Select the Event Type--</option>
                                <option>Public Event</option>
                                <option>Invites Only</option>
                            </select>
                        </div>
                        <div class="col-md-6 input-labels">
                            <label for="">Event Name</label>
                            <input class="form-control" type="text" name="" id="" v-model="eventname">
                        </div>
                        <div class="col-md-6 input-labels">
                            <label for="">Venue</label>
                            <input class="form-control" type="text" name="" id="" v-model="venue">
                        </div>
                        <div class="col-md-6 input-labels">
                            <label for="">Date</label>
                            <input class="form-control" type="date" name="" id="" v-model="eventdate">
                        </div>
                        <div class="col-md-6 input-labels">
                            <label for="">Guests</label>
                            <input class="form-control" type="text" name="" id="" v-model="guests">
                        </div>
                        <div class="col-md-6 input-labels">
                            <label for="">Images</label>
                            <input class="form-control" type="file" ref="file" @change="onFileChange" accept="image/jpg, image/png, image/jpeg">
                        </div>
                        <div class="col-md-10 input-labels">
                            <label for="">Description</label>
                            <textarea class="form-control" name="" id="" cols="40" rows="2" v-model="description"></textarea>
                        </div>
                        <div class="col-md-12 input-btn">
                        <button class="btn create-event-btn" type="submit">Create Event</button>
                        </div>
                    </div>
                </form>
            </div>
        </div> 
</template>

<script>
export default {
    data() {
        return {
            eventtype: null,
            eventname: null,
            eventdate: null,
            venue: null,
            guests: null,
            description: null,
            image: null,
        };
    },
    methods: {
        onFileChange(e) {
            this.image = e.target.files[0];
            console.log("the image uploaded is:", this.image);
        },
        async createEvent() {
            let formData = new FormData();
            formData.append("images", this.image);
            formData.append("eventtype", this.eventtype);
            formData.append("eventname", this.eventname);
            formData.append("description", this.description);
            formData.append("venue", this.venue);
            formData.append("eventdate", this.eventdate);
            formData.append("guests", this.guests);
            await this.$axios.$post("create_event/", formData)
                .then((response) => {
                this.eventtype = "";
                this.eventname = "";
                this.description = "";
                this.venue = "";
                this.image = "";
                this.eventdate = "";
                this.guests = "";
                this.$router.push("/");
                this.$toasted.global.defaultSuccess({
                    msg: 'Event Succesfully Created'
                })
            })
                .catch((error) => {
                console.log(error);
            });
        }
    },
}
</script>

<style scoped>
.container{
    margin-top: 30px;
    
    
}
.create-event-container{
    background-color: white;
    height: auto;
    padding: 30px;
    margin-bottom: 60px;
    width: 80%;
}
form{
    width: 100%;
}
.input-labels{
    margin-top: 0px;
}
.input-btn{
    margin-top: 20px;
}

h3{
    font-family: 'Source Code Pro', monospace;
}
.create-event-btn{
    background: linear-gradient(to right, #FF416C, #FF4B2B);
    font-family: 'Source Code Pro', monospace;
    transition: transform 80ms ease-in;
}
.create-event-btn:hover{
    background: linear-gradient(to right, #FF4B2B,#FF416C );
    color: white;
    border: 1px solid white;
}
input{
    height: 35px;
    font-size: 16px;
}
.form-control:focus{
    box-shadow: none;
    border-color: #FF6F61;
}
</style>