<template>
  <div id="main">
    <TodoTasks/>
  </div>
</template>
<script>
  import TodoTasks from './components/TodoTasks';
  export default {
    name: 'App',
    data: () => ({}),
    components: {
      TodoTasks,
    },
  };
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>