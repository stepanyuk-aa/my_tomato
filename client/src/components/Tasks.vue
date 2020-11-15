<template>
    <div class="main_tasks">
        <div class="column">
            <div class="group">
                <select class="select_group">
                    <option>All</option>
                    <option>Work</option>
                    <option>Home</option>
                </select>
            </div>
            <div class="tasks">
                <SingleTask
                    v-for="task in tasks"
                    v-bind:key="task[0]"
                    v-bind:task="task"

                    @choose_task="f_choose_task"
                />
            </div>
            <div @click='fun_add_task' class="add_task icon"></div>
        </div>

        <div class="column-r">
            <Task :task="choose_task" ref="Task"/>
        </div>
    </div>
</template>
<script>
import SingleTask from "@/components/SingleTask";
import Task from "@/components/Task";

export default {
    name: "Tasks",
    props: ['tasks'],
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
            },
        }
    },
    components: {
        SingleTask,
        Task,
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

    .select_group {
        width: 95%;
        height: 50%;
        border-radius: 100px;
        padding-left: 3%;
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