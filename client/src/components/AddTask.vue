<template>
    <div class="modal">
        <div class="task_title">
            <h1>Добавить задание </h1>
            <hr>
        </div>
        <div class="task_body">
            <div class="row">
                <p>Задание:</p>
                <input v-model="task" class="input_add_task" type="text">
            </div>
            <div class="row">
                <p>Описание</p>
                <input v-model="description" class="input_add_task" type="textarea">
            </div>
            <div class="row">
                <p>Тип</p>

                <div class="row_group">
                    <input v-model="group" class="input_new_group" type="textarea">
                    <SelectGroup v-model="group" :groups="groups"></SelectGroup>
                </div>
            </div>
            <div class="row">
                <p>Интервал:</p>
                <input v-model="interval" class="input_add_task" type="text">
            </div>
            <div class="row">
                <p>Повторений:</p>
                <input v-model="repeat" class="input_add_task" type="text">
            </div>
        </div>
        <div class="task_buttons">
            <button class="Close btn" @click="close">Close</button>
            <button class="Save btn"  @click="send_task">Save</button>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import SelectGroup from "@/components/SelectGroup";

export default {
    name: "AddTask",
    components: {SelectGroup},
    props: ['ip'],
    data() {
        return {
            showModal: false,
            task: "",
            description: "",
            interval: "",
            repeat: "",
            group: "",
            groups: [],
        }
    },
    methods: {
        close(){
            this.showModal = false
            this.$emit('Close_Add_Task')
        },
        local_storage(mode, key, value = ''){
            if (mode === 'set') {
                if (key == "token") { this.token = value }

                console.log("Set:" , key, "|", value)
                localStorage.setItem(key, value)
            }
            else {
                return localStorage.getItem(key)
            }
        },
        get_groups(){
            let token = this.local_storage('get','token')
            if (token === null){
                alert("Вы не авторизованы!")
            }
            else {
                axios
                    .post("http://" + this.ip + "/getgroups", {
                        "token": token,
                    })
                    .then((response) => {
                        this.groups = response.data.groups
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            }
        },
        send_task(){
            console.log(this.task)
            if (this.task === undefined && this.interval === undefined && this.repeat === undefined){
                alert("Некоторые поля не заполнены!")
            }
            else {
                let token = this.local_storage('get','token')
                if (token === null){
                    alert("Вы не авторизованы!")
                }
                else {
                    axios
                        .post("http://" + this.ip + "/addtask", {
                            'task': this.task,
                            'description': this.description,
                            'intervall': this.interval,
                            "repeat": this.repeat,
                            "group": this.group,
                            "token": token,
                        })
                        .then((response) => {
                            if (response.data.status === "success") {
                                console.log(response.data);
                            } else {
                                console.log(response.data);
                            }
                        })
                        .catch((error) => {
                            console.log(error);
                        });

                    this.task = "";
                    this.description = "";
                    this.intervall = "";
                    this.repeat = "";
                }
            }
            this.$emit('Close_Add_Task')
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
    .row_group {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        height: 90%;
        margin-left: 24%;
    }
    .input_add_task {
        width: 60%;
        height: 50%;
        margin-left: 10%;
        border-radius: 10px;
    }
    .input_new_group {
        text-align: center;
        width: 40%;
        height: 50%;
        margin-left: 14%;
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