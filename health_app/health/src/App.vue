<template>
  <div id = 'mainapp'>
  <h2>MedhaIR Health Tracker </h2>
  <button>Login</button>
  <user_login />
  </div>
</template>

<script>
import user_login from './components/user_login.vue'
export default {
  name: 'App',

  components: {user_login
  }, 

  data () {
    return {
      test : 'this is test data'
    }
  },

  methods : {
    handlemouse() {
      return "this is the test event !! "
    }
  }

}
</script>

<style scoped >
#mainapp {
  background-color: deepskyblue;
  border-radius: 10px;
  padding: 5px;
}

p, h2 {
  text-align: center;
  font-weight: bold;
  font-family: 'Varela Round', sans-serif;
  
}

button {
  border-radius: 2px;
  padding: auto auto ;
}
</style>
