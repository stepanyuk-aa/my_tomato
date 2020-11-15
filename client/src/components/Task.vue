<template>
    <div class="task">
        <div class="task_title">
            <input class="in_singl_task" type="text" v-model="task.task">

            <select class="sel_singl_task">
                <option>Work</option>
                <option>Home</option>
            </select>

            <button @click="send_update_task" class="edit">Edit</button>
            <button class="save">Save</button>
        </div>

        <div class="textarea">
            <div class="lable_description">Описание:</div>
            <textarea class="text_description" v-model="task.des" > </textarea>
        </div>

        <div ></div>
        <div class="timer_param">
            Интервалов: <input class="count_interfals" v-model="task.count">
            по <input class="count_interfals" v-model="task.interval"> секунд
        </div>
        <div class="timer">
            <Timer style="text-align: center"
                   :initial-value="time"
                   :stroke-width="5"
                   :seconds-stroke-color="'#f00'"
                   :minutes-stroke-color="'#0ff'"
                   :hours-stroke-color="'#0f0'"
                   :underneath-stroke-color="'lightgrey'"
                   :seconds-fill-color="'#00ffff66'"
                   :minutes-fill-color="'#00ff0066'"
                   :hours-fill-color="'#ff000066'"
                   :size="200"
                   :padding="4"
                   :hour-label="'hours'"
                   :minute-label="'minutes'"
                   :second-label="'seconds'"
                   :show-second="true"
                   :show-minute="true"
                   :show-hour="false"
                   :show-negatives="true"
                   :notify-every="'minute'"
                   :paused="status"
                   ref="Timer"
            />
        </div>
        <!--            :paused="some_variable"-->

        <div ></div>
        <div ></div>

        <div class="control">
            <button @click="play"  class="bt_contol">Start</button>
            <button @click="paused" class="bt_contol">Stop</button>
            <button @click="wipe" class="bt_contol">Wipe</button>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import Timer from "@/components/Timer";

export default {
    name: "Task",
    props: ['task', 'ip'],
    data() {
        return {
            time: 5,
            status: true
        }
    },
    components: {
        Timer,
    },
    methods: {
        paused(){
            this.status = true
            this.task.timer = this.$refs.Timer.get_value()
            this.send_update_task()
        },
        play(){
            this.status = false
        },
        wipe(){
            this.$refs.Timer.updateTime(-this.time+1)
            this.$refs.Timer.updateTime(this.task.interval-1)
            this.time = this.task.interval
        },
        update_timer(n_time){
            if (n_time === 0) {
                this.$refs.Timer.updateTime(-this.time+1)
            }
            else {
                this.$refs.Timer.updateTime(-this.time+1)
                this.$refs.Timer.updateTime(n_time-1)
            }
            this.time = n_time
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
        send_update_task(){
            let token = this.local_storage('get','token')
            if (token === null){
                alert("Вы не авторизованы!")
            }
            else {
                if (this.task.id === 0) { alert("Вы не выбрали задачу!") }
                else {
                    axios
                        .post("http://" + this.ip + "/updatetask", {
                            'id': this.task.id,
                            'task': this.task.task,
                            'description': this.task.des,
                            'interval': this.task.interval,
                            'count': this.task.count,
                            'timer': this.task.timer,
                            "token": token
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
                }
            }
        },
    }
}
</script>

<style scoped>
    .task {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 1%;
        align-items: center;

        width: 90%;
        height: 100%;
    }

    .task_title {
        display: flex;
        justify-content: space-around;
        align-items: center;

        /*border: black solid 2px;*/
        border-radius: 10px;

        width: 100%;
        height: 4%;

        margin-top: 4%;
        margin-bottom: 10%;

        padding: 2%;
        border: black dashed 2px;
        border-radius: 10px;
    }

    .textarea {
        width: 100%;
        height: 10%;
        display: flex;
        justify-content: space-around;

        padding: 1%;
        border: black dashed 2px;
        border-radius: 10px;
    }

    .timer {
        display: flex;
        justify-content: space-around;
        align-items: center;

        width: 100%;
        height: 25%;

        padding: 2%;
        border: black dashed 2px;
        border-radius: 10px;
    }

    .text_description {
        width: 65%;
        border-radius: 10px;
        padding: 1%;
    }

    .edit {
        width: 10%;
        height: 100%;
    }

    .save {
        display: none;
    }

    .timer_param {
        width: 100%;
        height: 8%;

        display: flex;
        justify-content: space-around;
        align-items: center;

        padding: 1%;
        border: black dashed 2px;
        border-radius: 10px;
    }
    .count_interfals {
        width: 20%;
        height: 50%;
        text-align: center;
        background-color: #B09F83;
    }

    .control {
        display: flex;
        width: 60%;
        height: 15%;
        justify-content: space-around;

        margin-top: 10%;
    }

    .bt_contol {
        width: 30%;
        height: 50%;

        border-radius: 30%;
    }

    .lable_description {
        display: flex;
        justify-content: center;
        align-items: center;

        width: 30%;
        height: 40%;
    }

    .in_singl_task {
        width: 60%;
        height: 80%;
        min-height: 5%;
        text-align: center;
    }

    .sel_singl_task {
        width: 20%;
        height: 100%;
        padding-left: 3%;
    }
</style>