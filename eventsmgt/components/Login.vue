<template>
    <div class="container">
            <div class="login-container">
                <form action="" @submit.prevent="userLogin">
                    <h3>Login</h3>
                    <div class="row">
                        <div class="col-md-12">
                            <label for="">Email</label>
                            <input class="form-control" type="email" v-model="user.email">
                        </div>
                        <div class="col-md-12">
                            <label for="">Password</label>
                            <input class="form-control" type="password" v-model="user.password">
                        </div>
                        <small>Forgot Password? Reset</small>
                        <small>Don't have an account?<nuxt-link to="/register">Register</nuxt-link></small>
                        <div class="col-md-12">
                            <button class="btn login-btn" type="submit">Login</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
</template>

<script>
export default {
    middleware: 'guest',
    data() {
        return {
            user:{},
        };
    },
    methods: {
        async userLogin() {
        try {
            await this.$auth.loginWith('local', {
            data: this.user
            })
            this.$toasted.global.defaultSuccess({
            msg: 'Login Succesful'
            })
            this.$router.replace("/homepage");
            this.$store.state.email = this.user.email
            console.log(this.$store.state.email)

        } catch (err) {
            this.$toasted.global.defaultError({
            msg: 'Invalid Credentials'
            })
        }
        }
    },
}
</script>

<style scoped>
form{
    width: 80%;
    padding: 20px;
}
.login-btn{
    background: linear-gradient(to right, #FF416C, #FF4B2B);
    font-family: 'Source Code Pro', monospace;
    transition: transform 80ms ease-in;
}
.login-btn:hover{
    background: linear-gradient(to right, #FF4B2B,#FF416C );
    color: white;
    border: 1px solid white;
}
.login-container{
    margin-bottom: 60px;
}
h3,label,small{
    color:black !important;
}
</style>