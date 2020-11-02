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
                <div class="singl_task">
                    <button class="bt_singl_task">.</button>
                    <input class="in_singl_task" type="text">
                    <select class="sel_singl_task">
                        <option>Work</option>
                        <option>Home</option>
                    </select>
                    <button class="bt_singl_task">0</button>
                </div>
            </div>
        </div>

        <div class="column-r">
            <div class="task_title">
                <input class="in_singl_task" type="text">
                <select class="sel_singl_task">
                    <option>Work</option>
                    <option>Home</option>
                </select>
                <button class="edit">Edit</button>
                <button class="save">Save</button>
            </div>

            <Timer style="text-align: center"
               :initial-value="360500"
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
               :paused="some_variable"
               :notify-every="'minute'"
            />
            <div class="control">
                <button class="bt_contol">Start</button>
                <button class="bt_contol">Stop</button>
                <button class="bt_contol">Wipe</button>
            </div>
        </div>
    </div>
</template>
<script>

import Timer from "@/components/Timer";

export default {
    name: "Tasks"
    ,
    components: {
        Timer,
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
    .singl_task {
        display: flex;
        justify-content: space-around;
        align-items: center;

        margin: 1%;
        height: 5%;

    }

    .bt_singl_task {
        border-radius: 50%;
        width: 10%;
        height: 100%;
    }

    .in_singl_task {
        width: 50%;
        height: 80%;
        min-height: 5%;
        text-align: center;
    }

    .sel_singl_task {
        width: 20%;
        height: 100%;
        padding-left: 3%;
    }

    .task_title {
        display: flex;
        justify-content: space-around;
        /*border: black solid 2px;*/
        border-radius: 10px;

        width: 80%;
        height: 4%;

        margin-top: 4%;
        margin-bottom: 10%;
    }

    .edit {
    }

    .save {
        display: none;
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
</style>