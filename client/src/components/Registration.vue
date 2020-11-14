<template>
    <div class="registration">
        <div class="user_logo"></div>
        <h1>Registration</h1>

        <div class="menu">
            <div class="email"></div>
            <input v-model="email" type="email">
        </div>

        <div class="menu">
            <div class="password"></div>
            <input v-model="password1" type="password">
        </div>
        <div class="menu">
            <div class="password"></div>
            <input v-model="password2" type="password">
        </div>

        <div class="buttons">
            <button @click="to_login" class="back">Back</button>
            <button @click="create_account" class="save">Create Account</button>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "Registration",
    props: ['ip'],
    data(){
        return {
            email: undefined,
            password1: undefined,
            password2: undefined,
        }
    },
    methods: {
        to_login(){
            this.$emit('to_login', {
                go:true
            })
        },
        create_account(){
            if (this.password1 === undefined || this.password2 === undefined || this.email === undefined) {
                alert("Оставлены пустые поля!")}
            else {
                if (this.password1 !== this.password2) { alert("Пароли не совпадают!") }
                else {
                    // Запрос на создание
                    axios
                        .post("http://" + this.ip + "/registration", {'login':this.email, 'password':this.password1})
                        .then((response) => {
                            if(response.data.status === "success"){
                                this.to_login()
                            }
                            if(response.data.status === "conflict"){
                                alert("Пользователь с таким логином уже зарегестрирован!")
                            }
                            if(response.data.status === "error"){
                                alert("Ваш логин не корректен!")
                            }
                        })
                        .catch((error) => {
                            console.log(error);
                        });

                    // Вернуться на исходную
                }
            }
        }
    }
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
    text-align: center;
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