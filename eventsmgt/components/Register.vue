<template>
    <div class="container">
        <div class="register-container">
            <form action="" @submit.prevent="registerUser">
                <h3>Register</h3>
                <div class="row">
                    <div class="col-md-6">
                        <label for="">First Name</label>
                        <input class="form-control" type="text" v-model="firstname">
                    </div>
                    <div class="col-md-6">
                        <label for="">Last Name</label>
                        <input class="form-control" type="text" v-model="lastname">
                    </div>
                    <div class="col-md-6">
                        <label for="">Email</label>
                        <input class="form-control" type="email" v-model="email">
                    </div>
                    <div class="col-md-6">
                        <label for="">Phone Number</label>
                        <input class="form-control" type="text" v-model="phonenumber">
                    </div>
                    <div class="col-md-6">
                        <label for="">Password</label>
                        <input class="form-control" type="password" v-model="password">
                    </div>
                    <div class="col-md-6">
                        <label for="">Confirm Password</label>
                        <input class="form-control" type="password" v-model="passwordconfirm">
                    </div>
                    <div class="col-md-12">
                        <button class="btn register-btn" type="submit">Register</button>
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
            firstname: null,
            lastname: null,
            email: null,
            phonenumber: null,
            password: null,
            passwordconfirm: null
        };
    },
    methods: {
        registerUser() {
            let formData = {
                first_name: this.firstname,
                last_name: this.lastname,
                email: this.email,
                phone_number: this.phonenumber,
            };
            this.$axios.post("register/", formData)
                .then((response) => {
                console.log(response.data);
                this.firstname = "";
                this.lastname = "";
                this.email = "";
                this.phonenumber = "";
                this.$toasted.global.defaultSuccess({
                    msg: 'Registration Succesful'
                })
            })
                .catch((error) => {
                console.log(error);
                this.$toast.error("Invalid Details!!");
            });
        }
    },
}
</script>

<style scoped>
.register-container{
    width: 80%;
    background-color: white !important;
    margin-top: 50px;
}
form{
    width: 80%;
    padding: 20px;
}
.register-btn{
    background: linear-gradient(to right, #FF416C, #FF4B2B);
    font-family: 'Source Code Pro', monospace;
    transition: transform 80ms ease-in;
}
.register-btn:hover{
    background: linear-gradient(to right, #FF4B2B,#FF416C );
    color: white;
    border: 1px solid white;
}
</style>