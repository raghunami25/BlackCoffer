<template>
  <v-app id="inspire"  style="background-image: linear-gradient(to top, #30cfd0 0%, #330867 100%);">
    <v-content>
      <v-container fluid fill-height>
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="4"
          >
            <v-card class="elevation-25" height="100%" overflow-y=auto;>
              <v-toolbar
                color="primary"
                dark
                flat
              >
               <v-toolbar-title>Halo</v-toolbar-title>
            </v-toolbar>
               
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="Login"
                    v-model="login"
                    prepend-icon="person"
                    type="text"
                  ></v-text-field>

                  <v-text-field
                    label="Password"
                    v-model="password"
                    prepend-icon="lock"
                    type="password"

                  ></v-text-field>
                </v-form>
                <div id="invalid" style="color:#4d4d4d; font-size:15px"> </div>
              </v-card-text>
              <v-card-actions>
                <div class="flex-grow-1"></div>
                <v-btn color="primary"  @click="Login()">Login</v-btn>
                <v-btn color="primary"  @click="Sign()">Sign Up</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
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
      Login(){
      	var res = String
      	const dat = {
      		username : this.login,
      		password : this.password
      	};
        this.$http.post('http://localhost:5000/login', dat,{
  			 	headers: {
       			'Content-Type': 'application/json'
   				}}).then((resp)=>{
   				res = resp.data
   				if(res == "valid user"){
   					this.$router.push({ name: 'home' });
   				}
          else{
            document.getElementById('invalid').innerHTML = "Invalid Username or Password";
          }
   				
   			});
      },
      Sign(){
      	this.$router.push({name:'register'});
      },
    },
  }
</script>

