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
    background: #84909F;
    width: 100%;
    display: flex;
    align-items: stretch;
    flex-direction: row;
    position: absolute;
    left:0;
    right:0;
    top:0;
    bottom:0;
}

.WorkSpace {
  padding: 1px 16px;
}
</style>
