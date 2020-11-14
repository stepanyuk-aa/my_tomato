<template>
    <div class="modal">
        <div class="task_title">
            <h1>Добавить задание {{ip}} </h1>
        </div>
        <div class="task_body">
            <div class="row">
                <p>Задание:</p>
                <input class="input_add_task" type="text">
            </div>
            <div class="row">
                <p>Интервал:</p>
                <input class="input_add_task" type="text">
            </div>
            <div class="row">
                <p>Повторений:</p>
                <input  class="input_add_task" type="text">
            </div>


        </div>
        <div class="task_buttons">
            <button class="Close btn" @click="close">Close</button>
            <button class="Save btn">Save</button>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "AddTask",
    props: ['ip'],
    data() {
        return {
            showModal: false
        }
    },
    methods: {
        close(){
            this.showModal = false
            this.$emit('Close_Add_Task')
        },
        send_task(data){
            console.log(data)
            axios
                .post("http://" + this.ip + "/addtask", {'login':'admin', 'password':"test"})
                .then((response) => {
                    if(response.data.status === "success"){
                        this.local_storage('set', 'token', response.data.token)
                        console.log(response.data);
                    }
                    else {
                        console.log(response.data);
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    }
}
</script>

<style scoped>
    .modal {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
    }
    .task_title {
        text-align: center;
    }
    .task_body {
        display: flex;
        flex-direction: column;

        width: 70%;
    }

    .row {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .input_add_task {
        width: 60%;
        height: 50%;
        margin-left: 10%;
        border-radius: 10px;
    }
    .task_buttons {
        display: flex;
        justify-content: space-around;

        width: 100%;
        height: 15%;
    }

    .btn {
        width: 20%;
        height: 50%;

        border-radius: 10px;
    }

    .Save {
        background-color: green;
    }

    .Close {
        background-color: brown;
    }
</style>