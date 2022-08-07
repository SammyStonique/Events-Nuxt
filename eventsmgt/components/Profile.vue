<template>
  <div class="container">
    <div class="content-section">
      <div class="row">
        <div class="col-md-3">
          <img class="rounded-circle account-img" src="" alt="Image" />
        </div>
        <div class="col-md-3">
          <h2 class="account-heading">Username</h2>
          <p class="text-secondary">{{ email }}</p>
        </div>
      </div>
      <!-- FORM HERE -->
      <form action="" @submit.prevent="updateProfile">
        <div class="row">
          <div class="col-md-6 input-labels">
            <label for="">First Name</label>
            <input
              class="form-control"
              type="text"
              name=""
              id=""
              placeholder="First Name"
              v-model="firstname"
            />
          </div>
          <div class="col-md-6 input-labels">
            <label for="">Last Name</label>
            <input
              class="form-control"
              type="text"
              name=""
              id=""
              placeholder="Last Name"
              v-model="lastname"
            />
          </div>
          <div class="col-md-6 input-labels">
            <label for="">Email</label>
            <input
              class="form-control"
              type="text"
              name=""
              id=""
              placeholder="Email"
              v-model="email"
            />
          </div>
          <div class="col-md-6 input-labels">
            <label for="">Gender</label>
            <select
              name="gender"
              class="form-control"
              placeholder="Gender"
              v-model="gender"
            >
              <option value="" disabled="true">--Select your Gender--</option>
              <option>Male</option>
              <option>Female</option>
              <option>Other</option>
            </select>
          </div>
          <div class="col-md-6 input-labels">
            <label for="">Phone Number</label>
            <input
              class="form-control"
              type="text"
              name=""
              id=""
              placeholder="07XXXXXXXX"
              v-model="phonenumber"
            />
          </div>
          <div class="col-md-6 input-labels">
            <label for="">Date of Birth</label>
            <input class="form-control" type="date" name="" id="" v-model="birthdate" />
          </div>
          <div class="col-md-6 input-labels">
            <label for="">City</label>
            <select name="city" class="form-control" placeholder="City" v-model="city">
              <option value="" disabled="true">--Select your City--</option>
              <option>Nairobi</option>
              <option>Mombasa</option>
              <option>Kisumu</option>
              <option>Nakuru</option>
            </select>
          </div>
          <div class="col-md-6 input-labels">
            <label for="">County</label>
            <select
              name="county"
              class="form-control"
              placeholder="County"
              v-model="county"
            >
              <option value="" disabled="true">--Select your County--</option>
              <option>Nairobi</option>
              <option>Mombasa</option>
              <option>Kisumu</option>
              <option>Siaya</option>
            </select>
          </div>
          <div class="col-md-6 input-labels">
            <label for="">Image</label>
            <input
              class="form-control"
              type="file"
              ref="file"
              @change="onFileChange"
              accept="image/jpg, image/png, image/jpeg"
            />
          </div>
          <div class="col-md-12 input-labels">
            <label for="">Bio</label>
            <textarea class="form-control" cols="40" rows="2" v-model="bio"></textarea>
          </div>
        </div>
        <button class="btn btn-success btn-update-profile" type="submit">
          Update Profile
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  props: [
    "firstname",
    "lastname",
    "email",
    "birthdate",
    "gender",
    "phonenumber",
    "city",
    "county",
    "image",
    "bio",
  ],
  data() {
    return {
      firstname: null,
      lastname: null,
      email: null,
      birthdate: null,
      gender: null,
      phonenumber: null,
      city: null,
      county: null,
      image: null,
      bio: null,
    };
  },
  methods: {
    onFileChange(e) {
      this.image = e.target.files[0];
      console.log("the image uploaded is:", this.image);
    },
    async updateProfile() {
      let formData = {
        firstname: this.firstname,
        lastname: this.lastname,
        image: this.image,
        bio: this.bio,
        birthdate: this.birthdate,
        gender: this.gender,
        email: this.email,
        contact: this.contact,
        city: this.city,
        county: this.county,
      };
      await this.$axios
        .put("user-profile/1", formData)
        .then((response) => {
          console.log(response.data);
          this.$toasted.global.defaultSuccess({
            msg: "Profile Updated Succesfully",
          });
        })
        .catch((error) => {
          console.log(error);
          this.$toasted.global.defaultError({
            msg: "Profile Update Failed",
          });
        });
    },
  },
  // async created() {
  //   await this.$axios.get();
  // },
};
</script>

<style scoped>
.content-section {
  background-color: white;
}
.account-img {
  height: 125px;
  width: 125px;
}
.account-heading {
  color: black;
}
.text-secondary {
  color: black;
  margin-bottom: 20px;
}
.content-section {
  margin-bottom: 60px;
  width: 80%;
  margin-left: 30px;
  padding: 30px;
}
.btn-update-profile {
  margin-top: 20px;
}
.input-labels {
  color: black;
  font-family: "Montserrat", sans-serif;
}
</style>
