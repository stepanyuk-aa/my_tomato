<template>
    <div class="login">
        <div class="user_logo"></div>
        <h1>Login</h1>

        <div class="menu">
           <div class="email"></div>
           <input v-model="email" type="email">
       </div>

        <div class="menu">
            <div class="password"></div>
            <input v-model="password" type="password">
        </div>

        <div class="buttons">
            <button @click='to_registration' class="registration">Registration</button>
            <button class="forgot_pass">Forgot password</button>
            <button @click='login' class="save">Sign in</button>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "Login",
    props: ['ip'],
    data(){
        return {
            email: undefined,
            password: undefined,
        }
    },
    methods: {
        to_tasks() {
            this.$emit('login_goto', {
                go:'tasks'
            })
        },
        to_registration(){
            this.$emit('login_goto', {
                go:'registration'
            })
        },
        local_storage(mode, key, value = ''){
            if (mode === 'set') {
                console.log("Set:" , key, "|", value)
                localStorage.setItem(key, value)
            }
            else {
                console.log(
                    localStorage.getItem(key)
                )
            }
        },
        login(){
            if (this.password === undefined || this.email === undefined) {
                alert("Оставлены пустые поля!")}
            else {
                axios
                    .post("http://" + this.ip + "/login", {'login':this.email, 'password':this.password})
                    .then((response) => {
                        if(response.data.status === "success"){
                            this.local_storage('set', 'token', response.data.token)
                            console.log(response.data);

                            this.to_tasks()
                        }
                        if(response.data.status === "error"){
                            alert("Ваш логин или пароль не корректен!")
                        }
                    })
                    .catch((error) => {
                        console.log(error);
                    });
                }
            }
        }
}
</script>

<style scoped>
    .login {
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
    .registration {
        background-color: coral;
    }
    .forgot_pass {
        background-color: darkgrey;
        height: 20%;
    }
    .save {
        background-color: #42b983;
    }
</style>