<template>
	<v-app id="inspire" style="background-image: linear-gradient(to top, #30cfd0 0%, #330867 100%);">
  <div>
	  <v-toolbar color="#d9d9d9">
      <v-toolbar-title>Halo</v-toolbar-title>
    </v-toolbar>
  </div>
	<v-container
	fluid>
	  <v-row >
		  <v-col cols="12" sm="6" md="3">
			  <v-text-field
 	       label="Enter Key"
    	   v-model="key"
    	   prepend-inner-icon="search"
    	   type="text"
    	   color="black"
    	   solo
    	   clearable
    	   >
        </v-text-field>
		  </v-col>
		  <v-col cols="12" sm="6" md="3">
			  <v-btn 
			   color="dark-grey" 
			   text 
			   @click="search()" 
			   style="background-color: #d9d9d9; margin-left: 20px; margin-top: 6px">
			   Search
			</v-btn>
      <v-btn 
			   color="dark-grey" 
			   text 
			   @click="modify()" 
			   style="background-color: #d9d9d9; margin-left: 24px; margin-top: 6px">
			   Modify
			</v-btn>
		</v-col>
	</v-row>
	<v-row>
		<v-col cols="12" sm="6" md="3">
			<v-text-field
          id="textbox3"
    	   	type="text"
    	   	color="black"
    	   	solo
    	   	v-model="new_value"
       	   	clearable
    	   	> 
    	   	</v-text-field>
         </v-col>
	</v-row>
  <div id="get" style="color:#d9d9d9;font-size: 20px;margin-top: 20px; margin-left: 10px;"></div>
	</v-container>
	</v-app>
</template>

<script>
  export default {

    props: {
      source: String,
    },

	data: () => ({
		seen:false
    }),
    
    methods: {
      search(){
      	var res = String
      	const dat = {
      		key : this.key
      	};
      	this.$http.post('http://localhost:5000/getvalue', dat,{
  			 	headers: {
       			'Content-Type': 'application/json'
   				}}).then((resp)=>{
   				res = resp.data
          var textbox3 = document.getElementById('textbox3');
          textbox3.value = res.value;
   			});
    },
    logout(){
    	console.log("hello")
    },
    modify(){
    	var res = String
    	const dat = {
      		key : this.key,
      		value:this.new_value
      	};
      	this.$http.post('http://localhost:5000/updatevalue', dat,{
  			 	headers: {
       			'Content-Type': 'application/json'
   				}}).then((resp)=>{
   				res = resp.data
          console.log(res)
   				if(res == "updated"){
            document.getElementById('get').innerHTML = "Data Updated";
          }
   			});

    },

	},
}
</script>






	