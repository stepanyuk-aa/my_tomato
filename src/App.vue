<template>
  <div id="app">
    <NavigationPanel></NavigationPanel>
    <div class="WorkSpace">
      <h1>Hello</h1>
    </div>
  </div>
</template>

<script>
import NavigationPanel from "@/components/NavigationPanel";



export default {
  name: 'App',
  data() {
    return {
      title: "Hello!"
    }
  },
  components: {
    NavigationPanel,
  },
  methods: {

  },
}


</script>

<style>
#app {
  background: #F5F5F5;
  display: flex;
}

div.WorkSpace {
  padding: 1px 16px;
  height: 1000px;
}
</style>
