<template>
    <div class="main_tasks">
        <div class="column">
            <div class="group">
                <SelectGroup id="sg"  v-model="group" :groups="groups"></SelectGroup>
            </div>

            <div class="tasks">
                <SingleTask
                    v-for="task in group_tasks"
                    v-bind:key="task[0]"
                    v-bind:task="task"
                    @chage_status="f_chage_status"
                />
            </div>
            <div @click='fun_add_task' class="add_task icon"></div>
        </div>

        <div class="column-r">
            <Task :task="choose_task" :ip="ip" ref="Task"/>
        </div>
    </div>
</template>
<script>
import SingleTask from "@/components/SingleTask";
import Task from "@/components/Task";
import SelectGroup from "@/components/SelectGroup";
import axios from "axios";

export default {
    name: "Tasks",
    props: ['tasks', 'ip'],
    data() {
        return {
            add_tasks: true,
            choose_task: {
                id: 0,
                task: "",
                des: "",
                interval: 0,
                count: 0,
                timer: "",
                group: "",
            },
            group: "",
        }
    },
    components: {
        SingleTask,
        Task,
        SelectGroup,
    },
    computed: {
        group_tasks: function (){
            return this.tasks.filter(task => task[8] == this.group);
        }
    },
    methods: {
        fun_add_task(){
            console.log("Hello")
            this.add_tasks = true
            this.send()
        },
        send() {
            this.$emit('Tasks', {
                add_tasks: this.add_tasks,
            })
            this.add_tasks = false
        },
        f_choose_task(data){
            this.choose_task = data;
            this.$refs.Task.update_timer(
                parseInt(data.timer)
            )
        },

        f_chage_status(data){
            console.log(this.task)
            let token = this.local_storage('get','token')
            if (token === null){
                alert("Вы не авторизованы!")
            }
            else {
                axios
                    .post("http://" + this.ip + "/chagestatus", {
                        "id": data.id,
                        "status": data.status,
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
                this.interval = "";
                this.repeat = "";
            }

            this.$emit('updateTasks', {
                add_tasks: this.add_tasks,
            })
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
    }
}
</script>

<style scoped>
    .main_tasks {
        display: flex;
        margin-left: auto;
        margin-right: auto;

        flex: 1 0 120px;
        justify-content: space-around;
    }

    .column {
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 1%;
        align-items: center;

        width: 50%;
    }
    .column-r {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 1%;
        align-items: center;

        width: 50%;
    }
    .group {
        display: flex;
        width: 100%;
        height: 10%;
        justify-content: center;
        align-items: center;
    }
    #sg.root_select {
        width: 100%;
        height: 50%;
        border-radius: 100px;
    }

    .tasks {
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 90%;
    }


    .add_task {
        background: url('../img/add_task.svg') no-repeat ;
        width: 8%;
        height: 8%;

        align-self: center;
    }
</style>