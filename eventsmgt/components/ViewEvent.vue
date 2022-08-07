<template>
    <div class="container">
    <div class="events-container">
            <h3>Events List</h3>
            <table>
                <thead>
                    <th>Event Type</th>
                    <th>Event Name</th>
                    <th>Venue</th>
                    <th>Date</th>
                    <th>Description</th>
                    <th>Guests</th>
                    <th>Image</th>

                </thead>
                <tbody v-for="event in events" :key="event.id">
                    <tr>
                        <td>{{event.eventtype}}</td>
                        <td>{{event.eventname}}</td>
                        <td>{{event.venue}}</td>
                        <td>{{event.date}}</td>
                        <td>{{event.description}}</td>
                        <td>{{event.guests}}</td>
                        <td>{{event.image}}</td>
                    </tr>
                </tbody>
            </table>
        
        </div>
    </div>
</template>

<script>
export default {
    name: "ViewEvent",
    props: ['events']
}
</script>

<style scoped>
.events-container{
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
thead{
    background-color: #dddddd;
    font-weight: bold;
}

</style>