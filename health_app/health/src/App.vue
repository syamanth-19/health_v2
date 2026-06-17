<template>
  <div id = 'mainapp'>
  <h2>MedhaIR Health Tracker </h2>
  <div class="log" v-if = logged><button @click = handlemouse >Login</button></div>
  
  <div >
    <user_login />
  </div>
  
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
      test : 'this is test data',
      logged : false
    }
  },

  methods : {
    handlemouse() {
      console.log("this is the test event !! ")
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

.log {
  text-align: right;
}
</style>
