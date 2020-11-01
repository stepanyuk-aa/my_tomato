<template>
    <div class="registration">
        <div class="user_logo"></div>
        <h1>Registration</h1>

        <div class="menu">
            <div class="email"></div>
            <input type="email">
        </div>

        <div class="menu">
            <div class="password"></div>
            <input type="password">
        </div>
        <div class="menu">
            <div class="password"></div>
            <input type="password">
        </div>

        <div class="buttons">
            <button class="back">Back</button>
            <button class="save">Create Account</button>
        </div>
    </div>
</template>

<script>
export default {
    name: "Registration"
}
</script>

<style scoped>
.registration {
    display: flex;
    flex-direction: column;
    margin-left: auto;
    margin-right: auto;
    margin-top: -20%;

    align-items: center;
    justify-content: center;
    flex: 1 0 120px;

}

.menu {
    display: flex;
    margin: 1%;
    width: 70%;
    height: 10%;

    justify-content: center;
    align-items: center;
}

input {
    border-radius: 100px;
    width: 70%;
    height: 30%;
}

.user_logo {
    width: 20%;
    height: 20%;

    margin-bottom: 5%;
    margin-top: 25%;
    background: url('../img/user_logo.svg') no-repeat ;
}

.email {
    width: 10%;
    color: #1F2323;
    height: 50%;
    background: url('../img/email.svg') no-repeat; /*Pixel perfect*/
}
.password {
    width: 10%;
    color: #1F2323;
    height: 50%;
    background: url('../img/shield.svg') no-repeat; /*Pixel perfect*/
}

/* Buttons */
.buttons {
    display: flex;
    width: 60%;
    height: 15%;
    justify-content: space-around;
}
button {
    width: 30%;
    height: 30%;
}
.back {
    background-color: coral;
}

.save {
    background-color: #42b983;
}
</style>