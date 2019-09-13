<template>
  <v-app>
 

    <v-content>
<!--       <HelloWorld @userlogin='userlogin'>
      </HelloWorld> -->
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';
import User from './components/user'
export default {
  name: 'App',
 
  components: {
    HelloWorld,
    User
  },
  data: () => ({
    result:'',
    userlogin: Object,
  }),

  // methods: {
  //   userlogin(variable){
  //     this.result = variable;
  //     console.log("hello")
  //     console.log(this.result);
  //   }
  // }
};
</script>
