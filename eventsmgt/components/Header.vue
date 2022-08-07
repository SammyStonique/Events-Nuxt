<template>
    <div class="container">
        <nav class="navbar navbar-default navbar-expand-lg navbar-light">
            <div class="container-fluid">
                <nuxt-link to="/homepage" class="navbar-brand " href="">EM4U SOLUTIONS</nuxt-link>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                  </button>
                <div class="collapse navbar-collapse " id="navbarSupportedContent">
                    <ul class="navbar-nav ">
                        <li class="nav-item " v-if="!isAuthenticated">
                            <nuxt-link to="/about" class="nav-link active " aria-current="page" >Our Solutions</nuxt-link>
                        </li>
                        <li class="nav-item ">
                            <nuxt-link to="/about" class="nav-link active " aria-current="page" >About</nuxt-link>
                        </li>

                        <li class="nav-item ">
                            <nuxt-link to="/contact" class="nav-link " href="">Contact Us</nuxt-link>
                        </li>
                        <div class="nav-item dropdown" v-if="isAuthenticated">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                              Guests
                            </a>
                            <div class="dropdown-content">
                                <nuxt-link to="/addguest" class="dropdown-item" >Add Guest</nuxt-link>
                                <nuxt-link to="/guestlist" class="dropdown-item">My Guest Lists</nuxt-link>
                                <hr class="dropdown-divider">
                                <nuxt-link to="" class="dropdown-item" href="#">Queries</nuxt-link>
                            </div>
                        </div>
                        <li class="nav-item dropdown" v-if="isAuthenticated">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                              Manage Events
                            </a>
                            <div class="dropdown-content">
                                <li><nuxt-link to="/createevent" class="dropdown-item" href="">Create Event</nuxt-link></li>
                                <li><nuxt-link to="/viewevents" class="dropdown-item" href="">My Events</nuxt-link></li>
                                <li><nuxt-link to="/publicevents" class="dropdown-item" href="">Public Event Attendees</nuxt-link></li>
                                <li><nuxt-link to="/privateevents" class="dropdown-item" href="">Invites Only Applications</nuxt-link></li>
                                <li>
                                    <hr class="dropdown-divider">
                                </li>
                                <li><a class="dropdown-item" href="#">Queries</a></li>
                            </div>
                        </li>

                        <nuxt-link to="/profile" class=" nav-link" v-if="isAuthenticated"><i class="fa fa-user-circle" aria-hidden="true"></i>Profile</nuxt-link>
                        <nuxt-link to="/login" class="nav-link" v-if="!isAuthenticated"><i class="fa fa-user-circle" aria-hidden="true"></i>Login</nuxt-link>
                        <nuxt-link to="/logout" class=" nav-link" v-if="isAuthenticated">Welcome, {{email}}</nuxt-link>
                        <nuxt-link to="/logout" class=" nav-link" v-if="isAuthenticated"><i class="fa fa-user-circle" aria-hidden="true"></i>Logout</nuxt-link>




                    </ul>
                </div>
            </div>
        </nav>
    </div>

</template>

<script>
import { mapGetters } from 'vuex';
import { mapState } from 'vuex';
export default {
    name: "Header",
    data(){
        return{

        }
    },
    computed:{
        ...mapGetters(['isAuthenticated', 'loggedInUser']),
        ...mapState(['email'])
    },
    
    mounted(){
        console.log('the authentication status is ',this.isAuthenticated);
        console.log('the current logged in user is ',this.email)

    }
}
</script>

<style scoped>
.navbar .navbar-expand-lg .navbar-light {
    background-color: transparent;
}

.navbar-light .navbar-brand {
    color: white;
    font-family: 'Montserrat', sans-serif;
}

.nav-item {
    padding: 0 5px;
    font-family: 'Montserrat', sans-serif;
}

.navbar-light .navbar-nav .nav-link.active {
    color: white;
    font-family: 'Montserrat', sans-serif;
}

.navbar-light .navbar-nav .nav-link {
    color: white;
    font-family: 'Montserrat', sans-serif;
}

.nav-link active {
    color: white;
    font-family: 'Montserrat', sans-serif;
}

.nav-link dropdown-toggle {
    color: white;
}

.nav-link {
    color: white;
    font-family: 'Montserrat', sans-serif;
}
.dropdown {
  position: relative;
  display: inline-block;
}
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  padding: 12px 16px;
  z-index: 1;
}

.dropdown:hover .dropdown-content {
  display: block;
}

</style>