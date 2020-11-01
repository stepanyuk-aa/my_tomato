<template>
    <div class="settings">
        <div class="buttons">
            <h1>Settings</h1>
        </div>

        <div class="menu">
            <div class="text">Продолжительность интервала:</div>
            <input type="text">
        </div>

            <div class="menu">
                <div class="text">Длительность перерыва:</div>
                <input type="text">
            </div>

            <div class="menu">
                <div class="text">Время большого перерыва:</div>
                <input type="text">
                <div class="text">каждые</div>
                <input type="text">
            </div>

            <div class="buttons">
                <button class="back">Back</button>
                <button class="save">Save</button>
            </div>



    </div>
</template>

<script>
export default {
name: "Settings"
}
</script>

<style scoped>
    .settings {
        display: flex;
        flex-direction: column;
        margin-left: auto;
        margin-right: auto;
        margin-top: 5%;

        /*align-items: flex-start;*/
        justify-content: space-between;
        flex: 1 0 120px;
    }
    .menu {
        display: flex;
        margin: 1%;
        width: 40%;
        height: 5%;

        justify-content: center;
        align-items: center;

        border: black solid 2px;
        border-radius: 100px;
        background-color: #B09F83;
    }
    input {
        border-radius: 100px;
        width: 5%;
        height: 40%;
        text-align: center;
    }
    .buttons {
        display: flex;
        width: 100%;
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