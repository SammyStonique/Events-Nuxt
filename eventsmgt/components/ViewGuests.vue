<template>
    <div class="container">
    <div class="guests-container">
        <h3>Guest List</h3>
            <table>
                <thead>
                    <th>Names</th>
                    <th>Email</th>
                    <th>Mobile No</th>
                    <th>ID Number</th>
                    <th>Gender</th>
                    <th>County</th>
                    <th>Guest Role</th>
                    <th>Reservation</th>
                </thead>
                <tbody v-for="guest in guests" :key="guest.id">
                    <tr>
                        <td>{{guest.guesttitle}} {{guest.firstname}} {{guest.lastname}}</td>
                        <td>{{guest.email}}</td>
                        <td>{{guest.phonenumber}}</td>
                        <td>{{guest.identificationnumber}}</td>
                        <td>{{guest.gender}}</td>
                        <td>{{guest.county}}</td>
                        <td>{{guest.guestrole}}</td>
                        <td>{{guest.reservation}}</td>
                    </tr>
                </tbody>
                
            </table> 
        </div>  
    </div>
</template>

<script>
export default {
    name: "ViewGuests",
    props: ['guests']
}
</script>

<style scoped>
.guests-container{
    width: 100%;
    background-color: white !important;
    margin-top: 50px;
    padding:30px;
}
table{
    border-collapse: collapse;
    width: 100%;
}
td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
  color: black !important;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
h3{
    color: black !important;
}
</style>