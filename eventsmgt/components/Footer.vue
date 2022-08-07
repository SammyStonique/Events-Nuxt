<template>
    <div class="container-fluid footer">
        <p>
            Created with <i class="fa fa-heart"></i> by
            <a target="_blank" href="">SammyB</a>
        </p>
    </div>
</template>

<script>
export default {
    name: "Footer"
}
</script>

<style scoped> 
.footer {
    background-color: #222;
    color: #fff;
    font-size: 14px;
    bottom: 0;
    left: 0;
    right: 0;
    height: 40px;
    text-align: center;
    z-index: 999;
    margin-top: 20px;
    padding-top: 10px;
    position:fixed;
}

.footer i {
    color: red;
}

.footer a {
    color: #3c97bf;
    text-decoration: none;
}


</style>
