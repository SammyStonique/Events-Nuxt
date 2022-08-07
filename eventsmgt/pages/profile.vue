<template>
  <div>
    <Header />
    <Profile
      :firstname="firstname"
      :lastname="lastname"
      :email="email"
      :birthdate="birthdate"
      :gender="gender"
      :phonenumber="phonenumber"
      :city="city"
      :county="county"
      :image="image"
      :bio="bio"
    />
    <Footer />
  </div>
</template>

<script>
export default {
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
  async created() {
    await this.$axios
      .get("user-profile/1")
      .then((response) => {
        console.log(response.data);
        this.firstname = response.data.firstname;
        this.lastname = response.data.lastname;
        this.email = response.data.email;
        this.birthdate = response.data.birthdate;
        this.gender = response.data.gender;
        this.phonenumber = response.data.phonenumber;
        this.city = response.data.city;
        this.county = response.data.county;
        this.image = response.data.image;
        this.bio = response.data.bio;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style></style>
