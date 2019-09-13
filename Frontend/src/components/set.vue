<template>
	<v-app id="inspire" style="background-image: linear-gradient(to top, #30cfd0 0%, #330867 100%);">
    <div>
           <v-toolbar color="#d9d9d9">
          <v-toolbar-title>Halo</v-toolbar-title>
      </v-toolbar>
    </div>
		<v-container
	fluid >
		<v-row>
    <v-col cols="12" sm="6" md="3">
      <v-text-field
         label="Enter Key"
         v-model="key"
         type="text"
         color="#d9d9d9"
         solo>
           </v-text-field>
    </v-col>
    <v-col cols="12" sm="6" md="3">
      <v-text-field
         label="Enter Value"
         v-model="value"
         type="text"
         color="#d9d9d9"
         solo>
           </v-text-field>
    </v-col>
  </v-row>
  <v-row>
        <v-col cols="12" sm="6" md="3">
      <v-btn 
      color="dark-grey" 
      text 
      @click="Submit()" 
      style="background-color: #d9d9d9">
      Submit
      </v-btn>
    </v-col>
  </v-row> 
  <div id="set" style="color:#d9d9d9;font-size: 20px;margin-top: 20px;margin-left: 10px;"></div>
	</v-container>
	</v-app>
</template>

<script>
  export default {

    props: {
      source: String,
    },

	data: () => ({

    }),
    
    methods: {
         Submit(){
          var res=String
          const dat ={
          key :this.key,
          value:this.value
      };
      this.$http.post('http://localhost:5000/insert', dat,{
          headers: {
            'Content-Type': 'application/json'
          }}).then((resp)=>{
          res = resp.data
          console.log(res)
          if(res == "inserted"){
            document.getElementById('set').innerHTML = "Data inserted";
          }
          else{
            document.getElementById('set').innerHTML = "Key already exist";
          }
        });
      } 
    },
}
</script>






	