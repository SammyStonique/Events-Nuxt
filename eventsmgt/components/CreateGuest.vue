<template>
    <div class="container">
        <div class="create-guest-container">
            <h3>Add Guest</h3>
            <form action="" @submit.prevent="createGuest">
                <div class="row">
                    <div class="col-md-6">
                            <label for="">Guest Title</label>
                            <select name="guesttitle" id="guesttitle" class="form-control" v-model="guesttitle">
                                <option value="" disabled="true">--Select Guest Title--</option>
                                <option value="">Dr.</option>
                                <option value="">Sir.</option>
                                <option value="">Madam</option>
                                <option value="">Mr.</option>
                                <option value="">Mrs.</option>
                                <option value="">Miss.</option>
                            </select>
                        </div>
                    <div class="col-md-6">
                        <label for="">First Name</label>
                        <input type="text" name="" class="form-control" v-model="firstname">
                    </div>
                    <div class="col-md-6">
                        <label for="">Last Name</label>
                        <input type="text" name="" class="form-control" v-model="lastname">
                    </div>
                    <div class="col-md-6">
                        <label for="">Email</label>
                        <input type="text" name="" class="form-control" placeholder="abc@example.com" v-model="email">
                    </div>
                    <div class="col-md-6">
                        <label for="">Phone Number</label>
                        <input type="text" name="" class="form-control" placeholder="07XXXXXXXX" v-model="phonenumber">
                    </div>
                    <div class="col-md-6">
                        <label for="">ID Number</label>
                        <input type="text" name="" class="form-control" v-model="idNo">
                    </div>
                    <div class="col-md-6">
                        <label for="">Gender</label>
                        <select name="guesttitle" class="form-control" v-model="gender">
                                <option value="" disabled="true">--Select your Gender--</option>
                                <option value="">Male</option>
                                <option value="">Female</option>
                                <option value="">Other</option>
                            </select>
                    </div>
                    <div class="col-md-6">
                        <label for="">County</label>
                        <select name="county" class="form-control" v-model="county">
                            <option value="" disabled="true">--Select your County--</option>
                            <option value="">Nairobi</option>
                            <option value="">Kisumu</option>
                            <option value="">Mombasa</option>
                            <option value="">Siaya</option>
                            <option value="">Nakuru</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                        <label for="">Guest Role</label>
                        <select name="guesttitle" class="form-control" v-model="guestrole">
                            <option value="" disabled="true">--Select Guest Role--</option>
                            <option value="">Guest of Honour</option>
                            <option value="">Main Speaker</option>
                            <option value="">Master of Ceremony</option>
                            <option value="">Attendee</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                        <label for="">Guest Reservation</label>
                        <select name="reservation" class="form-control" v-model="reservation">
                            <option value="" disabled="true">--Select Guest Reservation--</option>
                            <option value="">VVIP</option>
                            <option value="">VIP</option>
                            <option value="">First Class</option>
                            <option value="">Economy</option>
                        </select>
                    </div>
                </div>
                <button type="submit" class="btn btn-success create-guest-btn">Add Guest</button>
            </form>
        </div>    
    </div>
</template>

<script>
export default {
    data(){
        return{
            guesttitle: null,
            firstname : null,
            lastname : null,
            email : null,
            phonenumber : null,
            county : null,
            gender : null,
            guestrole: null,
            reservation: null,
            idNo : null,
            appliedEvent: null,
            eventOrganizer: null
        }
    },
    methods:{
        createGuest(){
            let formData = {
                firstname : this.firstname,
                lastname : this.lastname,
                email : this.email,
                identificationnumber : this.idNo,
                phonenumber : this.phonenumber,
                gender : this.gender,
                county : this.county,
                // event_applied_for : this. appliedEvent,
                // event_organizer : this.eventOrganizer
            }
            this.$axios.post('create_guests_list/', formData)
            .then((response)=>{
                console.log(response.data)
                this.$toasted.global.defaultSuccess({
                    msg: 'Guest Succesfully Added'
                })
                this.guesttitle = "";
                this.firstname = "";
                this.lastname = "";
                this.email = "";
                this.phonenumber = "";
                this.county = "";
                this.gender = "";
                this.guestrole= "";
                this.reservation= "";
                this.idNo = "";
                this.appliedEvent= "";
                this.eventOrganizer= "";
            })
            .catch((error)=>{
                console.log(error)
            })
        }
    }
}
</script>

<style scoped>
.create-guest-container{
    background-color: white;
    padding: 20px;
    margin-bottom: 60px;
}
.create-guest-btn{
    margin-top: 20px;
}
h3, label{
    color:black !important;
}
</style>