<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about"> About Us </router-link>

  </nav>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #0039b3;
  border-radius: 2px;
  text-decoration: none;
  border: none;
  padding: 5px;
  background-color: rgb(181, 255, 230);
}
</style>
