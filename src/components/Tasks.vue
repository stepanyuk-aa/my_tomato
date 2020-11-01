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
        <div class="midle"> </div>
        <div class="column">
            <div class="border">2</div>
            <div class="border">2</div>
            <div class="border">2</div>
        </div>
    </div>
</template>

<script>
export default {
name: "Tasks"
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

    .border {
        border: black solid 2px;
        width: 100%;
        height: 20%;
        margin: 5%;
    }
    .red {
        border: red solid 2px;
        background-color: red;
    }
    .green {
        border: #42b983 solid 2px;
        background-color: #42b983;
    }
</style>