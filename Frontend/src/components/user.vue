<template>
  <v-app id="inspire"  style="background-image: linear-gradient(to top, #30cfd0 0%, #330867 100%);">
  	<v-toolbar color="#d9d9d9">
      <v-toolbar-title>Halo</v-toolbar-title>
    </v-toolbar>
    <v-container fill-height class="text-center">
      <v-row>
          <v-col cols="12"
           			 sm="12"
        			   md="12">
          			<v-btn color="#d9d9d9" @click="GetValue()" width="200px"  height="auto" style="font-size: 35px; color: #4d4d4d;">Get</v-btn>
          </v-col>
          <v-col  cols="12"
            			sm="12"
            			md="12">
           		  <v-btn color="#d9d9d9" @click="SetValue()" width="200px" height="auto" style="font-size:35px; color: #4d4d4d; margin-top: 30px;">Set</v-btn>
          </v-col>
      </v-row>
    </v-container>
 </v-app>
</template>
<script>
  export default {
    props: {
      source: String,
    },
    data: () => ({
      drawer: null,
    }),
    methods: {
      GetValue(){
        this.$router.push({ name: 'get'});
      },
      SetValue(){
      	this.$router.push({name:'set'});
      }
    },
  }
</script>